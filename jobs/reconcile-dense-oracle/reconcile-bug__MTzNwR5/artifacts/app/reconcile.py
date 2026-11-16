#!/usr/bin/env python3
import argparse
import csv
import json
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP


def parse_timestamp(value):
    timestamp = datetime.fromisoformat(value)
    if timestamp.tzinfo is None or timestamp.utcoffset() is None:
        raise ValueError("timestamps must include a timezone offset")
    return timestamp


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", help="CSV file to reconcile")
    args = parser.parse_args()

    latest_by_id = {}
    with open(args.csv_path, newline="", encoding="utf-8") as csv_file:
        for row in csv.DictReader(csv_file):
            timestamp = parse_timestamp(row["timestamp"])
            tx_id = row["tx_id"]
            current = latest_by_id.get(tx_id)
            if current is None or timestamp >= current[0]:
                latest_by_id[tx_id] = (timestamp, row)

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

    total = valid_total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    print(json.dumps({
        "total_valid_amount": float(total),
        "valid_count": valid_count,
        "failed_count": failed_count,
    }))


if __name__ == "__main__":
    main()
