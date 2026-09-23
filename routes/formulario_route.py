from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.formulario_controller import FormularioController

formulario_bp = Blueprint('formularios', __name__)

@formulario_bp.route('/', methods=['POST'])
@jwt_required()
def create_formulario():
    user_id = get_jwt_identity
    return jsonify(FormularioController.create_formulario(user_id, request.get_json()))


@formulario_bp.route('/<int:formulario_id', methods=['PUT'])
@jwt_required()
def update_formulario(formulario_id):
    user_id = get_jwt_identity()
    return jsonify(FormularioController.update_formulario(user_id, formulario_id, request.get.json()))


@formulario_bp.route('/<int:formulario_id>', methods=[DELETE])
@jwt_required()
def delete_formulario(formulario_id):
    user_id = get_jwt_identity
    return jsonify(FormularioController.delete_formulario(user_id, formulario_id))