# Payment reconciliation

Implement `reconcile.py` as a command-line program that reads a CSV file with
the columns `tx_id,timestamp,amount,status` and prints one JSON object.

Run it as:

```bash
python reconcile.py input.csv
```

Timestamps are ISO 8601 values and include timezone offsets. Treat timestamps
as instants when choosing one record per transaction ID. If records for the
same ID represent the same instant, use the one appearing later in the CSV.

Trim surrounding whitespace from statuses and compare them without regard to
letter case. Count `success` records as valid and `failed` records as failed;
exclude records with any other status. Sum the valid amounts using decimal
arithmetic and round the final total to two decimal places using
round-half-up. The JSON object must contain exactly these keys:
`total_valid_amount`, `valid_count`, and `failed_count`.

The sample input is `sample.csv`.
