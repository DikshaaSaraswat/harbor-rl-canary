#!/usr/bin/env python3
"""Reconcile transaction rows from a CSV file."""

import argparse
import csv
import json
from decimal import Decimal, ROUND_HALF_UP


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="CSV file to reconcile")
    args = parser.parse_args()

    latest_by_id = {}
    with open(args.input, newline="", encoding="utf-8") as csv_file:
        for row in csv.DictReader(csv_file):
            # Rows are overwritten as read, so the last row wins for each ID.
            latest_by_id[row["tx_id"]] = row

    valid_total = Decimal("0")
    valid_count = 0
    failed_count = 0
    for row in latest_by_id.values():
        if row["status"] == "success":
            valid_total += Decimal(row["amount"])
            valid_count += 1
        elif row["status"] == "failed":
            failed_count += 1

    rounded_total = valid_total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    print(
        json.dumps(
            {
                "total_valid_amount": float(rounded_total),
                "valid_count": valid_count,
                "failed_count": failed_count,
            }
        )
    )


if __name__ == "__main__":
    main()
