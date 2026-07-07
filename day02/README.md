# Advent of Code 2024 - Day 2: Red-Nosed Reports

This repository contains my Python solution for **Advent of Code 2024 – Day 2**.

## Problem

Given a list of reactor safety reports, determine:

- **Part 1:** Count reports that are strictly increasing or strictly decreasing, where each adjacent difference is between 1 and 3.
- **Part 2:** Extend the solution by allowing the removal of a single level (Problem Dampener) if it makes an otherwise unsafe report valid.

## Solution

The implementation includes:

- `is_safe()` – Validates a report using the Part 1 rules.
- `is_safe_with_dampener()` – Checks whether removing one level makes a report safe.
- `count_part1()` – Computes the Part 1 result.
- `count_part2()` – Computes the Part 2 result.

## Results

| Part | Answer |
|------|-------:|
| Part 1 | 224 |
| Part 2 | 293 |

## Requirements

- Python 3.x

## Usage

Place your puzzle input in a file named `input.txt` in the same directory and run:

```bash
python solution.py
```

Example output:

```text
Part 1: 224
Part 2: 293
```

## Time Complexity

- **Part 1:** O(n) per report
- **Part 2:** O(n²) per report (checks all possible single-level removals)
