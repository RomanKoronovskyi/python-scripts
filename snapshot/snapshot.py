import argparse
import json
import os
import time
import psutil
from datetime import datetime

class Snapshot:
    def get_info(self):
        all_processes = list(psutil.process_iter())
        result_processes = {"total": 0, "running": 0, "sleeping": 0, "stopped": 0, "zombie": 0}

        for proc in all_processes:
            status = proc.status()
            if status == psutil.STATUS_RUNNING:
                result_processes["running"] += 1
            elif status == psutil.STATUS_SLEEPING:
                result_processes["sleeping"] += 1
            elif status == psutil.STATUS_STOPPED:
                result_processes["stopped"] += 1
            elif status == psutil.STATUS_ZOMBIE:
                result_processes["zombie"] += 1

        return {
            "total": len(all_processes),
            "running": result_processes["running"],
            "sleeping": result_processes["sleeping"],
            "stopped": result_processes["stopped"],
            "zombie": result_processes["zombie"]
        }

    def cpu(self):
        all_cpus = psutil.cpu_times_percent(interval=1)

        return{
            "user": all_cpus.user,
            "system": all_cpus.system,
            "idle": all_cpus.idle
        }

    def memory(self):
        all_memory = psutil.virtual_memory()

        return {
            "total": all_memory.total // 1024,
            "free": all_memory.free // 1024,
            "used": all_memory.used // 1024
        }

    def swap(self):
        all_swap = psutil.swap_memory()

        return {
            "total": all_swap.total // 1024,
            "free": all_swap.free // 1024,
            "used": all_swap.used // 1024
        }

    def timestamp(self):
        time = int(datetime.now().timestamp())

        return {"Timestamp": time}

    def full_snapshot(self):
        return {
            "Tasks": self.get_info(),
            "%CPU": self.cpu(),
            "KiB Mem": self.memory(),
            "KiB Swap": self.swap(),
            **self.timestamp()
        }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="Interval between snapshots in seconds", type=int, default=30)
    parser.add_argument("-f", help="Output file name", default="snapshot.json")
    parser.add_argument("-n", help="Quantity of snapshots to output", type=int, default=20)
    args = parser.parse_args()

    monitor = Snapshot()

    with open(args.f, "w") as file:
        file.write("")

    for _ in range(args.n):
        snap = monitor.full_snapshot()
        os.system("clear")
        print(json.dumps(snap, indent=4))
        print(snap, end="\r")
        with open(args.f, "a") as file:
            file.write(json.dumps(snap) + "\n")

    time.sleep(args.i)

if __name__ == "__main__":
    main()
