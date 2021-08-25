from flask import Blueprint, jsonify

user = Blueprint('user', __name__, url_prefix='/api')


@user.route('/', methods=['GET'])
def test():
    return jsonify({'code': 200, 'msg': 'OK'})
