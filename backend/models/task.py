class Task:
    def __init__(self, task_id, description):
        self.task_id = task_id
        self.description = description

    def serialize(self):
        return {
            'id': self.task_id,
            'description': self.description
        }
