
# ---------------- PRIORITY SCHEDULING ----------------

# Input number of processes
n = int(input("Enter number of processes: "))

# List to store (PID, Burst Time, Priority)
processes = []

for i in range(n):
    bt = int(input(f"Enter Burst Time for P{i+1}: "))
    pr = int(input(f"Enter Priority (lower number = higher priority) for P{i+1}: "))
    processes.append((i+1, bt, pr))

# Sorting by priority
processes.sort(key=lambda x: x[2])

wt = 0
total_wt = 0
total_tat = 0

print("\nPriority Scheduling:")
print("PID\tBT\tPriority\tWT\tTAT")

for pid, bt, priority in processes:
    tat = wt + bt
    print(f"{pid}\t{bt}\t{priority}\t\t{wt}\t{tat}")
    total_wt += wt
    total_tat += tat
    wt += bt

print(f"Average Waiting Time: {total_wt / n}")
print(f"Average Turnaround Time: {total_tat / n}")

# ---------------- ROUND ROBIN SCHEDULING ----------------

processes = []
n = int(input("Enter number of processes: "))

for i in range(n):
    bt = int(input(f"Enter Burst Time for P{i+1}: "))
    processes.append([i+1, bt])

quantum = int(input("Enter Time Quantum: "))

remaining = [bt for _, bt in processes]
wt = [0] * n
tat = [0] * n
time = 0

while True:
    done = True
    for i in range(n):
        if remaining[i] > 0:
            done = False  # process still left
            if remaining[i] > quantum:
                time += quantum
                remaining[i] -= quantum
            else:
                time += remaining[i]
                wt[i] = time - processes[i][1]
                remaining[i] = 0
    if done:
        break

for i in range(n):
    tat[i] = wt[i] + processes[i][1]

print("\nRound Robin Scheduling:")
print("PID\tBT\tWT\tTAT")
for i in range(n):
    print(f"P{i+1}\t{processes[i][1]}\t{wt[i]}\t{tat[i]}")

print(f"Average Waiting Time: {sum(wt)/n}")
print(f"Average Turnaround Time: {sum(tat)/n}")


# ---------------- SEQUENTIAL FILE ALLOCATION ----------------

total_blocks = int(input("Enter total number of blocks: "))
block_status = [0] * total_blocks  # 0 = free, 1 = allocated

n = int(input("Enter number of files: "))

for i in range(n):
    start = int(input(f"Enter starting block for File {i+1}: "))
    length = int(input(f"Enter length of File {i+1}: "))

    allocated = True
    for j in range(start, start + length):
        if j >= total_blocks or block_status[j] == 1:
            allocated = False
            break

    if allocated:
        for j in range(start, start + length):
            block_status[j] = 1
        print(f"File {i+1} allocated from block {start} to {start + length - 1}")
    else:
        print(f"File {i+1} cannot be allocated.")


