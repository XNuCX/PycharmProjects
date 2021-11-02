from .task import Task

class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        else:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        if task_name not in [name_1.name for name_1 in self.tasks]:
            return f"Could not find task with the name {task_name}"
        else:
            for i, task in enumerate(self.tasks):
                if task_name == task.name:
                    self.tasks[i].completed = True
                    return f"Completed task {task_name}"

    def clean_section(self):
        total_tasks = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task.completed]
        return f"Cleared {total_tasks - len(self.tasks)} tasks."

    def view_section(self):
        section_details = '\n'.join([task.details() for task in self.tasks])
        return f"Section {self.name}:\n{section_details}"




