from datetime import datetime, timedelta
from functools import wraps

from flask import request, jsonify
import jwt

from config.settings import KEY
from config import status_code


def jwt_auth(auth, alg='HS256'):
    '''JWT encoding to authorization user.'''

    try:
        decode_auth = jwt.decode(auth, KEY, alg)
        exp = datetime.utcfromtimestamp(decode_auth['exp'])
        if (exp - datetime.now()).total_seconds() > 0:
            return status_code.OK, True, decode_auth['uid'], decode_auth['role'], None
    except jwt.exceptions.ExpiredSignatureError:
        return status_code.USER_TOKEN_EXPIRE, False, None, None, 'Token过期'  # token过期
    except Exception as e:
        print(e)
        return status_code.USER_INVALID_TOKEN, False, None, None, '无效Token'
    else:
        return status_code.USER_INVALID_TOKEN, False, None, None, '无效Token'  # 非法的token


def auth(func):
    '''Authorization is user logined.'''

    @wraps(func)
    def wrapper(*args, **kwargs):
        auth = request.headers.get('Authorization')
        if not auth:
            return jsonify({'code': status_code.USER_INVALID_TOKEN, 'msg': '无效Token'})
        status, auth_s, _, role = jwt_auth(auth.encode())
        if status == 200 and auth_s and role:
            return func(*args, **kwargs)
        else:
            return jsonify({'success': False, 'code': status})  # , status

    return wrapper


def current_user_uid_role(request, need_role=False):
    auth = request.headers.get('Authorization')
    if not auth:
        return
    _, _, uid, role, _ = jwt_auth(auth.encode())
    if need_role:
        return uid, role
    return uid


def generate_token(uid, role='student'):
    return jwt.encode(
        {'uid': uid, 'exp': datetime.now() + timedelta(hours=3), 'role': role},
        KEY,
        'HS256',
    )
