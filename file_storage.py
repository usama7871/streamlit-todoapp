import os
from task_manager import Task

TASKS_FILE = "tasks.txt"

def save_tasks(tasks):
    """Save tasks to a plain text file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task.done}|{task.description}|{task.priority}\n")  # Save priority

def load_tasks():
    """Load tasks from the plain text file."""
    if not os.path.exists(TASKS_FILE):
        return []
    
    tasks = []
    with open(TASKS_FILE, "r") as file:
        for line in file:
            try:
                done, description, priority = line.strip().split("|", 2)  # Split into three parts
                tasks.append(Task(description, done == "True", priority))
            except ValueError:
                print(f"Skipping invalid line: {line.strip()}")  # Log invalid lines
    return tasks
