# Harbor RL Environment & Agent Evaluation

A debugging and evaluation environment for a payment reconciliation CLI application, built to explore automated debugging, reward design, and agent evaluation using Harbor.

## Overview

The task contains three intentional debugging challenges:

- CLI input handling and argument validation
- Transaction status normalization and monetary rounding
- Timezone-aware timestamp ordering and duplicate transaction handling

## Reward Configuration

| Component | Weight |
|---|---:|
| CLI behavior | 0.20 |
| Status normalization and rounding | 0.30 |
| Timestamp ordering and deduplication | 0.50 |
| **Total** | **1.00** |

## Evaluation Results

The following completed validation runs were recovered from the existing Harbor job artifacts.

| Evaluation | Trials | Mean Reward |
|---|---:|---:|
| Phase 1 Oracle | 1 | 1.00 |
| Phase 1 Nop | 1 | 0.00 |
| Dense Reward Oracle | 1 | 1.00 |
| Dense Reward Nop | 1 | 0.00 |
| Codex (gpt-5.6-terra) | 1 | 1.00 |

These are individual validation runs, not a completed three-trial baseline or ablation comparison. The interrupted and incomplete runs are not presented as completed results.

Detailed result and trajectory artifacts are available in `jobs_summary/`.

## Short RL Concepts

**1. What is a reward function?**

A reward function assigns a numerical score to an agent's actions or final outcome. It guides the agent toward the desired behavior.

**2. What is an episode?**

An episode is one complete interaction between an agent and an environment, from the initial state to a terminal state.

**3. What is a trajectory?**

A trajectory is the sequence of states, actions, and observations collected during an episode.

**4. What is an ablation study?**

An ablation study removes or changes one component at a time to understand how much that component contributes to overall performance.

**5. Why compare baseline and oracle agents?**

A baseline provides a reference for normal agent performance, while an oracle provides an upper-bound reference using an ideal or known solution.

## Technology Stack

- Python
- Docker
- Harbor
- Pytest
- Shell scripting
- Git and GitHub

## Repository Structure

- `tasks/reconcile-bug/` - Task definition, environment, solution, and tests
- `jobs_summary/` - Selected evaluation results, trajectories, and validation summary
- `ai_transcripts/` - Sanitized AI coding-session transcripts

## Getting Started

1. Clone the repository.
2. Install the required dependencies and Docker.
3. Review `tasks/reconcile-bug/instruction.md`.
4. Run the environment and evaluations using the Harbor CLI.

## Demo

Loom demonstration: https://www.loom.com/share/54fe585047704f959b0291490dbbfbe5

## Purpose

An experimental environment for exploring debugging, automated verification, reward design, and agent-based software problem solving.
