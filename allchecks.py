#!/usr/bin/env python3

import shutil
import sys

def check_reboot():
    """Return True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_absolute, min_percent):
    """Return True if there isn't enough disk space, False otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free < min_percent or gigabytes_free < main_absolute:
        return True
    return False

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    if check_disk_full("/", 2, 10):
        print("Disk Full!")
        sys.exit(0)

main()
