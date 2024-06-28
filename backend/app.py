from flask import Flask
from flask_cors import CORS
from controllers.task_controller import tasks_blueprint

app = Flask(__name__)
CORS(app)

# Registrar el blueprint de tareas
app.register_blueprint(tasks_blueprint, url_prefix='/tasks')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
