from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory storage for tasks
tasks = [
    {"id": 1, "title": "Buy groceries", "completed": False},
    {"id": 2, "title": "Walk the dog", "completed": True},
    {"id": 3, "title": "Learn Flask", "completed": False}
]

# Counter for generating new IDs
next_id = 4


@app.route('/')
def home():
    return jsonify({
        "message": "Task Manager API",
        "endpoints": {
            "GET /tasks": "Get all tasks",
            "GET /tasks/:id": "Get a single task",
            "POST /tasks": "Create a new task",
            "PATCH /tasks/:id": "Update a task",
            "DELETE /tasks/:id": "Delete a task"
        }
    })


@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    return jsonify(tasks), 200


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Get a single task by ID"""
    task = next((task for task in tasks if task['id'] == task_id), None)
    
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    
    return jsonify(task), 200


@app.route('/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    global next_id
    
    # Check if request has JSON data
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 400
    
    data = request.get_json()
    
    # Validate title field
    if 'title' not in data:
        return jsonify({"error": "Field 'title' is required"}), 400
    
    title = data.get('title', '').strip()
    
    if not title:
        return jsonify({"error": "Field 'title' cannot be empty"}), 400
    
    # Create new task
    new_task = {
        "id": next_id,
        "title": title,
        "completed": False
    }
    
    tasks.append(new_task)
    next_id += 1
    
    return jsonify(new_task), 201


@app.route('/tasks/<int:task_id>', methods=['PATCH'])
def update_task(task_id):
    """Update a task"""
    task = next((task for task in tasks if task['id'] == task_id), None)
    
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    
    # Check if request has JSON data
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 400
    
    data = request.get_json()
    
    # Update fields if provided
    if 'title' in data:
        title = data['title'].strip()
        if not title:
            return jsonify({"error": "Field 'title' cannot be empty"}), 400
        task['title'] = title
    
    if 'completed' in data:
        if not isinstance(data['completed'], bool):
            return jsonify({"error": "Field 'completed' must be a boolean"}), 400
        task['completed'] = data['completed']
    
    return jsonify(task), 200


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task"""
    global tasks
    
    task = next((task for task in tasks if task['id'] == task_id), None)
    
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    
    tasks = [task for task in tasks if task['id'] != task_id]
    
    return '', 204


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"error": "Method not allowed"}), 405


@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
