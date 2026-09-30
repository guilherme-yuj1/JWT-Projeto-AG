from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from controllers.user_controller import UserController

user_bp = Blueprint('users', __name__)


def _response(result):
    body, status = result
    return jsonify(body), status


@user_bp.route('/register', methods=['POST'])
def register():
    return _response(UserController.register_user(request.get_json(silent=True) or {}))


@user_bp.route('/login', methods=['POST'])
def login():
    return _response(UserController.login_user(request.get_json(silent=True) or {}))


@user_bp.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    return _response(UserController.get_user(user_id))


@user_bp.route('/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    return _response(UserController.update_user(
        user_id,
        request.get_json(silent=True) or {}
    ))


@user_bp.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    return _response(UserController.delete_user(user_id))
