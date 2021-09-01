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


class Menu(db.Model):
    __tablename__ = 'tb_menu'

    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(64))
    path = db.Column(db.String(256))
    level = db.Column(db.Integer, default=0)
    parent = db.Column(db.Integer)

    def keys(self):
        return ('id', 'name', 'path', 'level', 'parent')

    def __getitem__(self, item):
        return getattr(self, item)


class User(db.Model):
    __tablename__ = 'tb_users'

    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(512))
    gender = db.Column(db.String(2), nullable=True, default='男')
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, onupdate=datetime.now)
    password = db.Column(db.String(1024))
    position = db.Column(db.String(512))
    status = db.Column(db.String(64))
    office = db.Column(db.String(512))
    salary = db.Column(db.Float())
    age = db.Column(db.Integer)
    department_id = db.Column(
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
