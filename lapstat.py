#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Seiya Fukushima
# SPDX-License-Identifier: BSD-3-Clause

import sys

lap_times = []

# Read lap times from standard input
for line in sys.stdin:
    try:
        lap_time = float(line.strip())
        lap_times.append(lap_time)
    except ValueError:
        print("Invalid lap time", file=sys.stderr)
        sys.exit(1)

# Check whether lap times were entered
if len(lap_times) == 0:
    print("No lap times entered", file=sys.stderr)
    sys.exit(1)

# Calculate lap statistics
best = min(lap_times)
worst = max(lap_times)
average = sum(lap_times) / len(lap_times)

# Display results
print(f"Fastest lap: {best:.2f} sec")
print(f"Slowest lap: {worst:.2f} sec")
print(f"Average lap: {average:.2f} sec")
