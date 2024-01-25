from random import randint, choice, sample
from datetime import date
import faker

from class_table import Groups, Students, Teachers, Subjects, Assessments, DBsession


NUMBER_STUDENTS = randint(30, 50)
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = randint(5, 8)
NUMBER_TEACHERS = randint(3, 5)
NUMBER_ASSESSMENTS = 20

subjects = ["Python Core", "SQL", "ORM", "API", "HTML and CSS", "Docker", "Git", "Django"]


def generate_fake_data(number_students, number_teachers) -> tuple():
    
    fake_students = []
    fake_teachers = []
    
    fake_data = faker.Faker()

    for _ in range(number_students):
        fake_students.append(fake_data.name())
    
    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    return fake_students, fake_teachers


def create_groups(num_groups) -> dict:
    for_groups = []
    id_groups = []
    num_list = [num for num in range(1, num_groups + 15)]
    numbers = []

    for _ in range(num_groups):
        num = choice(num_list)
        numbers.append(num)
        num_list.remove(num)
    
    numbers.sort()
    for num in numbers:
        for_groups.append((f"PD{num}", f"Python developer {num}"))
        id_groups.append(f"PD{num}")
    
    return {"id_groups": id_groups, "for_groups": for_groups}


def create_students(students, id_groups) -> dict:
    for_students = []
    id_students = [num for num in range(1, len(students) + 1)]

    for student in students:
        for_students.append((student, choice(id_groups)))

    return {"id_students": id_students, "for_students": for_students}


def create_teachers(teachers) -> dict:
    for_teachers = []
    id_teachers = [num for num in range(1, len(teachers) + 1)]

    for teacher in teachers:
        for_teachers.append((teacher, ))

    return {"id_teachers": id_teachers, "for_teachers": for_teachers}


def create_subjects(num_subjects, subjects, id_teachers) -> dict:
    for_subjects = []
    id_subjects = [num for num in range(1, num_subjects + 1)]

    for subject in sample(subjects, num_subjects):
        for_subjects.append((subject, choice(id_teachers)))

    return {"id_subjects": id_subjects, "for_subjects": for_subjects}


def create_assessments(num_assessments, id_students, id_subjects) -> list[tuple]:
    for_assessments = []

    for student in id_students:
        assessments_list = [num for num in range(1, 6)]
        student_assessments = [choice(assessments_list) for _ in range(randint(0, num_assessments))]
        
        for ass in student_assessments:
            for_assessments.append((student, choice(id_subjects), ass, date(2023, randint(9, 11), randint(1, 29))))

    return for_assessments


def prepare_data(subjects) -> list:
    students, teachers = generate_fake_data(NUMBER_STUDENTS, NUMBER_TEACHERS)
    
    gr = create_groups(NUMBER_GROUPS)

    st = create_students(students, gr["id_groups"])

    te = create_teachers(teachers)

    sub = create_subjects(NUMBER_SUBJECTS, subjects, te["id_teachers"])

    ass = create_assessments(NUMBER_ASSESSMENTS, st["id_students"], sub["id_subjects"])

    data_dict = {"groups": gr["for_groups"], 
                 "students": st["for_students"], 
                 "teachers": te["for_teachers"], 
                 "subjects": sub["for_subjects"], 
                 "assessments": ass}
    
    return data_dict


def pars_object(args_list: dict) -> dict[list]:
    object_dict = {} 
    for key, args_tuple in args_list.items():
        key_list = []
        
        if key == "groups":
            for arg in args_tuple:
                key_list.append(Groups(id=arg[0], group_name=arg[1]))

        if key == "students":
            for arg in args_tuple:
                key_list.append(Students(student_name=arg[0], group_id=arg[1]))
        
        if key == "teachers":
            for arg in args_tuple:
                key_list.append(Teachers(teacher_name=arg[0]))
        
        if key == "subjects":
            for arg in args_tuple:
                key_list.append(Subjects(subject_name=arg[0], teacher_id=arg[1]))
        
        if key == "assessments":
            for arg in args_tuple:
                key_list.append(Assessments(student_id=arg[0], subject_id=arg[1], assessment=arg[2], date_of_receipt=arg[3]))

        object_dict[key] = key_list

    return object_dict


def insert_data_to_db() -> None:
    with DBsession() as session:
        for object_list in pars_object(prepare_data(subjects)).values():
            for ob in object_list:
                session.add(ob)
            session.commit()


if __name__ == "__main__":
    insert_data_to_db()
