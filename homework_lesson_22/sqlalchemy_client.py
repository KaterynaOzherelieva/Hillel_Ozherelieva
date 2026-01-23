import os
import random

from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import Session, sessionmaker
from dotenv import load_dotenv

from homework_lesson_22.data_provider.add_clubs import get_all_clubs
from homework_lesson_22.data_provider.add_student import get_new_student
from homework_lesson_22.declarative_base import Base
from homework_lesson_22.courses_students import Students, Club
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()


class SQLAlchemyClient:
    def __init__(self, db_url: str):
        self.db_url = db_url
        self.__engine: Engine = self.__create_engine()
        self.__session: Session = self.__create_session()

    @property
    def session(self):
        return self.__session

    def __create_engine(self) -> Engine:
        return create_engine(self.db_url)

    def __create_session(self) -> Session:
        logging.info("Creating session...")
        session = sessionmaker(bind=self.__engine)
        return session()

    def create_table(self, table_model):
        logging.info(f"Creating table {table_model.__tablename__}...")
        table_model.metadata.create_all(self.__engine)

    def create_all_tables(self):
        Base.metadata.create_all(self.__engine)

    def close_connection(self):
        logging.info("Close connection...")
        self.session.close()
        # self.__engine.dispose()


if __name__ == "__main__":
    db_url = os.getenv("DB_URL")
    client = SQLAlchemyClient(db_url=db_url)


    #_____task_2_____
    client.create_all_tables()

    all_clubs = get_all_clubs()
    client.session.add_all(all_clubs)
    client.session.commit()

    club_list_from_db = client.session.query(Club).all()

    random_students = []
    for _ in range(20):
        student = get_new_student()
        student.club = random.choice(club_list_from_db)
        random_students.append(student)

    client.session.add_all(random_students)
    client.session.commit()
    client.close_connection()


    #_____task_3_____
    students_from_sport_club = client.session.query(Students).join(Club).filter(Club.name == 'Sport').all()



    #_____task_4_____
    student_to_update = client.session.query(Students).filter_by(id=1).first()
    student_to_update.name = "Kateryna Ozherelieva"
    client.session.commit()


    student_to_delete = client.session.query(Students).filter_by(name="Kateryna Ozherelieva").first()
    client.session.delete(student_to_delete)
    client.session.commit()


