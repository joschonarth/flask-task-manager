from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models.task import Task

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class TaskModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), default="")
    completed = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }

with app.app_context():
    db.create_all()

@app.route("/tasks", methods=['POST'])
def create_task():
    data = request.get_json()
    
    if 'title' not in data or not data['title']:
        return jsonify({"message": "O campo 'title' é obrigatório."}), 400

    new_task = TaskModel(title=data['title'], description=data.get("description", ""))
    
    try:
        db.session.add(new_task)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Erro ao criar nova tarefa.", "error": str(e)}), 500

    return jsonify({"message": "Nova tarefa criada com sucesso", "id": new_task.id}), 201


@app.route("/tasks", methods=['GET'])
def get_tasks():
    tasks = TaskModel.query.all()
    task_list = [task.to_dict() for task in tasks]
    return jsonify({"tasks": task_list, "total_tasks": len(task_list)}), 200


@app.route("/tasks/<int:id>", methods=['GET'])
def get_task(id):
    task = TaskModel.query.get(id)
    if task:
        return jsonify(task.to_dict()), 200
    return jsonify({"message": "Tarefa não encontrada"}), 404


@app.route("/tasks/<int:id>", methods=['PUT'])
def update_task(id):
    task = TaskModel.query.get(id)
    if not task:
        return jsonify({"message": "Tarefa não encontrada"}), 404

    data = request.get_json()
    
    if 'title' not in data or not data['title']:
        return jsonify({"message": "O campo 'title' é obrigatório."}), 400

    task.title = data['title']
    task.description = data.get('description', task.description)
    task.completed = data.get('completed', task.completed)

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Erro ao atualizar a tarefa.", "error": str(e)}), 500
    
    return jsonify({"message": "Tarefa atualizada com sucesso"}), 200


@app.route("/tasks/<int:id>", methods=['DELETE'])
def delete_task(id):
    task = TaskModel.query.get(id)
    if not task:
        return jsonify({"message": "Tarefa não encontrada"}), 404

    try:
        db.session.delete(task)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Erro ao deletar a tarefa.", "error": str(e)}), 500

    return jsonify({"message": f"Tarefa '{task.title}' deletada com sucesso"}), 200


@app.route("/tasks/<int:id>/complete", methods=['PATCH'])
def complete_task(id):
    task = TaskModel.query.get(id)
    if not task:
        return jsonify({"message": "Tarefa não encontrada"}), 404

    task.completed = not task.completed

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Erro ao atualizar a tarefa.", "error": str(e)}), 500
    
    return jsonify({"message": f"Tarefa '{task.title}' marcada como {'concluída' if task.completed else 'não concluída'}"}), 200


if __name__ == "__main__":
    app.run(debug=True)
