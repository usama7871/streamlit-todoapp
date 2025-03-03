import os
import json
from task_manager import Task

USER_FILE = "users.json"

def load_users():
    """Load users from the JSON file."""
    if not os.path.exists(USER_FILE):
        return {"users": {}}
    with open(USER_FILE, "r") as file:
        return json.load(file)

def save_users(users):
    """Save users to the JSON file."""
    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)  # Pretty print JSON

def add_user(username):
    """Add a new user if they don't already exist."""
    users = load_users()
    if username not in users["users"]:
        users["users"][username] = []
        save_users(users)

def get_user_tasks(username):
    """Retrieve tasks for a specific user."""
    users = load_users()
    user_tasks = users["users"].get(username, [])
    return [Task(task["description"], task["done"], task["priority"]) for task in user_tasks]

def save_user_tasks(username, tasks):
    """Save tasks for a specific user."""
    users = load_users()
    users["users"][username] = [task.to_dict() for task in tasks]
    save_users(users) 