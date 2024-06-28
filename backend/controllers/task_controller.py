from flask import Blueprint, request
from services.task_service import TaskService
from views.task_view import TaskView

tasks_blueprint = Blueprint('tasks', __name__)
task_service = TaskService()

@tasks_blueprint.route('', methods=['POST'])
def add_task():
    data = request.json
    description = data.get('description')

    if not description:
        return TaskView.error('Missing task description', 400)

    task = task_service.create_task(description)
    return TaskView.render(task, 201)


@tasks_blueprint.route('/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    description = data.get('description')

    if not description:
        return TaskView.error('Missing task description', 400)

    if task_service.update_task(task_id, description):
        updated_task = task_service.get_task(task_id)
        return TaskView.render(updated_task, 200)
    else:
        return TaskView.error('Task not found', 404)



@tasks_blueprint.route('', methods=['GET'])
def get_tasks():
    tasks = task_service.get_all_tasks()
    return TaskView.render_many(tasks, 200)


@tasks_blueprint.route('/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_service.delete_task(task_id):
        return '', 204
    else:
        return TaskView.error('Task not found', 404)