from utils.export_table_define import generate_excel_file
from config.settings import IMAGE_PREFIX, STATIC_FOLDER
import os
from server_src.wraps import auth, current_user_uid_role, generate_token
from utils.util import check_password, make_password, get_parse_response, gen_uuid_name
from server_src.models import (
    Department,
    Factory,
    TableDefine,
    User,
    SystemCode,
    UserInfo,
)
from flask import Blueprint, jsonify, request, send_from_directory, make_response
from config import status_code
from config.global_params import db
from datetime import datetime
import json
from urllib.parse import quote

apis = Blueprint('apis', __name__, url_prefix='/api')


@apis.route('/user/role/list/', methods=['GET'])
@auth
def api_user_role_list():
    items = SystemCode.query.filter_by(code_kbn='01').all()
    resp = get_parse_response(items)

    return jsonify({'code': status_code.OK, 'data': resp})


@apis.route('/user/duty/list/', methods=['GET'])
@auth
def api_user_duty_list():
    items = SystemCode.query.filter_by(code_kbn='02').all()
    resp = get_parse_response(items)

    return jsonify({'code': status_code.OK, 'data': resp})


@apis.route('/user/abort/list/', methods=['GET'])
@auth
def api_user_abort_list():
    items = SystemCode.query.filter_by(code_kbn='00').all()
    resp = get_parse_response(items)

    return jsonify({'code': status_code.OK, 'data': resp})


@apis.route('/user/list/', methods=['POST'])
@auth
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
        user_list = user_list.filter(User.user_nm.like(f"%{name}%"))
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
@auth
def api_user_options():
    if request.method == 'GET':
        data = request.args
        user_cd = data.get('user_cd')
        if not user_cd:
            user_cd = current_user_uid_role(request)
        user = User.query.filter_by(user_cd=user_cd).first()
        return jsonify({'code': status_code.OK, 'data': dict(user)})
    elif request.method == 'POST':
        user = User()
        res_code = _assignment_user(user, request, mode='create')
        if res_code == 0:
            return jsonify({'code': status_code.PARAMS_LACK, 'msg': '???????????????????????????'})
        elif res_code == -1:
            return jsonify({'code': status_code.USER_EXISTED, 'msg': 'user_cd?????????'})
        return jsonify({'code': status_code.OK, 'data': dict(user)})
    elif request.method == 'PUT':
        data = request.form
        user_cd = data.get('user_cd')
        user = User.query.filter_by(user_cd=user_cd).first()
        _assignment_user(user, request, mode='edit')
        return jsonify({'code': status_code.OK})
    elif request.method == 'DELETE':
        cur_user_cd = current_user_uid_role(request)
        data = request.get_json()
        user_cds = data.get('user_cd')
        if cur_user_cd in user_cds:
            return jsonify(
                {'code': status_code.USER_INVALID_OPERATION, 'msg': '??????????????????'}
            )

        user = User.query.filter(User.user_cd.in_(user_cds)).delete()
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
    role_cd = json.loads(data.get('role_cd', '{}'))
    duty_cd = json.loads(data.get('duty_cd', '{}'))
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
    photo = data.get('photo')
    abort_div = data.get('abort_div')

    if user_cd:
        user_obj.user_cd = user_cd
    if factory_cd:
        user_obj.factory_cd = factory_cd
    if user_nm:
        user_obj.user_nm = user_nm
    if mode == 'edit' and password:
        user_obj.password = make_password(password)
    elif mode == 'create':
        user_obj.password = make_password(password or 'User12345')
    if role_cd:
        sc = SystemCode.query.filter_by(
            code_kbn=role_cd['code_kbn'], code_no=role_cd['code_no']
        ).first()
        user_obj.role_cd = sc.id
    if duty_cd:
        sc = SystemCode.query.filter_by(
            code_kbn=duty_cd['code_kbn'], code_no=duty_cd['code_no']
        ).first()
        user_obj.duty_cd = sc.id
    if abort_div:
        sc = SystemCode.query.filter_by(
            code_kbn=duty_cd['code_kbn'], code_no=duty_cd['code_no']
        ).first()
        user_obj.abort_div = sc.id
    else:
        user_obj.abort_div = 1

    if dep_cd:
        user_obj.dep_cd = dep_cd
    if comment:
        user_obj.comment = comment
    if mode == 'create':
        if all((user_cd, factory_cd, user_nm, role_cd, name, sex, birthday, phone)):
            user_exisit = User.query.filter_by(user_cd=user_cd).first()
            if user_exisit:
                return -1
            db.session.add(user_obj)
            db.session.commit()
            info = UserInfo(
                user_cd=user_obj.user_cd,
                factory_cd=factory_cd,
                name=name,
                sex=sex,
                birthday=birthday,
                phone=phone,
            )
            db.session.add(info)
            db.session.commit()
        else:
            return 0
    if name:
        user_obj.info.name = name
    if sex:
        user_obj.info.sex = int(sex)
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
        # ext = os.path.splitext(photo.filename)[-1]
        # filename = f'{gen_uuid_name()}{ext}'
        # path = STATIC_FOLDER / filename
        # photo.save(path)
        user_obj.info.photo = photo

    db.session.commit()
    return 1


