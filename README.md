# Harbor RL Environment & Agent Evaluation

A debugging and evaluation environment for a payment reconciliation CLI application.

## Overview

The project contains three debugging challenges:

- CLI input handling and argument validation
- Transaction status normalization and monetary rounding
- Timezone-aware timestamp ordering and duplicate transaction handling

## Reward Configuration

| Component | Weight |
|---|---:|
| CLI behavior | 0.20 |
| Status normalization and rounding | 0.30 |
| Timestamp ordering and deduplication | 0.50 |
| Total | 1.00 |

## Technology Stack

- Python
- Docker
- Harbor
- Pytest
- Shell scripting
- Git and GitHub

## Repository Structure

- `tasks/reconcile-bug/` - Task definition, environment, solution and tests
- `jobs/` - Evaluation artifacts
- `jobs_summary/` - Evaluation summaries

## Getting Started

1. Clone the repository.
2. Install the required dependencies and Docker.
3. Review `tasks/reconcile-bug/instruction.md`.
4. Run the environment and evaluations using Harbor CLI.

## Evaluation

The project uses reference solutions, baseline agents and automated verifier tests to assess task performance.

## Purpose

An experimental environment for exploring debugging, automated verification and agent-based software problem solving.
