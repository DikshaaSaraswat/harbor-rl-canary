"""Black-box checks using verifier-owned fixtures, independent of sample.csv."""

import json
import os
import subprocess
import sys
import tempfile
from decimal import Decimal
from pathlib import Path

import pytest


PROGRAM = Path(os.environ.get("RECONCILE_PROGRAM", "/app/reconcile.py"))


def run_cli(csv_text, *arguments):
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", newline="", suffix=".csv"
    ) as fixture:
        fixture.write(csv_text)
        fixture.flush()
        result = subprocess.run(
            [sys.executable, str(PROGRAM), *arguments, fixture.name],
            capture_output=True,
            text=True,
            check=False,
        )
    assert result.returncode == 0, f"CLI failed: {result.stderr}"
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        pytest.fail(f"CLI did not print JSON: {exc}; output={result.stdout!r}")
    assert isinstance(payload, dict)
    assert set(payload) == {"total_valid_amount", "valid_count", "failed_count"}
    return payload


def assert_summary(payload, total, valid, failed):
    assert Decimal(str(payload["total_valid_amount"])) == Decimal(total)
    assert payload["valid_count"] == valid
    assert payload["failed_count"] == failed


@pytest.mark.category_cli
def test_positional_csv_path():
    payload = run_cli(
        "tx_id,timestamp,amount,status\n"
        "independent-a,2024-04-03T08:00:00+00:00,6.40,success\n"
        "independent-b,2024-04-03T08:01:00+00:00,9.00,failed\n"
    )
    assert_summary(payload, "6.40", 1, 1)


@pytest.mark.category_status
def test_status_normalization_and_half_up_rounding():
    payload = run_cli(
        "tx_id,timestamp,amount,status\n"
        "status-a,2024-04-03T08:00:00+00:00,1.005, SUCCESS  \n"
        "status-b,2024-04-03T08:01:00+00:00,0.004, success\n"
        "status-c,2024-04-03T08:02:00+00:00,80.00,  FaIlEd \n"
        "status-d,2024-04-03T08:03:00+00:00,50.00, pending \n"
    )
    # 1.005 + 0.004 rounds to 1.01 with decimal half-up rounding.
    assert_summary(payload, "1.01", 2, 1)


@pytest.mark.category_timestamp
def test_latest_timezone_aware_instant_wins():
    payload = run_cli(
        "tx_id,timestamp,amount,status\n"
        # The later instant appears first; the later CSV row is actually older.
        "offset,2024-04-03T08:30:00-04:00,3.00,failed\n"
        "offset,2024-04-03T12:00:00+00:00,10.00,success\n"
        # These are the same instant, so the later CSV row must win.
        "tie,2024-04-03T09:00:00+00:00,20.00,success\n"
        "tie,2024-04-03T04:00:00-05:00,7.25,failed\n"
        # A separate transaction ensures the expected aggregate is distinctive.
        "keep,2024-04-03T09:15:00+00:00,2.00,success\n"
    )
    assert_summary(payload, "2.00", 1, 2)
