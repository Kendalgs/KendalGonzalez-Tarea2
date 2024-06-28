from models.task import Task

class TaskService:
    def __init__(self):
        self.tasks = []
        self.next_task_id = 1

    def create_task(self, description):
        task = Task(self.next_task_id, description)
        self.tasks.append(task)
        self.next_task_id += 1
        return task

    def get_all_tasks(self):
        return self.tasks

    def get_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def update_task(self, task_id, description):
        task = self.get_task(task_id)
        if task:
            task.description = description
            return True
        return False

    def delete_task(self, task_id):
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False