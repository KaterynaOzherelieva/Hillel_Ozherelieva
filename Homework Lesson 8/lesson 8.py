class Student:
    def __init__(self, name: str, surname: str, age: int, average_score: float | int):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_score = average_score

    def change_score(self, new_score: float | int):
        self.average_score = new_score


person_1 = Student(name="Kateryna", surname="Ozherelieva", age=35, average_score=7)

print(person_1.name, person_1.surname, person_1.age, person_1.average_score, )

person_1.change_score(10)
print(person_1.average_score)
