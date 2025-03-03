class Task:
    def __init__(self, description: str, done: bool = False, priority: str = "Medium"):
        self.description = description
        self.done = done
        self.priority = priority

    def mark_complete(self):
        self.done = True

    def to_dict(self):  # New method to convert Task to a dictionary
        return {
            "description": self.description,
            "done": self.done,
            "priority": self.priority
        }

    def __str__(self):
        return f"[{'✓' if self.done else '✗'}] {self.description} (Priority: {self.priority})"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_desc: str, priority: str = "Medium"):
        task = Task(task_desc, priority=priority)
        self.tasks.append(task)

    def list_tasks(self):
        return self.tasks

    def complete_task(self, task_index: int):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_complete()

    def remove_task(self, task_index: int):
        if 0 <= task_index < len(self.tasks):
            self.tasks.pop(task_index)