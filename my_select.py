from class_table import Assessments, Groups, Students, Subjects, Teachers, DBsession
from sqlalchemy import func, desc, or_, and_


def select_1() -> list:
    """
    Знаходить 5 студентів із найбільшим середнім балом з усіх предметів.
    """
    with DBsession() as session:
        rezult = (session.query(
            Students.id, 
            Students.student_name, 
            func.round(func.avg(Assessments.assessment), 2)
            .label('average_score')
            )
            .select_from(Assessments)
            .join(Students)
            .group_by(Students.id)
            .order_by(desc('average_score'))
            .limit(5)
            .all()
            )
    return rezult
    
 
def select_2(subject: str) -> list:
    """
    Знаходить студента із найвищим середнім балом з певного предмета.
    """
    subject_id = int(subject) if subject.isdigit() else 0

    with DBsession() as session:
        rezult = (session.query(
            Students.id,
            Students.student_name,
            func.round(func.avg(Assessments.assessment), 2)
            .label('average_score')
            )
            .select_from(Students)
            .join(Assessments)
            .join(Subjects)
            .where(
                or_(Subjects.subject_name == subject, Subjects.id == subject_id)
                )
            .group_by(Students.id)
            .order_by(desc('average_score'))
            .limit(1)
            .all()
            )
    return rezult


def select_3(subject: str) -> list:
    """
    Знаходить середній бал у групах з певного предмета.
    """
    subject_id = int(subject) if subject.isdigit() else 0

    with DBsession() as session:
        rezult = (session.query(
            Groups.id,
            Groups.group_name, 
            func.round(func.avg(Assessments.assessment), 2)
            .label('average_score')
            )
            .select_from(Groups)
            .join(Students)
            .join(Assessments)
            .join(Subjects)
            .where(
                or_(Subjects.subject_name == subject, Subjects.id == subject_id)
                )
            .group_by(Groups.id)
            .all()
            )
    return rezult


def select_4() -> list:
    """
    Знаходить середній бал на потоці (по всій таблиці оцінок).
    """
    with DBsession() as session:
        rezult = (session.query(
            func.round(func.avg(Assessments.assessment), 2)
            .label('average_score')
            )
            .select_from(Assessments)
            .all()
            )
    return rezult


def select_5(teacher: str) -> list:
    """
    Знаходить які курси читає певний викладач.
    """
    teacher_id = int(teacher) if teacher.isdigit() else 0

    with DBsession() as session:
        rezult = (session.query(
            Subjects.subject_name
            )
            .select_from(Subjects)
            .join(Teachers)
            .where(
                or_(Teachers.teacher_name == teacher, Teachers.id == teacher_id)
                )
            .group_by(Subjects.id)
            .order_by(Subjects.id)
            .all()
            )
    return rezult


def select_6(group: str) -> list:
    """
    Знаходить список студентів у певній групі.
    """
    with DBsession() as session:
        rezult = (session.query(
            Students.id,
            Students.student_name
            )
            .select_from(Students)
            .join(Groups)
            .where(
                or_(Groups.group_name == group, Groups.id == group)
                )
            .group_by(Students.id)
            .all()
            )
    return rezult


def select_7(group: str, subject: str) -> list:
    """
    Знаходить оцінки студентів у окремій групі з певного предмета.
    """
    subject_id = int(subject) if subject.isdigit() else 0

    with DBsession() as session:
        rezult = (session.query(
            Students.id,
            Students.student_name,
            Assessments.assessment
            )
            .select_from(Students)
            .join(Groups)
            .join(Assessments)
            .join(Subjects)
            .where(
                and_(
                    or_(Groups.group_name == group, Groups.id == group),
                    or_(Subjects.subject_name == subject, Subjects.id == subject_id)
                    )
                )
            .group_by(Assessments.id, Students.id)
            .all()
            )
    return rezult


def select_8(teacher: str) -> list:
    """
    Знаходить середній бал, який ставить певний викладач зі своїх предметів.
    """
    teacher_id = int(teacher) if teacher.isdigit() else 0

    with DBsession() as session:
        rezult = (session.query(
            Subjects.subject_name,
            func.round(func.avg(Assessments.assessment), 2)
            .label('average_score')
            )
            .select_from(Teachers)
            .join(Subjects)
            .join(Assessments)
            .where(
                or_(Teachers.teacher_name == teacher, Teachers.id == teacher_id)
                )
            .group_by(Subjects.id)
            .all()
            )
    return rezult


