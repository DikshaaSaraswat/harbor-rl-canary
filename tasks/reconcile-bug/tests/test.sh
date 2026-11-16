#!/bin/bash
set -u

# Run each behavioral category separately so failures in one area do not erase
# earned credit in another. Harbor parses the resulting plain-text float.
score_hundredths=0

pytest --ctrf /logs/verifier/ctrf-cli.json /tests/test_outputs.py -m category_cli -rA
cli_status=$?
pytest --ctrf /logs/verifier/ctrf-status.json /tests/test_outputs.py -m category_status -rA
status_status=$?
pytest --ctrf /logs/verifier/ctrf-timestamp.json /tests/test_outputs.py -m category_timestamp -rA
timestamp_status=$?

if [ "$cli_status" -eq 0 ]; then
  score_hundredths=$((score_hundredths + 20))
fi
if [ "$status_status" -eq 0 ]; then
  score_hundredths=$((score_hundredths + 30))
fi
if [ "$timestamp_status" -eq 0 ]; then
  score_hundredths=$((score_hundredths + 50))
fi

if [ "$score_hundredths" -eq 100 ]; then
  printf '1.0\n' > /logs/verifier/reward.txt
else
  printf '%d.%02d\n' "$((score_hundredths / 100))" "$((score_hundredths % 100))" \
    > /logs/verifier/reward.txt
fi
