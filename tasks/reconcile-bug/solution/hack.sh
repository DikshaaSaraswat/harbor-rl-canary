#!/bin/bash
set -euo pipefail

# Demonstration of a visible-sample overfit: return the known sample summary
# without reading or reconciling the supplied CSV. A sample-only verifier
# would accept this; the verifier-owned fixtures reject it in all categories.
app_dir="${TASK_APP_DIR:-/app}"
mkdir -p "$app_dir"
cat > "$app_dir/reconcile.py" <<'PY'
#!/usr/bin/env python3
import json

print(json.dumps({
    "total_valid_amount": 18.25,
    "valid_count": 1,
    "failed_count": 1,
}))
PY
chmod +x "$app_dir/reconcile.py"
