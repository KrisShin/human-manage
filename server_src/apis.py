from config.settings import IMAGE_PREFIX, STATIC_FOLDER
import os
from server_src.wraps import generate_token
from utils.util import check_password, make_password, get_parse_response, gen_uuid_name
from server_src.models import (
    Department,
    Factory,
    TableDefine,
    User,
    SystemCode,
    UserInfo,
)
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
        user_cd = data.get('user_cd')
        user = User.query.filter_by(user_cd=user_cd).first()
        return jsonify({'code': status_code.OK, 'data': dict(user)})
    elif request.method == 'POST':
        user = User()
        if not _assignment_user(user, request):
            return jsonify({'code': status_code.PARAMS_LACK, 'msg': '请确认参数是否完整'})
        return jsonify({'code': status_code.OK, 'data': dict(user)})
    elif request.method == 'PUT':
        data = request.form
        user_cd = data.get('user_cd')
        user = User.query.filter_by(user_cd=user_cd).first()
        _assignment_user(user, request)
        return jsonify({'code': status_code.OK})
    elif request.method == 'DELETE':
        data = request.get_json()
        user_cd = data.get('user_cd')

        user = User.query.filter(User.user_cd.in_(user_cd)).all()
        db.session.delete(user)
        db.session.commit()
        return jsonify({'code': status_code.OK})


def _assignment_user(user_obj, request, mode='create'):
    if not any((user_obj, request)):
        return False
    data = request.form
    factory_cd = data.get('factory_cd')
    user_cd = data.get('user_cd')
    user_nm = data.get('user_nm')
    password = data.get('password')
    role_cd = data.get('role_cd')
    duty_cd = data.get('duty_cd')
    dep_cd = data.get('dep_cd')
    comment = data.get('comment')
    name = data.get('name')
    sex = data.get('sex')
    birthday = data.get('birthday')
    address1 = data.get('address1')
    address2 = data.get('address2')
    phone = data.get('phone')
    telephone = data.get('telephone')
    email = data.get('email')
    photo = request.files.get('photo')

    if user_cd:
        user_obj.user_cd = user_cd
    if factory_cd:
        user_obj.factory_cd = factory_cd
    if user_nm:
        user_obj.user_nm = user_nm
    if password:
        user_obj.password = make_password(password)
    if role_cd:
        sc = SystemCode.query.filter_by(
            code_kbn=role_cd['code_kbn'], code_no=role_cd['code_no']
        ).first()
        user_obj.role_cd = sc.id
    if duty_cd:
        sc = SystemCode.query.filter_by(
            code_kbn=duty_cd['code_kbn'], code_no=duty_cd['code_no']
        ).first()
        user_obj.duty_cd = duty_cd
    if dep_cd:
        user_obj.dep_cd = dep_cd
    if comment:
        user_obj.comment = comment
    if mode == 'create' and not all(
        user_cd, factory_cd, user_nm, role_cd, name, sex, birthday, phone
    ):
        db.session.add(user_obj)
        db.session.commit()
        info = UserInfo(user_cd=user_obj.user_cd)
        db.session.add(info)
        db.session.commit()
    else:
        return False
    if name:
        user_obj.info.name = name
    if sex:
        user_obj.info.sex = sex
    if birthday:
        user_obj.info.birthday = birthday
    if address1:
        user_obj.info.address1 = address1
    if address2:
        user_obj.info.address2 = address2
    if phone:
        user_obj.info.phone = phone
    if telephone:
        user_obj.info.telephone = telephone
    if email:
        user_obj.info.email = email
    if photo:
        ext = os.path.splitext(photo.filename)[-1]
        filename = f'{gen_uuid_name()}{ext}'
        path = STATIC_FOLDER / filename
        photo.save(path)
        user_obj.info.photo = f'{IMAGE_PREFIX}/{filename}'
    if mode == 'create':
        db.session.add(user_obj)
    db.session.commit()
    return True


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
    data = request.args
    factory_cd = data.get('factory_cd')
    dp_list = Department.query.filter_by(factory_cd=factory_cd).all()

    resp = get_parse_response(dp_list)
    return jsonify({'code': status_code.OK, 'data': resp})


@apis.route('/factory/list/', methods=['GET'])
def api_factory_list():
    fac_list = Factory.query.all()

    resp = get_parse_response(fac_list)
    return jsonify({'code': status_code.OK, 'data': resp})


@apis.route('/table/list/', methods=['POST'])
def api_table_list():
    data = request.get_json()
    page = data.get('page', 1)
    page_size = data.get('pageSize', 10)
    table_list = (
        TableDefine.query.order_by(TableDefine.create_time.desc())
        .paginate(page, page_size)
        .items
    )
    table_list = get_parse_response(table_list)
    return jsonify({'code': status_code.OK, 'data': table_list})
