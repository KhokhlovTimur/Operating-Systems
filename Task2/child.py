#!/usr/bin/python3

import os
import sys
import random
import time

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage python child.py S")
        sys.exit(1)

    S = int(sys.argv[1])
    print(f"Child[{os.getpid()}] I am started. My PID is {os.getpid()}. Parent PID is {os.getppid()}")

    time.sleep(S)

    exit_status = random.choice([0, 1])
    print(f"Child[{os.getpid()}] I am ended. My PID is {os.getpid()}. Parent PID is {os.getppid()}")
    sys.exit(exit_status)