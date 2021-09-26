from config.global_params import db
from datetime import datetime


class BaseInfo(db.Model):
    __abstract__ = True

    update_user_id = db.Column(db.String(32))
    update_count = db.Column(db.Integer)
    update_pgid = db.Column(db.String(512))
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, onupdate=datetime.now)
    comment = db.Column(db.Text)


class SystemCode(BaseInfo):
    __tablename__ = 'm_system_code'

    id = db.Column(db.Integer, primary_key=True)
    code_kbn = db.Column(db.String(3))
    code_kbn_nm = db.Column(db.String(32))
    code_no = db.Column(db.String(3))
    code_nm = db.Column(db.String(32))
    flug1 = db.Column(db.String(1))
    flug1_nm = db.Column(db.String(32))
    flug2 = db.Column(db.String(1))
    flug2_nm = db.Column(db.String(10))
    flug3 = db.Column(db.String(1))
    flug3_nm = db.Column(db.String(100))

    factory_cd = db.Column(
        db.String(2),
        db.ForeignKey("m_factory.factory_cd"),
        index=True,
    )

    __table_args__ = (
        db.UniqueConstraint("code_kbn", "code_no", "factory_cd", name="unique_kbn_no"),
    )

    def keys(self):
        return ('code_kbn', 'code_kbn_nm', 'code_no', 'code_nm')

    def __getitem__(self, item):
        return getattr(self, item)


class Factory(BaseInfo):
    __tablename__ = 'm_factory'

    factory_cd = db.Column(db.String(2), primary_key=True)
    factory_nm = db.Column(db.String(64))

    abort_div = db.Column(
        db.Integer,
        db.ForeignKey("m_system_code.id"),
    )  # 数据状态0 正常, 1 停用, 2 废弃

    deps = db.relationship(
        "Department",
        backref="factory",
        cascade="all, delete-orphan",
        passive_deletes=True,
        lazy=True,
    )

    users = db.relationship(
        "User",
        backref="factory",
        cascade="all, delete-orphan",
        passive_deletes=True,
        lazy=True,
    )

    def keys(self):
        return ('factory_cd', 'factory_nm', 'abort_div')

    def __getitem__(self, item):
        if item == 'abort_div':
            sc = SystemCode.query.filter_by(id=self.abort_div).first()
            return sc.code_nm if sc else None
        return getattr(self, item)


class Department(BaseInfo):
    __tablename__ = 'm_department'

    dep_cd = db.Column(db.String(10), primary_key=True)
    dep_name = db.Column(db.String(64))

    factory_cd = db.Column(
        db.String(2),
        db.ForeignKey("m_factory.factory_cd", ondelete="CASCADE"),
        index=True,
    )

    abort_div = db.Column(
        db.Integer,
        db.ForeignKey("m_system_code.id"),
    )  # 数据状态0 正常, 1 停用, 2 废弃

    users = db.relationship(
        "User",
        backref="department",
        cascade="all, delete-orphan",
        passive_deletes=True,
        lazy=True,
    )

    def keys(self):
        return ('dep_cd', 'dep_name', 'factory', 'abort_div')

    def __getitem__(self, item):
        if item == 'abort_div':
            sc = SystemCode.query.filter_by(id=self.abort_div).first()
            return sc.code_nm if sc else None
        elif item == 'factory':
            return self.factory.factory_nm if self.factory else None
        return getattr(self, item)


