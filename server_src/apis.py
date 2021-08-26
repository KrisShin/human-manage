from server_src.models import User
from flask import Blueprint, jsonify, request
from config import status_code

apis = Blueprint('apis', __name__, url_prefix='/api')


# @user.route('/', methods=['GET'])
# def test():
#     return jsonify({'code': 200, 'msg': 'OK'})


@apis.route('/user/list/', methods=['GET'])
def users_list():
    data = request.args
    page = int(data.get('page', 1) or 1)
    page_size = int(data.get('pageSize', 10) or 10)
    user_list = User.query
    total = user_list.count()
    user_list = [dict(user) for user in user_list.paginate(page, page_size).items]
    return jsonify(
        {
            'code': status_code.OK,
            'data': user_list,
            'page': page,
            'pageSize': page_size,
            'total': total,
        }
    )


@apis.route('/user/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def user_options():
    if request.method == 'GET':
        data = request.args
        user_id = data.get('id')
        user = User.query.filter_by(id=user_id).first()
        return jsonify({'code': status_code.OK, 'data': dict(user)})
