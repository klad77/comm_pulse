from flask import Blueprint, request


questions_bp = Blueprint('questions', __name__, url_prefix='/questions')


@questions_bp.route('/', methods=['GET'])
def get_questions():
    return "Список всех вопросов"


@questions_bp.route('/', methods=['POST'])
def create_question():
    return "Вопрос создан"


@questions_bp.route('/<int:question_id>', methods=['GET'])
def get_question(question_id):
    return f"Детали вопроса {question_id}"


@questions_bp.route('/<int:question_id>', methods=['PUT'])
def update_question(question_id):
    return f"Вопрос {question_id} обновлен"


@questions_bp.route('/<int:question_id>', methods=['DELETE'])
def delete_question(question_id):
    return f"Вопрос {question_id} удален"
