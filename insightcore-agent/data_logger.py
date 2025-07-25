import csv
import os
from datetime import datetime

# Automatically get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "user_behavior_log.csv")

def log_task(task_name, status):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [timestamp, task_name, status]

    file_exists = os.path.isfile(file_path)

    try:
        with open(file_path, mode="a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["timestamp", "task_name", "status"])
            writer.writerow(row)
        print(f"Logged: {row}")
    except Exception as e:
        print("Error while logging:", e)

# Sample usage
if __name__ == "__main__":
    print("Enter task details:")
    task = input("Task name: ")
    status = input("Status (completed/skipped/repeated): ")
    log_task(task, status)
