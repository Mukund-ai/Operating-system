# ------------------------------------------------------------
# Program Name: System Startup, Process Creation, and Termination Simulation
# Course Code: ENCS351 - Operating System
# Program: B.Tech CSE / AI / ML / Data Science / Cyber / FSD / UX/UI
# ------------------------------------------------------------

# Import required libraries
import multiprocessing
import time
import logging

# ------------------------------------------------------------
# Sub-Task 1: Initialize the Logging Configuration
# ------------------------------------------------------------
logging.basicConfig(
    filename='process_log.txt',          # Log file name
    level=logging.INFO,                  # Log only INFO-level messages
    format='%(asctime)s - %(processName)s - %(message)s'  # Log format
)

# ------------------------------------------------------------
# Sub-Task 2: Define a Function that Simulates a Process Task
# ------------------------------------------------------------
def system_process(task_name):
    """
    Function that simulates a simple system process.
    It logs when the process starts and ends.
    """
    logging.info(f"{task_name} started")
    time.sleep(2)  # Simulate process execution delay
    logging.info(f"{task_name} ended")

# ------------------------------------------------------------
# Sub-Task 3 & 4: Create, Start, and Join Multiple Processes
# ------------------------------------------------------------
if __name__ == '__main__':
    print("System Starting...")

    # Create two separate processes
    p1 = multiprocessing.Process(target=system_process, args=('Process-1',))
    p2 = multiprocessing.Process(target=system_process, args=('Process-2',))

    # Start both processes
    p1.start()
    p2.start()

    # Wait for both to finish
    p1.join()
    p2.join()

    print("System Shutdown.")