@apis.route('/upload/', methods=['POST'])
@auth
def api_upload():
    photo = request.files.get('file')
    if not photo:
        return jsonify({'code': status_code.NO_FILE_UPLOAD, 'msg': '??????????????????'})
    ext = os.path.splitext(photo.filename)[-1]
    filename = f'{gen_uuid_name()}{ext}'
    path = STATIC_FOLDER / filename
    photo.save(path)
    photo_url = f'{IMAGE_PREFIX}/{filename}'
    return jsonify({'code': status_code.OK, 'data': photo_url})


@apis.route('/user/login/', methods=['POST'])
def api_user_login():
    '''Login user by phone and password.'''

    data = request.get_json()
    user_cd = data.get('user_cd')
    password = data.get('password')

    user_obj = User.query.filter_by(user_cd=user_cd).first()
    if not user_obj:
        return jsonify({'code': status_code.USER_NOT_EXIST, 'msg': '??????????????????'})

    if not check_password(user_obj.password, password):
        return jsonify({'code': status_code.USER_WRONG_PASSWORD, 'msg': '????????????'})

    db.session.commit()

    Authorization = generate_token(uid=user_obj.user_cd, role=user_obj.role_cd)

    return jsonify({"code": status_code.OK, 'token': Authorization})


@apis.route('/department/list/', methods=['GET'])
@auth
def api_department_list():
    data = request.args
    factory_cd = data.get('factory_cd')
    dp_list = Department.query.filter_by(factory_cd=factory_cd).all()

    resp = get_parse_response(dp_list)
    return jsonify({'code': status_code.OK, 'data': resp})


@apis.route('/factory/list/', methods=['GET'])
@auth
def api_factory_list():
    fac_list = Factory.query.all()

    resp = get_parse_response(fac_list)
    return jsonify({'code': status_code.OK, 'data': resp})


@apis.route('/table/list/', methods=['POST'])
@auth
def api_table_list():
    data = request.get_json()
    page = int(data.get('page', 1))
    page_size = int(data.get('pageSize', 10))
    table_list = TableDefine.query.distinct(TableDefine.tbl_code).order_by(
        TableDefine.tbl_code
    )
    class_name = data.get('class_name')
    tbl_name = data.get('tbl_name')
    tbl_code = data.get('tbl_code')

    if class_name:
        table_list = table_list.filter(TableDefine.class_name.like(f'%{class_name}%'))

    if tbl_name:
        table_list = table_list.filter(TableDefine.tbl_name.like(f'%{tbl_name}%'))

    if tbl_code:
        table_list = table_list.filter(TableDefine.tbl_code.like(f'%{tbl_code}%'))
    total = table_list.count()
    table_list = table_list.all()[(page - 1) * page_size : (page * page_size)]
    resp = []
    for row in table_list:
        resp.append(
            {
                'tbl_code': row.tbl_code,
                'tbl_name': row.tbl_name,
                'class_name': row.class_name,
            }
        )
    return jsonify(
        {
            'code': status_code.OK,
            'data': resp,
            "page": page,
            "pageSize": page_size,
            "total": total,
        }
    )


