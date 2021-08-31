from utils.util import make_password
from server_src.models import Department, Menu, User
from flask import Blueprint, jsonify, request
from config import status_code
from config.global_params import db
import json
from datetime import datetime

apis = Blueprint('apis', __name__, url_prefix='/api')


@apis.route('/user/list/', methods=['GET'])
def api_user_list():
    data = request.args
    page = int(data.get('page', 1) or 1)
    page_size = int(data.get('pageSize', 10) or 10)
    user_list = User.query

    name = data.get('name')
    department_id = data.get('department_id')
    status = json.loads(data.get('status', '[]') or '[]')
    gender = data.get('gender')
    start_time = data.get('start_time')
    end_time = data.get('end_time')

    if name:
        user_list = user_list.filter_by(name=name)
    if status:
        user_list = user_list.filter(User.status.in_(status))
    if gender is not None:
        user_list = user_list.filter_by(gender=gender)
    if department_id:
        user_list = user_list.filter_by(department_id=int(department_id))
    if start_time and end_time:
        user_list = user_list.filter(
            User.create_time >= datetime.strptime(start_time, "%Y-%m-%d"),
            User.create_time <= datetime.strptime(end_time, "%Y-%m-%d"),
        )
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
        password = make_password(data.get('password', 'password'))
        user.position = data.get('position')
        user.office = data.get('office')
        user.salary = data.get('salary', 0)
        user.gender = data.get('gender', '男')
        user.status = data.get('status')
        user.department_id = data.get('department_id', 1)

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
        if password:
            password = make_password(password)
        position = data.get('position')
        office = data.get('office')
        salary = data.get('salary')
        status = data.get('status')
        gender = data.get('gender')
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
        if gender is not None:
            user.gender = gender
        if department_id:
            user.department_id = department_id

        db.session.commit()
        return jsonify({'code': status_code.OK})
    elif request.method == 'DELETE':
        data = request.get_json()
        user_id = data.get('id')

        user = User.query.filter_by(id=user_id).first()
        db.session.delete(user)
        db.session.commit()
        return jsonify({'code': status_code.OK})


@apis.route('/menu/list/', methods=['GET'])
def api_menu_list():
    menu_list = Menu.query.order_by(Menu.level).all()

    resp = {}
    menus = {}
    for menu in menu_list:
        menus[menu.id] = menu
        if menu.level == 0:
            resp[menu.name] = []
        elif menu.level == 1:
            resp[menus[menu.parent].name].append(menu.name)
    return jsonify({'code': status_code.OK, 'data': resp})


@apis.route('/user/login/', methods=['POST'])
def api_user_login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'code': status_code.USER_NOT_EXIST, 'msg': '用户不存在'})

    if make_password(password) != user.password:
        return jsonify({'code': status_code.USER_WRONG_PASSWORD, 'msg': '密码错误'})

    return jsonify({'code': status_code.OK, 'data': dict(user)})


@apis.route('/department/list/', methods=['GET'])
def api_department_list():
    dp_list = Department.query.all()

    resp = [dict(dp) for dp in dp_list]
    return jsonify({'code': status_code.OK, 'data': resp})


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