class User(BaseInfo):
    __tablename__ = 'm_user'

    user_cd = db.Column(db.String(6), primary_key=True)
    user_nm = db.Column(db.String(64))  # 用户昵称
    password = db.Column(db.String(512))
    create_user_id = db.Column(db.String(6))

    role_cd = db.Column(
        db.Integer,
        db.ForeignKey("m_system_code.id"),
    )  # 关联到system_code: kbn=01

    duty_cd = db.Column(
        db.Integer,
        db.ForeignKey("m_system_code.id"),
        nullable=True,
    )  # 关联system_code: kbn=02

    abort_div = db.Column(
        db.Integer,
        db.ForeignKey("m_system_code.id"),
    )  # 数据状态0 正常, 1 停用, 2 废弃

    dep_cd = db.Column(
        db.String(10),
        db.ForeignKey("m_department.dep_cd"),
    )

    factory_cd = db.Column(
        db.String(2),
        db.ForeignKey("m_factory.factory_cd"),
    )

    info = db.relationship(
        "UserInfo",
        backref="user",
        uselist=False,
        cascade="all, delete-orphan",
        passive_deletes=True,
        lazy=True,
    )

    def keys(self):
        return (
            'user_cd',  # 用户id
            'user_nm',  # 用户姓名
            'role_cd',  # 角色
            'duty_cd',  # 班次(早班/晚班)
            # 'abort_div',  # 是否弃用
            'factory_cd',  # 所在工厂
            'dep_cd',  # 所在部门
            'create_time',  # 创建时间
            'update_time',  # 更新时间
            'name',  # 昵称
            'sex',  # 性别
            'birthday',  # 生日
            'phone',  # 固定电话
            'telephone',  # 移动电话
            'email',  # 邮箱
            'address1',  # 地址1
            'address2',  # 地址2
            'photo',  # 照片
            'comment',  # 备注
        )

    def __getitem__(self, item):
        if item in ('create_time', 'update_time'):
            time = getattr(self, item)
            return str(time)[:19] if time else time
        elif item == 'dep_cd':
            return dict(self.department) if self.department else None
        elif item == 'factory_cd':
            return dict(self.factory) if self.factory else None
        elif item in ('role_cd', 'duty_cd'):
            return self.get_system_code_nm(item)
        elif item in (
            'name',
            'sex',
            'birthday',
            'phone',
            'telephone',
            'email',
            'address1',
            'address2',
            'photo',
        ):
            return getattr(self.info, item)
        return getattr(self, item)

    def get_system_code_nm(self, item):
        res = SystemCode.query.filter_by(id=getattr(self, item)).first()
        return dict(res) if res else res


class UserInfo(BaseInfo):
    __tablename__ = 'm_user_info'

    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(32), nullable=False)
    sex = db.Column(db.Integer, nullable=False, index=True)  # 1:男, 2:女
    birthday = db.Column(db.DateTime)
    phone = db.Column(db.String(12), nullable=False)
    telephone = db.Column(db.String(12))
    email = db.Column(db.String(128))
    address1 = db.Column(db.String(256))
    address2 = db.Column(db.String(256))
    photo = db.Column(db.String(1024))

    factory_cd = db.Column(
        db.String(2),
        db.ForeignKey("m_factory.factory_cd", ondelete="CASCADE"),
        index=True,
    )

    user_cd = db.Column(
        db.String(6),
        db.ForeignKey("m_user.user_cd", ondelete="CASCADE"),
        index=True,
    )

    abort_div = db.Column(
        db.Integer,
        db.ForeignKey("m_system_code.id"),
    )  # 数据状态0 正常, 1 停用, 2 废弃


class TableDefine(BaseInfo):
    __tablename__ = 'm_table_define'

    class_name = db.Column(db.String(64))
    tbl_code = db.Column(db.String(20))
    tbl_name = db.Column(db.String(20))
    field_code = db.Column(db.String(20))
    field_name = db.Column(db.String(20))
    type = db.Column(db.String(20))
    size = db.Column(db.String(20))
    decimal = db.Column(db.Integer)
    nullable = db.Column(db.String(1))
    doc = db.Column(db.String(256))
    comment = db.Column(db.String(1024))
    key = db.Column(db.String(1))

    __table_args__ = (db.PrimaryKeyConstraint('tbl_code', 'field_code'),)

    def keys(self):
        return (
            'class_name',
            'tbl_code',
            'tbl_name',
            'field_code',
            'field_name',
            'type',
            'key',
            'size',
            'decimal',
            'nullable',
            'doc',
            'comment',
        )

    def __getitem__(self, item):
        return getattr(self, item)


# class Calendar(BaseInfo):
#     __tablename__ = 'm_calendar'

#     calendar_date = db.Column(db.String(8), primary_key=True)
#     Seq_No = db.Column(db.Integer, primary_key=True)
#     holiday_flg = db.Column(db.Integer, index=True)  # 0:工作日，1休息日
#     holiday_nm = db.Column(db.String(10))
#     event_cd = db.Column(db.Integer, index=True)  # 0: ALL 1: 作業者  2: 設備　3:その他
#     event_nm = db.Column(db.String(20))
#     event_time1 = db.Column(db.String(4), nullable=False)
#     event_time2 = db.Column(db.String(4), nullable=False)
#     month_end_flg = db.Column(db.String(1))
#     sche_flg = db.Column(db.String(1))

#     factory_cd = db.Column(
#         db.String(2),
#         db.ForeignKey("m_factory.factory_cd", ondelete="CASCADE"),
#         index=True,
#     )
