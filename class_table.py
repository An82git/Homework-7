from sqlalchemy.orm import DeclarativeBase, Mapped, sessionmaker, mapped_column, relationship
from sqlalchemy import DATE, String, ForeignKey, create_engine


URL_DB = "postgresql://postgres:mypassword@localhost:5432/postgres"

engine = create_engine(URL_DB)
DBsession = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass

class Groups(Base):
    __tablename__ = "groups"

    id: Mapped[str] = mapped_column(String(4), primary_key=True)
    group_name: Mapped[str] = mapped_column(String(30))
    students: Mapped[list["Students"]] = relationship("Students", back_populates="groups")

class Students(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    student_name: Mapped[str] = mapped_column(String(50))
    group_id: Mapped[str] = mapped_column(String(4), ForeignKey("groups.id"))
    groups: Mapped[list["Groups"]] = relationship("Groups", back_populates="students")
    student_assessments: Mapped[list["Assessments"]] = relationship("Assessments", back_populates="students")

class Teachers(Base):
    __tablename__ = "teachers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    teacher_name: Mapped[str] = mapped_column(String(50))
    subjects: Mapped[list["Subjects"]] = relationship("Subjects", back_populates="teachers")

class Subjects(Base):
    __tablename__ = "subjects"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    subject_name: Mapped[str] = mapped_column(String(50))
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teachers.id"))
    teachers: Mapped[list["Teachers"]] = relationship("Teachers", back_populates="subjects")
    subjects_assessments: Mapped[list["Assessments"]] = relationship("Assessments", back_populates="subjects")

class Assessments(Base):
    __tablename__ = "assessments"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"))
    subject_id: Mapped[int] = mapped_column(ForeignKey("subjects.id"))
    assessment: Mapped[int]
    date_of_receipt = mapped_column(DATE)
    students: Mapped[list["Students"]] = relationship("Students", back_populates="student_assessments")
    subjects: Mapped[list["Subjects"]] = relationship("Subjects", back_populates="subjects_assessments")
