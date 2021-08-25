from config.global_params import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'tb_users'
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(512))
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, onupdate=datetime.now)
    password = db.Column(db.String(1024))
    position = db.Column(db.String(512))
    office = db.Column(db.String(512))
    salary = db.Column(db.Float())


# rs_library_questnar = db.Table(
#     "rs_library_questionnaire",
#     db.Column(
#         "questionnaire_lib_uid",
#         db.String(36),
#         db.ForeignKey("questionnaire_lib.uid"),
#         primary_key=True,
#     ),
#     db.Column(
#         "questionnaire_uid",
#         db.String(36),
#         db.ForeignKey("questionnaire.uid"),
#         primary_key=True,
#     ),
# )


# def db_commit():
#     db.session.commit()


# class Base(db.Model):
#     """Base model, only with uuid"""

#     __abstract__ = True

#     uid = db.Column(db.String(36), default=generate_uuid, primary_key=True, index=True)

#     def save(self):
#         db.session.add(self)
#         self.commit()

#     def commit(self):
#         db_commit()

#     def hard_delete(self):
#         db.session.delete(self)
#         db_commit()


# class BaseTime(Base):
#     """Base model with create time, update time and delete time"""

#     __abstract__ = True

#     create_time = db.Column(db.DateTime, default=datetime.now)
#     update_time = db.Column(db.DateTime, onupdate=datetime.now)
#     delete_time = db.Column(db.DateTime)

#     def delete(self):
#         self.delete_time = datetime.now()
#         self.commit()


# class User(BaseTime):
#     __abstract__ = True

#     work_no = db.Column(db.String(36), unique=True, index=True)
#     name = db.Column(db.String(64), nullable=False)
#     password = db.Column(db.String(36), nullable=False)
#     is_first = db.Column(db.Boolean, default=False)


# class Student(User):
#     __tabelname__ = "student"

#     class_no = db.Column(
#         db.String(36),
#         db.ForeignKey("stu_class.class_no", ondelete="CASCADE"),
#         index=True,
#     )

#     def keys(self):
#         return ("uid", "name", "work_no", "class_no", "is_first", "role")

#     def __getitem__(self, item):
#         if item == "role":
#             return "student"
#         return getattr(self, item)


# class Teacher(User):
#     __tablename__ = "teacher"

#     is_admin = db.Column(db.Boolean, default=False)

#     def keys(self):
#         return ("uid", "name", "work_no", "is_first", "role")

#     def __getitem__(self, item):
#         if item == "role":
#             return "admin" if self.is_admin else "teacher"
#         return getattr(self, item)


# class BaseOperator(Base):
#     """Base model with users."""

#     __abstract__ = True

#     create_by = db.Column(db.String(36), nullable=True, index=True)
#     update_by = db.Column(db.String(36), nullable=True, index=True)
#     delete_by = db.Column(db.String(36), nullable=True, index=True)

#     @property
#     def creator(self):
#         user = Student.query.filter_by(uid=self.create_by).first()
#         return user

#     @property
#     def updator(self):
#         user = Teacher.query.filter_by(uid=self.update_by).first()
#         return user

#     @property
#     def delete(self):
#         user = Teacher.query.filter_by(uid=self.delete_by).first()
#         return user


# class StuClass(Base):
#     __tabelname__ = "stu_class"

#     class_no = db.Column(db.String(36), index=True, unique=True)
#     name = db.Column(db.String(64))

#     students = db.relationship(
#         "Student",
#         backref="stuclass",
#         cascade="all, delete-orphan",
#         passive_deletes=True,
#         lazy=True,
#     )

#     def keys(self):
#         return ("uid", "class_no", "name", "count")

#     def __getitem__(self, item):
#         if item == "count":
#             return len(self.students)
#         return getattr(self, item)


# class Question(BaseTime):
#     __tablename__ = "question"

#     QUESTION_SINGLE = "single"  # 单选题，判断题
#     QUESTION_MULTIPLE = "multiple"  # 多选题
#     QUESTION_FILLBLANK = "fill_blank"  # 填空题
#     QUESTION_TEXT = "text"  # 问答题
#     QUESTION_IMAGE = "image"  # 图片题

#     code = db.Column(db.String(256))
#     name = db.Column(db.String(64))
#     description = db.Column(db.Text)
#     image = db.Column(db.String(512), nullable=True)  # 图片问题
#     category = db.Column(
#         db.Enum(
#             QUESTION_SINGLE,
#             QUESTION_MULTIPLE,
#             QUESTION_FILLBLANK,
#             QUESTION_IMAGE,
#             QUESTION_TEXT,
#         ),
#         server_default=QUESTION_SINGLE,
#         nullable=False,
#         index=True,
#     )
#     analyze = db.Column(db.Text)  # 解析
#     options = db.Column(db.JSON)  # 选项
#     answer = db.Column(db.String(512), nullable=True)  # 正确答案
#     score = db.Column(db.Float, nullable=False, default=0)  # 分值

