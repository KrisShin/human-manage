from server_src.wraps import generate_token
from utils.util import check_password, make_password, get_parse_response
from server_src.models import Department, Factory, User, SystemCode
from flask import Blueprint, jsonify, request
from config import status_code
from config.global_params import db
from datetime import datetime

apis = Blueprint('apis', __name__, url_prefix='/api')


@apis.route('/user/role/list/', methods=['GET'])
def api_user_role_list():
    items = SystemCode.query.filter_by(code_kbn='01').all()
    resp = get_parse_response(items)

    return jsonify({'code': status_code.OK, 'data': resp})


@apis.route('/user/duty/list/', methods=['GET'])
def api_user_duty_list():
    items = SystemCode.query.filter_by(code_kbn='02').all()
    resp = get_parse_response(items)

    return jsonify({'code': status_code.OK, 'data': resp})


@apis.route('/user/abort/list/', methods=['GET'])
def api_user_abort_list():
    items = SystemCode.query.filter_by(code_kbn='00').all()
    resp = get_parse_response(items)

    return jsonify({'code': status_code.OK, 'data': resp})


@apis.route('/user/list/', methods=['POST'])
def api_user_list():
    data = request.get_json()
    page = data.get('page', 1)
    page_size = data.get('pageSize', 10)
    user_list = User.query.order_by(User.create_time.desc())

    name = data.get('name')
    role = data.get('role')
    abort_div = data.get('abort_div')
    duty = data.get('duty')
    start_time = data.get('start_time')
    end_time = data.get('end_time')

    if name:
        user_list = user_list.filter(User.name.like(f"%{name}%"))
    if role:
        sc_id = SystemCode.query.filter_by(
            code_kbn=role['code_kbn'], code_no=role['code_no']
        ).first()
        user_list = user_list.filter_by(role_cd=sc_id.id)
    if abort_div:
        sc_id = SystemCode.query.filter_by(
            code_kbn=abort_div['code_kbn'], code_no=abort_div['code_no']
        ).first()
        user_list = user_list.filter_by(abort_div=sc_id.id)
    if duty:
        sc_id = SystemCode.query.filter_by(
            code_kbn=duty['code_kbn'], code_no=duty['code_no']
        ).first()
        user_list = user_list.filter_by(duty_cd=sc_id.id)
    if start_time and end_time:
        user_list = user_list.filter(
            User.create_time >= datetime.strptime(start_time[:19], "%Y-%m-%dT%H:%M:%S"),
            User.create_time <= datetime.strptime(end_time[:19], "%Y-%m-%dT%H:%M:%S"),
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


@apis.route('/user/login/', methods=['POST'])
def student_login():
    '''Login user by phone and password.'''

    data = request.get_json()
    user_cd = data.get('user_cd')
    password = data.get('password')

    user_obj = User.query.filter_by(user_cd=user_cd).first()
    if not user_obj:
        return jsonify({'code': status_code.USER_NOT_EXIST, 'msg': '该学生不存在'})

    if not check_password(password, user_obj.password):
        return jsonify({'code': status_code.USER_WRONG_PASSWORD, 'msg': '密码错误'})

    db.session.commit()

    Authorization = generate_token(uid=user_obj.user_cd, role=user_obj.role_cd)

    return jsonify({"code": status_code.OK, 'token': Authorization})


@apis.route('/department/list/', methods=['GET'])
def api_department_list():
    dp_list = Department.query.all()

    resp = get_parse_response(dp_list)
    return jsonify({'code': status_code.OK, 'data': resp})


@apis.route('/factory/list/', methods=['GET'])
def api_factory_list():
    fac_list = Factory.query.all()

    resp = get_parse_response(fac_list)
    return jsonify({'code': status_code.OK, 'data': resp})
