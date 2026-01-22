from faker import Faker

from homework_lesson_22.courses_students import Students

fake = Faker()

def get_new_student() -> Students:
    return Students(name=fake.name())