@apis.route('/table/field/', methods=['POST', 'PUT', 'DELETE'])
# @auth
def api_table_field_oprations():
    if request.method == 'POST':
        table_obj = TableDefine()
        resp = _assignment_table(table_obj, request, 'create')
        if resp == 0:
            return jsonify({'code': status_code.PARAMS_LACK, 'msg': '???????????????????????????'})
        elif resp == -1:
            return jsonify({'code': status_code.FIELD_DUPLICATE, 'msg': 'field_code??????'})

        return jsonify({'code': status_code.OK, 'data': dict(table_obj)})
    elif request.method == 'PUT':
        data = request.get_json()
        field_code = data.get('field_code')
        tbl_code = data.get('tbl_code')
        table_obj = TableDefine.query.filter_by(
            tbl_code=tbl_code, field_code=field_code
        ).first()
        resp = _assignment_table(table_obj, request, 'edit')
        if resp == -1:
            return jsonify({'code': status_code.FIELD_DUPLICATE, 'msg': 'field_code??????'})
        return jsonify({'code': status_code.OK, 'data': dict(table_obj)})
    elif request.method == 'DELETE':
        data = request.get_json()
        table_list = data.get('table_list')
        if table_list:
            table_code_list = []
            for table in table_list:
                table_code_list.append(table['tbl_code'])
            table = TableDefine.query.filter(
                TableDefine.tbl_code.in_(table_code_list)
            ).delete()
            db.session.commit()
            return jsonify({'code': status_code.OK})
        field_list = data.get('field_list')
        for field in field_list:
            table = TableDefine.query.filter_by(
                field_code=field['field_code'], tbl_code=field['tbl_code']
            ).delete()
        db.session.commit()
        return jsonify({'code': status_code.OK})


@apis.route('/table/field/list/', methods=['POST'])
@auth
def api_table_field_list():
    data = request.get_json()
    code = data.get('tbl_code')
    if not code:
        return jsonify({'code': status_code.PARAMS_LACK, 'msg': '???????????????????????????'})
    field_list = TableDefine.query.filter_by(tbl_code=code).order_by(TableDefine.field_code).all()
    return jsonify({'code': status_code.OK, 'data': get_parse_response(field_list)})


def _assignment_table(table_obj, request, mode='create'):
    data = request.get_json()
    class_name = data.get('class_name')
    tbl_code = data.get('tbl_code')
    tbl_name = data.get('tbl_name')
    field_code = data.get('field_code')
    field_name = data.get('field_name')
    type = data.get('type')
    key = data.get('key')
    size = data.get('size')
    decimal = data.get('decimal')
    nullable = data.get('nullable')
    doc = data.get('doc')
    comment = data.get('comment')

    if not all((class_name, tbl_code)):
        return 0

    if class_name:
        table_obj.class_name = class_name
    if tbl_code:
        table_obj.tbl_code = tbl_code
    if tbl_name:
        table_obj.tbl_name = tbl_name
    if mode == 'create' and field_code:
        if TableDefine.query.filter_by(
            tbl_code=tbl_code, field_code=field_code
        ).first():
            return -1
        table_obj.field_code = field_code
    if field_name:
        table_obj.field_name = field_name
    if type:
        table_obj.type = type
    if size:
        table_obj.size = size
    if decimal:
        table_obj.decimal = int(decimal)
    if key:
        table_obj.key = key
    if nullable:
        table_obj.nullable = nullable
    if doc:
        table_obj.doc = doc
    if comment:
        table_obj.comment = comment

    if mode == 'create':
        db.session.add(table_obj)

    db.session.commit()
    return 1


@apis.route('/table/export/', methods=['POST'])
@auth
def api_table_export():
    data = request.get_json()
    table_code_list = data.get('table_code_list')
    if not table_code_list:
        return jsonify({'code': status_code.PARAMS_LACK, 'msg': 'table_code_list'})
    table_codes = set(table_code_list)
    field_dict = {}
    for code in table_codes:
        field_dict[code] = TableDefine.query.filter_by(tbl_code=code).all()
    excel_name = generate_excel_file(field_dict)
    # response = make_response(send_from_directory(STATIC_FOLDER, f'{excel_name}.xlsx'))
    # response.headers[
    #     "Content-Disposition"
    # ] = "attachment; filename={0}; filename*=utf-8''{0}".format(
    #     quote(f"{excel_name}.xlsx")
    # )
    # return response
    return jsonify({"code": status_code.OK, "data": excel_name})