def select_9(student: str) -> list:
    """
    Знаходить список курсів, які відвідує студент.
    """
    student_id = int(student) if student.isdigit() else 0

    with DBsession() as session:
        rezult = (session.query(
            Subjects.id,
            Subjects.subject_name
            )
            .select_from(Subjects)
            .join(Assessments)
            .join(Students)
            .where(
                or_(Students.student_name == student, Students.id == student_id)
                )
            .group_by(Subjects.id)
            .all()
            )
    return rezult


def select_10(student: str, teacher:str) -> list:
    """
    Знаходить список курсів, які певному студенту читає певний викладач.
    """
    student_id = int(student) if student.isdigit() else 0
    teacher_id = int(teacher) if teacher.isdigit() else 0

    with DBsession() as session:
        rezult = (session.query(
            Subjects.id,
            Subjects.subject_name
            )
            .select_from(Subjects)
            .join(Assessments)
            .join(Students)
            .join(Teachers)
            .where(
                and_(
                    or_(Students.student_name == student, Students.id == student_id),
                    or_(Teachers.teacher_name == teacher, Teachers.id == teacher_id)
                    )
                )
            .group_by(Subjects.id)
            .all()
            )
    return rezult


def select_11(student: str, teacher: str) -> list:
    """
    Знаходить середній бал, який певний викладач ставить певному студентові.
    """
    student_id = int(student) if student.isdigit() else 0
    teacher_id = int(teacher) if teacher.isdigit() else 0

    with DBsession() as session:
        rezult = (session.query(
            Subjects.subject_name,
            func.round(func.avg(Assessments.assessment), 2)
            .label('average_score')
            )
            .select_from(Teachers)
            .join(Subjects)
            .join(Assessments)
            .join(Students)
            .where(
                and_(
                    or_(Students.student_name == student, Students.id == student_id),
                    or_(Teachers.teacher_name == teacher, Teachers.id == teacher_id)
                    )
                )
            .group_by(Subjects.id)
            .all()
            )
    return rezult


def select_12(group: str, subject: str) -> list:
    """
    Знаходить оцінки студентів у певній групі з певного предмета на останньому занятті.
    """
    subject_id = int(subject) if subject.isdigit() else 0

    with DBsession() as session:
        rezult = (session.query(
            Assessments.id
            .label("Assessments_id"),
            Students.student_name,
            Assessments.assessment,
            Assessments.date_of_receipt,
            )
            .select_from(Assessments)
            .join(Students)
            .join(Groups)
            .join(Subjects)
            .where(
                and_(
                    or_(Groups.group_name == group, Groups.id == group),
                    or_(Subjects.subject_name == subject, Subjects.id == subject_id),
                    Assessments.date_of_receipt.in_(session.query(
                        func.max(Assessments.date_of_receipt)
                        )
                        .select_from(Assessments)
                        .join(Students)
                        .join(Groups)
                        .join(Subjects)
                        .where(
                            and_(
                                or_(Groups.group_name == group, Groups.id == group),
                                or_(Subjects.subject_name == subject, Subjects.id == subject_id)
                                )
                            )
                        )
                    )
                )
            .group_by(Assessments.id, Students.id)
            .all()
            )
    return rezult


select_dict = {
    "select_1": {"func": select_1, "args": [None]},
    "select_2": {"func": select_2, "args": [("subject", "subject_id")]},
    "select_3": {"func": select_3, "args": [("subject", "subject_id")]},
    "select_4": {"func": select_4, "args": [None]},
    "select_5": {"func": select_5, "args": [("teacher", "teacher_id")]},
    "select_6": {"func": select_6, "args": [("group", "group_id")]},
    "select_7": {"func": select_7, "args": [("group", "group_id"), ("subject", "subject_id")]},
    "select_8": {"func": select_8, "args": [("teacher", "teacher_id")]},
    "select_9": {"func": select_9, "args": [("student", "student_id")]},
    "select_10": {"func": select_10, "args": [("student", "student_id"), ("teacher", "teacher_id")]},
    "select_11": {"func": select_11, "args": [("student", "student_id"), ("teacher", "teacher_id")]},
    "select_12": {"func": select_12, "args": [("group", "group_id"), ("subject", "subject_id")]}
    }
                        