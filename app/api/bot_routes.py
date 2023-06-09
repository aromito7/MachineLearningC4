from flask import Blueprint, jsonify, session, request
from app.models import User, db
from flask_login import current_user, login_user, logout_user, login_required
from app.c4 import Board
import numpy as np

bot_routes = Blueprint('bot', __name__)



@bot_routes.route('/ai/decide', methods=['POST'])
def authenticate():
    """
    Authenticates a user.
    """
    json = request.get_json()

    board = Board(json['board'], json['active'])

    print(board.rows)
    return {'message' : 'successful request',
            'numpy': repr(board.rows)}
