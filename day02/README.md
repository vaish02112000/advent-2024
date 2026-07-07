# Day 2: Red-Nosed Reports

## Problem

Determine how many reports are safe.

A report is considered safe if:

- All numbers are strictly increasing or strictly decreasing.
- The difference between adjacent numbers is between 1 and 3 inclusive.

## Solution

The solution checks each report by verifying whether it is strictly increasing or strictly decreasing while ensuring every adjacent difference is within the allowed range.

### Time Complexity

O(n) per report

### Language

Python 3
