# Harbor RL Environment & Agent Evaluation

Author: Diksha Saraswat

## Project
Payment reconciliation debugging task with three intentional bugs: CLI argument handling, status normalization, and timezone-aware timestamp deduplication.

## Dense Rewards
- CLI behavior: 0.20
- Status normalization and rounding: 0.30
- Timestamp ordering and deduplication: 0.50
- Total: 1.00

## Validation
- Oracle Phase 1: 1.00
- Nop Phase 1: 0.00
- Oracle dense reward: 1.00
- Nop dense reward: 0.00
- Codex retry: failed because model name was missing.
- Hardcoded-output hack: rejected, reward 0.00.

## Limitations
The requested three-trial LLM baseline and ablation comparison remain incomplete. No results have been fabricated.

## Structure
- tasks/reconcile-bug/: task, environment, solution and verifier.
- jobs/: raw Harbor results.
- jobs_summary/: evaluation summaries.

## Demo
Loom URL: Pending.

## Evaluation Summary
See [jobs_summary/validation_summary.md](jobs_summary/validation_summary.md) for the recorded Oracle and Nop validation results.
