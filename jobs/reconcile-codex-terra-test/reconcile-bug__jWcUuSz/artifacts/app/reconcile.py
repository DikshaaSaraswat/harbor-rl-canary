#!/usr/bin/env python3
"""Select the latest record for each transaction and reconcile its result."""

import argparse
import csv
import json
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP


def parse_timestamp(value: str) -> datetime:
    """Parse an ISO 8601 timestamp as a timezone-aware instant."""
    value = value.strip()
    # ``fromisoformat`` on older Python releases does not accept a trailing Z.
    if value.endswith(("Z", "z")):
        value = f"{value[:-1]}+00:00"
    timestamp = datetime.fromisoformat(value)
    if timestamp.tzinfo is None or timestamp.utcoffset() is None:
        raise ValueError("timestamp must include a timezone offset")
    return timestamp


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="CSV file to reconcile")
    args = parser.parse_args()

    # Each value includes its parsed instant. Replacing on equality deliberately
    # gives a same-instant tie to the record later in the CSV.
    latest_by_id: dict[str, tuple[datetime, dict[str, str]]] = {}
    with open(args.input, newline="", encoding="utf-8") as csv_file:
        for row in csv.DictReader(csv_file):
            timestamp = parse_timestamp(row["timestamp"])
            transaction_id = row["tx_id"]
            previous = latest_by_id.get(transaction_id)
            if previous is None or timestamp >= previous[0]:
                latest_by_id[transaction_id] = (timestamp, row)

    valid_total = Decimal("0")
    valid_count = 0
    failed_count = 0
    for _, row in latest_by_id.values():
        status = row["status"].strip().casefold()
        if status == "success":
            valid_total += Decimal(row["amount"])
            valid_count += 1
        elif status == "failed":
            failed_count += 1

    rounded_total = valid_total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    # Decimal is not JSON-serializable by default. Its fixed-point spelling is
    # a valid JSON number and retains the requested two decimal places.
    result = {
        "total_valid_amount": str(rounded_total),
        "valid_count": valid_count,
        "failed_count": failed_count,
    }
    encoded = json.dumps(result, separators=(",", ":"))
    print(encoded.replace(f'"{rounded_total}"', str(rounded_total), 1))


if __name__ == "__main__":
    main()
