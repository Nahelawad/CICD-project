from flask import Flask, jsonify, request, render_template, redirect, url_for

app = Flask(__name__)
tasks = []


@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        tasks.append({"title": task})
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if data:
        tasks.append(data)
        return jsonify({"message": "Task added!"}), 201
    return jsonify({"error": "Invalid data"}), 400
if __name__ == '__main__':
    app.run(debug=True)