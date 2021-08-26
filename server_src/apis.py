from server_src.models import Menu, User
from flask import Blueprint, jsonify, request
from config import status_code
from config.global_params import db

apis = Blueprint('apis', __name__, url_prefix='/api')


# @user.route('/', methods=['GET'])
# def test():
#     return jsonify({'code': 200, 'msg': 'OK'})


@apis.route('/user/list/', methods=['GET'])
def api_user_list():
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
def api_user_options():
    if request.method == 'GET':
        data = request.args
        user_id = data.get('id')
        user = User.query.filter_by(id=user_id).first()
        return jsonify({'code': status_code.OK, 'data': dict(user)})
    elif request.method == 'POST':
        data = request.get_json()

        user = User()
        user.name = data.get('name')
        user.email = data.get('email')
        user.password = "password"
        user.position = data.get('position')
        user.office = data.get('office')
        user.salary = data.get('salary')
        user.status = data.get('status')
        user.department_id = data.get('department_id')

        db.session.add(user)
        db.session.commit()
        return jsonify({'code': status_code.OK, 'data': dict(user)})
    elif request.method == 'PUT':
        data = request.get_json()
        user_id = data.get('id')

        user = User.query.filter_by(id=user_id).first()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        position = data.get('position')
        office = data.get('office')
        salary = data.get('salary')
        status = data.get('status')
        department_id = data.get('department_id')

        if name:
            user.name = name
        if email:
            user.email = email
        if password:
            user.password = password
        if position:
            user.position = position
        if office:
            user.office = office
        if salary:
            user.salary = salary
        if status:
            user.status = status
        if department_id:
            user.department_id = department_id

        db.session.commit()
        return jsonify({'code': status_code.OK})
    elif request.method == 'DELETE':
        data = request.get_json()
        user_id = data.get('id')

        user = User.query.filter_by(id=user_id).first()
        user.delete()

        db.session.commit()
        return jsonify({'code': status_code.OK})


@apis.route('/menu/list/', methods=['GET'])
def api_menu_list():
    menu_list = Menu.query.all()
    menu_list = [dict(menu) for menu in menu_list]
    return jsonify({'code': status_code.OK, 'data': menu_list})


@apis.route('/user/login/', methods=['POST'])
def api_user_login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'code': status_code.USER_NOT_EXIST, 'msg': '用户不存在'})

    if password != user.password:
        return jsonify({'code': status_code.USER_WRONG_PASSWORD, 'msg': '密码错误'})

    return jsonify({'code': status_code.OK, 'data': dict(user)})


@apis.route('/user/mock/', methods=['GET'])
def mock_users():
    import random
    import string

    for _ in range(10):
        user = User()
        user.name = ''.join(
            random.choices(string.ascii_letters, k=random.randint(5, 10))
        )
        user.email = (
            ''.join(random.choices(string.ascii_letters, k=random.randint(5, 10)))
            + '@'
            + ''.join(random.choices(string.ascii_letters, k=random.randint(5, 10)))
            + '.com'
        )
        user.password = "password"
        user.position = ''.join(
            random.choices(string.ascii_letters, k=random.randint(5, 10))
        )
        user.office = ''.join(
            random.choices(string.ascii_letters, k=random.randint(5, 10))
        )
        user.salary = random.randint(2000, 200000)
        user.status = ''.join(
            random.choices(string.ascii_letters, k=random.randint(5, 10))
        )
        user.department_id = random.choice((1, 2, 3, 4, 5, 6, 7, 8))

        db.session.add(user)
        db.session.commit()
    return jsonify({'code': status_code.OK})
