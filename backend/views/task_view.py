from flask import jsonify

class TaskView:
    @staticmethod
    def render(task, status_code=200):
        return jsonify(task.serialize()), status_code

    @staticmethod
    def render_many(tasks, status_code=200):
        return jsonify([task.serialize() for task in tasks]), status_code

    @staticmethod
    def error(message, status_code):
        return jsonify({'error': message}), status_code
