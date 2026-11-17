# Harbor Evaluation Summary

## Completed Validation Runs

| Run | Completed trials | Mean reward | Errors |
|---|---:|---:|---:|
| Oracle Phase 1 | 1 | 1.00 | 0 |
| Nop Phase 1 | 1 | 0.00 | 0 |
| Oracle dense reward | 1 | 1.00 | 0 |
| Nop dense reward | 1 | 0.00 | 0 |
| Codex gpt-5.6-terra | 1 | 1.00 | 0 |
| Hardcoded-output hack | 1 | 0.00 | Rejected |

## Codex Baseline Attempt

A three-trial run using gpt-5.6-terra was interrupted after the machine became unresponsive.

At the time its results were inspected:
- Total trials: 3
- Completed: 0
- Running: 1
- Pending: 2
- Errored: 0

This run does not provide a completed three-trial baseline result.

## Interpretation

The Oracle runs achieved the expected reward of 1.00, while the Nop runs received 0.00. The hardcoded-output attempt was rejected by the verifier. One Codex gpt-5.6-terra trial completed successfully with reward 1.00.

The requested three-trial LLM baseline and ablation comparison remain incomplete. No group advantages, missing trial outcomes, or ablation results have been invented.

## Limitations

The interrupted baseline was not rerun due to machine stability and time constraints. The Loom demonstration link is pending.
