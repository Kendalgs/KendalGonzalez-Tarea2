document.getElementById('taskForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const description = document.getElementById('description').value;

    fetch('http://localhost:5000/tasks', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ description })
    })
    .then(response => response.json())
    .then(task => {
        addTaskToList(task);
        document.getElementById('description').value = '';
    })
    .catch(error => console.error('Error:', error));
});

function fetchTasks() {
    fetch('http://localhost:5000/tasks')
    .then(response => response.json())
    .then(tasks => {
        tasks.forEach(task => addTaskToList(task));
    })
    .catch(error => console.error('Error:', error));
}

function addTaskToList(task) {
    const taskList = document.getElementById('taskList');
    const li = document.createElement('li');
    li.innerHTML = `
        <span>${task.id}: ${task.description}</span>
        <div class="buttons">
            <button class="modify" onclick="modifyTask(${task.id}, '${task.description}', this)">M</button>
            <button class="delete" onclick="deleteTask(${task.id}, this)">X</button>
        </div>
    `;
    taskList.appendChild(li);
}

function deleteTask(taskId, buttonElement) {
    fetch(`http://localhost:5000/tasks/${taskId}`, {
        method: 'DELETE'
    })
    .then(() => {
        const li = buttonElement.parentElement.parentElement;
        li.remove();
    })
    .catch(error => console.error('Error:', error));
}

function modifyTask(taskId, currentDescription, buttonElement) {
    const newDescription = prompt("Ingrese la nueva descripción:", currentDescription);
    if (newDescription && newDescription !== currentDescription) {
        fetch(`http://localhost:5000/tasks/${taskId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ description: newDescription })
        })
        .then(response => response.json())
        .then(updatedTask => {
            const li = buttonElement.parentElement.parentElement;
            li.querySelector('span').textContent = `${updatedTask.id}: ${updatedTask.description}`;
        })
        .catch(error => console.error('Error:', error));
    }
}

window.onload = fetchTasks;
