## Snapshot task

Python script for capturing system snapshots including processes, CPU usage, memory, swap, and timestamps. Snapshots can be printed to the console and saved to a JSON file.

---

## Overview

The script collects the following system information:

- **Processes**: number of running, sleeping, stopped, and zombie processes
- **CPU usage**: user, system, idle percentages
- **Memory usage**: total, free, and used memory (KiB)
- **Swap usage**: total, free, and used swap (KiB)
- **Timestamp**: current UNIX timestamp

Snapshots can be collected at a specified interval and written to a file.

---

## Requirements

- Python 3.10+
- Python modules:
  - `psutil`
  - `argparse`
  - `json`

Install required dependencies:

```bash
pip install psutil
```
## Usage

To run the snapshot monitor script, use the following command:

```bash
python snapshot.py [-i INTERVAL] [-f FILENAME] [-n NUMBER]
```
