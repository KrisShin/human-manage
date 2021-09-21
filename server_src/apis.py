from server_src.wraps import generate_token
from utils.util import check_password, make_password, get_parse_response
from server_src.models import Department, User, SystemCode
from flask import Blueprint, jsonify, request
from config import status_code
from config.global_params import db
from datetime import datetime

apis = Blueprint('apis', __name__, url_prefix='/api')


@apis.route('/user/role/list', methods=['GET'])
def api_user_role_list():
    items = SystemCode.query.filter(code_kbn='01').all()
    resp = get_parse_response(items)

    return jsonify({'code': status_code.OK, 'data': resp})


@apis.route('/user/duty/list', methods=['GET'])
def api_user_duty_list():
    items = SystemCode.query.filter(code_kbn='02').all()
    resp = get_parse_response(items)

    return jsonify({'code': status_code.OK, 'data': resp})


@apis.route('/user/abort/list', methods=['GET'])
def api_user_abort_list():
    items = SystemCode.query.filter(code_kbn='00').all()
    resp = get_parse_response(items)

    return jsonify({'code': status_code.OK, 'data': resp})


@apis.route('/user/list/', methods=['POST'])
def api_user_list():
    data = request.get_json()
    page = data.get('page', 1)
    page_size = data.get('pageSize', 10)
    user_list = User.query.order_by(User.create_time.desc())

    name = data.get('name')
    department_id = data.get('department_id')
    status = data.get('status')
    gender = data.get('gender')
    create_time = data.get('create_time')

    if name:
        user_list = user_list.filter(User.name.like(f"%{name}%"))
    if status:
        user_list = user_list.filter(User.status.in_(status))
    if gender is not None:
        user_list = user_list.filter_by(gender=gender)
    if department_id:
        user_list = user_list.filter_by(department_id=int(department_id))
    if create_time:
        user_list = user_list.filter(
            User.create_time >= datetime.strptime(create_time[:19], "%Y-%m-%dT%H:%M:%S")
        )
    total = user_list.count()
    user_list = get_parse_response(user_list.paginate(page, page_size).items)
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
        import random, string

        data = request.get_json()

        user = User()
        user.name = data.get('name')
        user.email = data.get(
            'email',
            ''.join(random.choices(string.ascii_letters, k=random.randint(5, 10)))
            + '@email.com',
        )
        user.password = make_password(data.get('password', 'password'))
        user.position = data.get('position')
        user.age = data.get('age', 0)
        user.office = data.get('office')
        user.salary = data.get('salary', 0)
        user.gender = data.get('gender', '男')
        user.status = data.get('status', '在职')
        user.department_id = data.get('department_id', 1)

        db.session.add(user)
        db.session.commit()
        return jsonify({'code': status_code.OK, 'data': dict(user)})
    elif request.method == 'PUT':
        data = request.get_json()
        user_id = data.get('id')

        user = User.query.filter_by(id=user_id).first()
        name = data.get('name')
        age = data.get('age')
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
        if age is not None:
            user.age = age
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


# @apis.route('/menu/list/', methods=['GET'])
# def api_menu_list():
#     menu_list = Menu.query.order_by(Menu.level).all()

#     resp = []
#     menus = {}
#     for menu in menu_list:
#         line = {}
#         if menu.level == 0:
#             line['title'] = menu.name
#             line['path'] = menu.path
#             line['children'] = []
#             resp.append(line)
#             menus[menu.id] = line
#         elif menu.level == 1:
#             line = menus[menu.parent]
#             subline = {'title': menu.name, 'path': menu.path}
#             line['children'].append(subline)
#     return jsonify({'code': status_code.OK, 'data': resp})


@apis.route('/user/login/', methods=['POST'])
def student_login():
    '''Login user by phone and password.'''

    data = request.get_json()
    work_no = data.get('work_no')
    password = data.get('password')

    stu_obj = User.query.filter_by(work_no=work_no).first()
    if not stu_obj:
        return jsonify({'code': status_code.USER_NOT_EXISIT, 'msg': '该学生不存在'})

    if not check_password(password, stu_obj.password):
        return jsonify({'code': status_code.USER_WRONG_PWD, 'msg': '密码错误'})

    Authorization = generate_token(uid=stu_obj.uid, role='student')

    return jsonify({"code": status_code.OK, 'token': Authorization})


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
            + '@email.com'
        )
        user.password = make_password("password")
        user.position = ''.join(
            random.choices(string.ascii_letters, k=random.randint(5, 10))
        )
        user.office = ''.join(
            random.choices(string.ascii_letters, k=random.randint(5, 10))
        )
        user.salary = random.randint(2, 200) * 1000
        user.status = random.choices('在职', '休假')
        user.department_id = random.randint(1, 8)
        user.age = random.randint(22, 60)

        db.session.add(user)
        db.session.commit()
    return jsonify({'code': status_code.OK})
