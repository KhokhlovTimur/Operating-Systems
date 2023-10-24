import os
import sys
import random
import time

def create_child():
    child_pid = os.fork()

    if child_pid == 0:
        sleep_duration = random.randint(5, 10)
        args = ['child.py', str(sleep_duration)]
        os.execvp('/usr/bin/python3', ['/usr/bin/python3'] + args)  
        print("Error in execvp")
        sys.exit(1)
    else:
        return child_pid

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Correct args: python parent.py N")
        sys.exit(1)

    N = int(sys.argv[1])
    children = []

    for child_num in range(1, N + 1):
        child_pid = create_child()
        if child_pid is not None:
            children.append(child_pid)
            print(f"Parent[{os.getpid()}]: I ran children process with PID {child_pid}")

    while children:
        terminated_pid, status = os.wait()
        if os.WIFEXITED(status):
            print(f"Parent[{os.getpid()}]: Child with PID {terminated_pid}. Exit Status {os.WEXITSTATUS(status)}")
            if os.WEXITSTATUS(status) != 0:
                new_child_pid = create_child()
                if new_child_pid is not None:
                    children.append(new_child_pid)
            children.remove(terminated_pid)