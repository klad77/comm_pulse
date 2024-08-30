from flask import Blueprint, request

response_bp = Blueprint('responses', __name__, url_prefix='/responses')


@response_bp.route('/', methods=['GET'])
def get_responses():
    return "Статистика всех ответов"


@response_bp.route('/', methods=['POST'])
def add_response():
    return "Ответ добавлен"
