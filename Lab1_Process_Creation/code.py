import os
import time

def task1_process_creation(n):
    print(f"Parent PID: {os.getpid()}")
    for i in range(n):
        pid = os.fork()
        if pid == 0:
            # Child process
            print(f"Child {i+1}: PID={os.getpid()}, Parent PID={os.getppid()}")
            print(f"Child {i+1} says: Hello, I am a child process!")
            os._exit(0)
        else:
            # Parent waits for child
            os.wait()

if __name__ == "__main__":
    task1_process_creation(3)
