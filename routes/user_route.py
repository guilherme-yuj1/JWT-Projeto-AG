from flask import Blueprint, request, jsonify
from controllers.user_controller import UserController

user_bp = Blueprint('users', __name__)


@user_routes.route('/register', methods=['POST'])
def register():
    return jsonify(UserController.register_user(request.get_json))

@user_routes.route('/login', methods=['POST'])
def login():
    return jsonify(UserController.login_user(request.get_json))


@user_bp.route('/User', methods=['GET'])
def users_get():
    return get_users()


@user_routes.route('/User/<int:user_id>', methods=['GET'])
def user_get_by_id(user_id):
    return user_by_id(user_id)


@user_routes.route('/User/<int:user_id>', methods=['PUT'])
def users_put(user_id):
    return update_user(user_id, request.json)


@user_routes.route('/User/<int:user_id>', methods=['DELETE'])
def users_delete(user_id):
    return delete_user(user_id)


