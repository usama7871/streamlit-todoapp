import streamlit as st
from task_manager import TaskManager
from user_manager import add_user, get_user_tasks, save_user_tasks
from file_storage import load_tasks, save_tasks
from datetime import datetime

# User Login
username = st.text_input("Enter your username:")
if st.button("Login"):
    add_user(username)
    st.success(f"Welcome, {username}!")

# Initialize Task Manager and Load User Tasks
task_manager = TaskManager()
task_manager.tasks = get_user_tasks(username)

st.title("📌 Daily Task Manager")

# Date Picker for Task Management
selected_date = st.date_input("Select Date", datetime.today())

# Add New Task
new_task = st.text_input("Enter a new task:")
priority = st.selectbox("Select Priority", ["High", "Medium", "Low"])
if st.button("Add Task"):
    if new_task:
        task_manager.add_task(f"{selected_date} - {new_task}", priority=priority)
        save_user_tasks(username, task_manager.tasks)
        st.success("Task added successfully!")

# Show Existing Tasks for Selected Date
st.subheader(f"Tasks for {selected_date}")
tasks_for_date = [task for task in task_manager.list_tasks() if task.description.startswith(str(selected_date))]
if not tasks_for_date:
    st.info("No tasks found for this date!")
else:
    for index, task in enumerate(tasks_for_date):
        col1, col2, col3 = st.columns([3, 2, 1])
        col1.text(task.description)
        col2.text(f"Priority: {task.priority}")
        col3.checkbox("Done", value=task.done, key=f"done_{index}", on_change=lambda i=index: complete_task(tasks_for_date[i]))

        # Button to remove task
        col3.button("❌", key=f"remove_{index}", on_click=lambda i=index: remove_task(tasks_for_date[i]))

# Mark Task as Completed
def complete_task(task):
    task.done = True
    save_user_tasks(username, task_manager.tasks)
    st.success("Task marked as completed!")

# Remove Task
def remove_task(task):
    task_manager.tasks.remove(task)
    save_user_tasks(username, task_manager.tasks)
    st.success("Task removed successfully!")