#     questionnaire_uid = db.Column(
#         db.String(36),
#         db.ForeignKey("questionnaire.uid", ondelete="CASCADE"),
#         index=True,
#     )
#     answers = db.relationship(
#         "Answer",
#         backref="question",
#         lazy=True,
#         cascade="all, delete-orphan",
#         passive_deletes=True,
#     )

#     def keys(self, keys=QUESTION_KEYS):
#         return keys

#     def __getitem__(self, item):
#         if item == "image":
#             return IMAGE_PREFIX + self.image if self.image else None
#         if item == "questionnaire":
#             return self.questionnaire.name
#         return getattr(self, item)


# class Questionnaire(BaseTime, BaseOperator):
#     __tablename__ = "questionnaire"

#     name = db.Column(db.String(64), nullable=False)

#     questions = db.relationship(
#         "Question",
#         backref="questionnaire",
#         lazy=True,
#         cascade="all, delete-orphan",
#         passive_deletes=True,
#     )

#     @property
#     def total_score(self):
#         return sum((q.score for q in self.questions))

#     def keys(self):
#         return ("uid", "name", "libraries", "count", "lib_names")

#     def __getitem__(self, item):
#         if item == "libraries":
#             return [{"uid": lib.uid, "name": lib.name} for lib in self.libs]
#         elif item == "count":
#             return len(self.questions)
#         elif item == "lib_names":
#             return ", ".join([lib.name for lib in self.libs])
#         return getattr(self, item)


# class QuestionnaireLib(BaseOperator, BaseTime):
#     # 试卷库：试卷分类
#     __tablename__ = "questionnaire_lib"

#     name = db.Column(db.String(64), index=True, unique=True)  # 问题模块

#     questionnaires = db.relationship(
#         "Questionnaire",
#         secondary=rs_library_questnar,
#         lazy="subquery",
#         backref=db.backref("libs", lazy=True),
#     )

#     def keys(self):
#         return ("uid", "name", "count")

#     def __getitem__(self, item):
#         if item == "count":
#             return len(self.questionnaires)
#         return getattr(self, item)


# class StudentExamQuestionnaireScore(BaseTime):
#     __tablename__ = "student_exam_questnar_score"

#     score = db.Column(db.Float, nullable=True)
#     is_submit = db.Column(db.Boolean, default=False)

#     examination_uid = db.Column(
#         db.String(36),
#         db.ForeignKey("examination.uid", ondelete="CASCADE"),
#         index=True,
#     )
#     student_uid = db.Column(db.String(36), index=True)
#     questionnaire_uid = db.Column(db.String(36), index=True)

#     answers = db.relationship(
#         "Answer",
#         backref="student_exam_questnar_score",
#         lazy=True,
#         cascade="all, delete-orphan",
#         passive_deletes=True,
#     )

#     score_detail = db.Column(
#         db.JSON,
#         default={
#             "single": 0,
#             "multiple": 0,
#             "fill_blank": 0,
#             "image": 0,
#             "text": 0,
#         },
#     )

#     @property
#     def student(self):
#         return Student.query.filter_by(uid=self.student_uid).first()

#     @property
#     def questionnaire(self):
#         return Questionnaire.query.filter_by(uid=self.questionnaire_uid).first()

#     @classmethod
#     def stu_in_exam(cls, uid):
#         return cls.query.filter_by(examination_uid=uid)

#     @classmethod
#     def exam_with_stu(cls, uid):
#         return cls.query.filter_by(student_uid=uid)

#     def calc_student_score(self):
#         if self.score is not None:
#             return self.score
#         score_detail = self.score_detail
#         score = 0.0

#         for ans in self.answers:
#             if ans.score is not None:
#                 score_detail[ans.question.category] += ans.score
#                 score += ans.score
#             else:
#                 return None
#         else:
#             self.score = score
#             self.score_detail = score_detail
#             self.commit()
#             return score

#     def keys(self):
#         return (
#             "uid",
#             "examination_uid",
#             "exam",
#             "student_uid",
#             "student_no",
#             "student_name",
#             "questionnaire_uid",
#             "questionnaire_name",
#             "score_detail",
#             "question_count",
#             "correct_count",
#             "score",
#         )

