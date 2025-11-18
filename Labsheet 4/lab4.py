# =====================================================================
#          OS LAB ASSIGNMENT 4 - COMPLETE PYTHON IMPLEMENTATION
# =====================================================================

import subprocess
import multiprocessing
import logging
import time
import os
import platform

# =====================================================================
# TASK 1: BATCH PROCESSING SIMULATION
# =====================================================================

def batch_processing():
    print("\n=========== BATCH PROCESSING EXECUTION ===========")

    scripts = ['script1.py', 'script2.py', 'script3.py']

    for script in scripts:
        print(f"\nExecuting {script}...")
        subprocess.call(['python3', script])


# =====================================================================
# TASK 2: SYSTEM STARTUP + PROCESS LOGGING
# =====================================================================

def process_task(name):
    logging.info(f"{name} started")
    time.sleep(2)
    logging.info(f"{name} terminated")

def system_startup():
    print("\n=========== SYSTEM STARTUP SIMULATION ===========")

    logging.basicConfig(
        filename='system_log.txt',
        level=logging.INFO,
        format='%(asctime)s - %(processName)s - %(message)s'
    )

    print("System Booting...")

    p1 = multiprocessing.Process(target=process_task, args=("Process-1",))
    p2 = multiprocessing.Process(target=process_task, args=("Process-2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("System Shutdown.")
    print("Log saved to system_log.txt")


# =====================================================================
# TASK 3: SYSTEM CALLS (fork, exec, pipe)
# =====================================================================

def system_calls_ipc():
    print("\n=========== SYSTEM CALLS (FORK + PIPE) ===========")

    r, w = os.pipe()
    pid = os.fork()

    if pid > 0:
        # Parent process
        os.close(r)
        os.write(w, b"Hello from Parent Process")
        os.close(w)
        os.wait()
    else:
        # Child process
        os.close(w)
        msg = os.read(r, 1024)
        print("Child received:", msg.decode())
        os.close(r)
        os._exit(0)


# =====================================================================
# TASK 4: VM DETECTION (Python Script)
# =====================================================================

def detect_vm():
    print("\n=========== VM DETECTION ===========")

    print("Machine:", platform.machine())
    print("Platform:", platform.platform())

    # Check virtualization from dmesg output
    try:
        output = subprocess.check_output("dmesg | grep -i virtual", shell=True).decode()
        if output:
            print("\nSystem is running inside a Virtual Machine.")
            print(output)
        else:
            print("\nNo virtualization detected.")
    except:
        print("\nPermission denied for dmesg. Running limited detection.")

    # Check CPU flags
    try:
        cpu = subprocess.check_output("lscpu | grep Virtualization", shell=True).decode()
        print(cpu)
    except:
        print("Cannot run lscpu check.")


# =====================================================================
# TASK 5: CPU SCHEDULING ALGORITHMS
# =====================================================================

def fcfs():
    print("\n=========== FCFS SCHEDULING ===========")
    n = int(input("Enter number of processes: "))
    bt = []
    for i in range(n):
        bt.append(int(input(f"Enter BT for P{i+1}: ")))

    wt = [0] * n
    tat = [0] * n

    for i in range(1, n):
        wt[i] = wt[i-1] + bt[i-1]

    for i in range(n):
        tat[i] = wt[i] + bt[i]

    print("PID\tBT\tWT\tTAT")
    for i in range(n):
        print(f"P{i+1}\t{bt[i]}\t{wt[i]}\t{tat[i]}")

def sjf():
    print("\n=========== SJF SCHEDULING ===========")
    n = int(input("Enter number of processes: "))
    processes = []

    for i in range(n):
        bt = int(input(f"Enter BT for P{i+1}: "))
        processes.append((i+1, bt))

    processes.sort(key=lambda x: x[1])

    wt = 0
    total_w = 0
    total_t = 0

    print("PID\tBT\tWT\tTAT")
    for pid, bt in processes:
        tat = wt + bt
        print(f"{pid}\t{bt}\t{wt}\t{tat}")
        total_w += wt
        total_t += tat
        wt += bt

def priority_sched():
    print("\n=========== PRIORITY SCHEDULING ===========")
    n = int(input("Enter number of processes: "))
    processes = []

    for i in range(n):
        bt = int(input(f"Enter BT for P{i+1}: "))
        pr = int(input(f"Enter Priority: "))
        processes.append((i+1, bt, pr))

    processes.sort(key=lambda x: x[2])

    wt = 0
    print("PID\tBT\tPR\tWT\tTAT")
    for pid, bt, pr in processes:
        tat = wt + bt
        print(f"{pid}\t{bt}\t{pr}\t{wt}\t{tat}")
        wt += bt

def round_robin():
    print("\n=========== ROUND ROBIN SCHEDULING ===========")
    n = int(input("Enter processes: "))
    bt = []
    for i in range(n):
        bt.append(int(input(f"BT for P{i+1}: ")))

    quantum = int(input("Enter quantum: "))
    rem = bt[:]
    wt = [0] * n
    tat = [0] * n

    t = 0
    while True:
        done = True
        for i in range(n):
            if rem[i] > 0:
                done = False
                if rem[i] > quantum:
                    t += quantum
                    rem[i] -= quantum
                else:
                    t += rem[i]
                    wt[i] = t - bt[i]
                    rem[i] = 0
        if done:
            break

    for i in range(n):
        tat[i] = wt[i] + bt[i]

    print("PID\tBT\tWT\tTAT")
    for i in range(n):
        print(f"P{i+1}\t{bt[i]}\t{wt[i]}\t{tat[i]}")


# =====================================================================
# MAIN MENU
# =====================================================================

while True:
    print("\n================ OS LAB 4 MENU ================")
    print("1. Batch Processing")
    print("2. System Startup Logging")
    print("3. System Calls (fork, pipe)")
    print("4. VM Detection")
    print("5. FCFS Scheduling")
    print("6. SJF Scheduling")
    print("7. Priority Scheduling")
    print("8. Round Robin Scheduling")
    print("0. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        batch_processing()
    elif ch == 2:
        system_startup()
    elif ch == 3:
        system_calls_ipc()
    elif ch == 4:
        detect_vm()
    elif ch == 5:
        fcfs()
    elif ch == 6:
        sjf()
    elif ch == 7:
        priority_sched()
    elif ch == 8:
        round_robin()
    elif ch == 0:
        break
    else:
        print("Invalid option!")
