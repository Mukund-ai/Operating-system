import os
import time
import subprocess

# ----------------------------
# Task 1: Process Creation Utility
# ----------------------------
def task1_process_creation(n):
    print("\n=== Task 1: Process Creation ===")
    print(f"Parent PID: {os.getpid()}")
    for i in range(n):
        pid = os.fork()
        if pid == 0:
            # Child process
            print(f"Child {i+1}: PID={os.getpid()}, Parent PID={os.getppid()}")
            print(f"Child {i+1} says: Hello, I am a child process!")
            os._exit(0)
        else:
            os.wait()


# ----------------------------
# Task 2: Command Execution Using exec()
# ----------------------------
def task2_exec_commands():
    print("\n=== Task 2: Command Execution Using exec() ===")
    commands = [["ls"], ["date"], ["whoami"]]
    print(f"Parent PID: {os.getpid()}")
    for cmd in commands:
        pid = os.fork()
        if pid == 0:
            print(f"Executing command: {' '.join(cmd)}")
            os.execvp(cmd[0], cmd)
        else:
            os.wait()


# ----------------------------
# Task 3: Zombie & Orphan Processes
# ----------------------------
def task3_zombie_orphan():
    print("\n=== Task 3: Zombie & Orphan Processes ===")

    # Zombie process demo
    print("\n--- Zombie Process Demo ---")
    pid = os.fork()
    if pid > 0:
        print(f"Parent PID: {os.getpid()}, Child PID: {pid}")
        print("Parent not waiting, child becomes zombie for a short time...")
        time.sleep(10)
    else:
        print(f"Child PID: {os.getpid()} exiting quickly.")
        os._exit(0)

    # Orphan process demo
    print("\n--- Orphan Process Demo ---")
    pid2 = os.fork()
    if pid2 > 0:
        print(f"Parent PID: {os.getpid()} exiting before child finishes.")
        os._exit(0)
    else:
        time.sleep(5)
        print(f"Child (orphan) PID: {os.getpid()}, New Parent: {os.getppid()}")


# ----------------------------
# Task 4: Inspecting Process Info from /proc
# ----------------------------
def task4_inspect_proc(pid):
    print("\n=== Task 4: Inspecting Process Info from /proc ===")
    try:
        with open(f"/proc/{pid}/status", "r") as f:
            lines = f.readlines()
            print("\nProcess Status Info:")
            for line in lines[:10]:
                print(line.strip())

        exe_path = os.readlink(f"/proc/{pid}/exe")
        print(f"\nExecutable Path: {exe_path}")

        fds = os.listdir(f"/proc/{pid}/fd")
        print(f"Open File Descriptors: {fds}")

    except FileNotFoundError:
        print("Invalid PID or process not running.")


# ----------------------------
# Task 5: Process Prioritization
# ----------------------------
def task5_priority_demo():
    print("\n=== Task 5: Process Prioritization ===")
    print("Parent PID:", os.getpid())
    for i in range(3):
        pid = os.fork()
        if pid == 0:
            os.nice(i * 5)
            print(f"Child {i+1} (PID={os.getpid()}) running with nice value {i*5}")
            for _ in range(10000000):
                pass
            print(f"Child {i+1} completed.")
            os._exit(0)
        else:
            os.wait()


# ----------------------------
# Main Menu
# ----------------------------
if __name__ == "__main__":
    print("=== Operating System Lab Experiment 1 ===")
    print("Process Creation and Management using Python OS Module\n")

    print("1. Task 1 - Process Creation")
    print("2. Task 2 - Command Execution")
    print("3. Task 3 - Zombie & Orphan Process")
    print("4. Task 4 - Inspect Process Info")
    print("5. Task 5 - Process Prioritization")

    choice = input("\nEnter task number to run (1-5): ")

    if choice == '1':
        task1_process_creation(3)
    elif choice == '2':
        task2_exec_commands()
    elif choice == '3':
        task3_zombie_orphan()
    elif choice == '4':
        pid = input("Enter PID to inspect: ")
        task4_inspect_proc(pid)
    elif choice == '5':
        task5_priority_demo()
    else:
        print("Invalid choice!")