#     def __getitem__(self, item):
#         if item == "score":
#             return self.calc_student_score()
#         elif item == "question_count":
#             if not self.questionnaire:
#                 return 0
#             return len(self.questionnaire.questions)
#         elif item == "correct_count":
#             return Answer.query.with_parent(self).filter(Answer.score > 0).count()
#         elif item == "exam":
#             return dict(self.examination)
#         elif item == "student_name":
#             if not self.student:
#                 return '学生已被删除'
#             return self.student.name
#         elif item == "student_no":
#             if not self.student:
#                 return
#             return self.student.work_no
#         elif item == "questionnaire_name":
#             if not self.questionnaire_uid or not self.questionnaire:
#                 return '学生未选择试卷'
#             return self.questionnaire.name
#         return getattr(self, item)


# class Answer(BaseTime):
#     __tablename__ = "answer"

#     content = db.Column(db.Text, nullable=True)
#     score = db.Column(db.Float, nullable=True)  # 为空表示未评判, True表示回答正确, False表示错误

#     student_uid = db.Column(db.String(36), index=True)  # 答题的学生，非空
#     teacher_uid = db.Column(db.String(36), nullable=True)  # 批改的老师，默认为空（自动批改）

#     question_uid = db.Column(
#         db.String(36), db.ForeignKey("question.uid", ondelete="CASCADE"), index=True
#     )
#     seqs_uid = db.Column(
#         db.String(36),
#         db.ForeignKey("student_exam_questnar_score.uid", ondelete="CASCADE"),
#     )

#     __table_args__ = (
#         db.UniqueConstraint("question_uid", "seqs_uid", name="unique_ques_seqs"),
#     )

#     @property
#     def student(self):
#         """答题学生"""
#         return Student.query.filter_by(uid=self.student_uid).first()

#     @property
#     def teacher(self):
#         """阅卷老师"""
#         return Teacher.query.filter_by(uid=self.teacher_uid).first()

#     def keys(self):
#         return ("uid", "content", "student_uid", "is_right", "score")

#     def __getitem__(self, item):
#         if item == 'content' and (self.question.category == Question.QUESTION_MULTIPLE):
#             return json.loads(self.content or '[]')
#         if item == "is_right":
#             return (self.score or 0) > 0
#         if item == "score" and (
#             self.student_exam_questnar_score.examination.status != Examination.EXAM_END
#         ):
#             return
#         return getattr(self, item)


# class Examination(BaseTime, BaseOperator):
#     __tablename__ = "examination"
#     EXAM_SPECIFY = "specify"  # 指定试卷
#     EXAM_RANDOM = "random"  # 随机试卷（选择随机范围）
#     EXAM_CUSTOMIZE = "customize"  # 自定义（选择范围）， 学生自选

#     EXAM_PENDING = "pending"
#     EXAM_RUNNING = "running"
#     EXAM_END = "end"

#     name = db.Column(db.String(64), nullable=False)
#     description = db.Column(db.Text)
#     category = db.Column(
#         db.Enum(EXAM_SPECIFY, EXAM_RANDOM, EXAM_CUSTOMIZE),
#         server_default=EXAM_SPECIFY,
#         nullable=False,
#         index=True,
#     )

#     duration = db.Column(db.Integer, nullable=False, default=60)
#     start_time = db.Column(db.DateTime, nullable=True)
#     end_time = db.Column(db.DateTime, nullable=True)
#     status = db.Column(
#         db.Enum(EXAM_PENDING, EXAM_RUNNING, EXAM_END),
#         server_default=EXAM_PENDING,
#         nullable=False,
#         index=True,
#     )

#     questionnaire_uid_list = db.Column(db.JSON)

#     seqs_list = db.relationship(
#         "StudentExamQuestionnaireScore",
#         backref="examination",
#         cascade="all, delete-orphan",
#         passive_deletes=True,
#         lazy=True,
#     )

#     def keys(self):
#         return (
#             "uid",
#             "name",
#             "description",
#             "category",
#             "create_time",
#             "start_time",
#             "end_time",
#             "status",
#             "duration",
#         )

#     def __getitem__(self, item):
#         if item in ("create_time", "start_time", "end_time"):
#             time = getattr(self, item)
#             if time:
#                 return time.strftime("%Y-%m-%d %H:%M:%S")
#             return ""
#         return getattr(self, item)

#     def start(self, user_uid=None):
#         self.start_time = datetime.now()
#         self.end_time = self.start_time + timedelta(minutes=self.duration)
#         self.update_by = user_uid
#         self.status = self.EXAM_RUNNING
#         self.commit()
#         t = Thread(target=timeout_end_examination, args=(self.uid, self.duration))
#         t.start()

#     def end(self, user_uid=None):
#         self.end_time = datetime.now()
#         self.update_by = user_uid
#         self.status = self.EXAM_END
#         self.commit()
