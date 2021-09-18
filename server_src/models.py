from config.global_params import db
from datetime import datetime


class Department(db.Model):
    __tablename__ = 'tb_department'

    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(64))
    employees = db.relationship(
        "User",
        backref="department",
        cascade="all, delete-orphan",
        passive_deletes=True,
        lazy=True,
    )

    def keys(self):
        return ('id', 'name')

    def __getitem__(self, item):
        return getattr(self, item)


class User(db.Model):
    __tablename__ = 'tb_users'
    '''
    工厂ID	factory_cd
    用户ID	user_cd
    用户名	user_nm
    密码	password
    权限代码	role_cd
    倒班区分	duty_cd
    部门ID	dep_cd
    备注	comment
    使用区分	abort_div
    代码ID	create_user_id
    生成时间	create_date
    更新代码ID	update_pgid
    更新用户ID	update_user_id
    更新时间	update_date
    更新次数	update_count
    '''
    ROLE_SUPERADMIN = 0
    ROLE_ADMIN = 1
    ROLE_USER = 2

    factory_cd = db.Column(
        db.Integer, db.ForeignKey("tb_department.id", ondelete="CASCADE"), index=True
    )
    user_cd = db.Column(db.Integer, primary_key=True, index=True)
    user_nm = db.Column(db.String(64))
    password = db.Column(db.String(512))
    role_cd = db.Column(
        db.Enum(ROLE_SUPERADMIN, ROLE_ADMIN, ROLE_USER),
        server_default=ROLE_USER,
        nullable=False,
        index=True,
    )
    duty_cd = db.Column(db.String(2), nullable=True, default='男')
    abort_div = db.Column(db.String(512))
    create_user_id = db.Column(db.String(64))
    update_pgid = db.Column(db.String(512))
    comment = db.Column(db.String(512))
    update_user_id = db.Column(db.Float())
    update_count = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, onupdate=datetime.now)
    dep_cd = db.Column(
        db.Integer, db.ForeignKey("tb_department.id", ondelete="CASCADE"), index=True
    )

    def keys(self):
        return (
            'id',
            'name',
            'email',
            'age',
            'create_time',
            'update_time',
            'position',
            'status',
            'office',
            'gender',
            'salary',
            'department_id',
            'department',
        )

    def __getitem__(self, item):
        if item in ('create_time', 'update_time'):
            time = getattr(self, item)
            return str(time)[:19] if time else time
        elif item == 'department':
            if self.department:
                return self.department.name
            return
        return getattr(self, item)


class Factory(db.Model):
    __tablename__ = 'm_factory'

    factory_cd = db.Column(db.String(2), primary_key=True)
    factory_nm = db.Column(db.String(20))
    comment = db.Column(db.Text)
    abort_div = db.Column(db.Enum(0,1,2),default=0, index=True)  # 使用分区, 1.停用 2.废弃 0.正常(默认)
    create_user_id = 
    create_date
    update_pgid
    update_user_id
    update_date
    update_count