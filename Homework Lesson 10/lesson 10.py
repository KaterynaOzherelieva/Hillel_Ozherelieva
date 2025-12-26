print("------------------TASK 1-------------------")

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size

person_1 = TeamLead(name="Anatoliy", salary=1000, department="PM", programming_language="Python", team_size=10)

print("Attributes from Manager:")
print(
    hasattr(person_1, "department")
)

print("Attributes from Developer:")
print(
    hasattr(person_1, "programming_language")
)


print("------------------TASK 2-------------------")

from abc import abstractmethod, ABC

class Figure(ABC):

    @abstractmethod
    def figure_area(self):
        ...

    @abstractmethod
    def figure_perimetr(self):
        ...

class Rombus(Figure):
    def __init__(self, side_a, height_a):
        self.__side_a = side_a
        self.__height_a = height_a

    def figure_area(self):
        return f"Area of the Rombus is {self.__side_a * self.__height_a}"

    def figure_perimetr(self):
        return f"Perimetr of the Rombus is {self.__side_a * 4}"

class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c,height):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c
        self.__height = height

    def figure_area(self):
        return f"Area of the Triangle is {1 / 2 * self.__side_a * self.__height}"

    def figure_perimetr(self):
        return f"Perimetr of the Triangle is {self.__side_a + self.__side_b + self.__side_c}"

class Square(Figure):
    def __init__(self, side_a):
        self.__side_a = side_a

    def figure_area(self):
        return f"Area of the Square is {self.__side_a ** 2}"

    def figure_perimetr(self):
        return f"Perimetr of the Square is {self.__side_a * 4}"


rombus_1 = Rombus(20,10)
triangle_1 = Triangle(15, 15, 15, 10)
square_1 = Square(25)

figures = [rombus_1, triangle_1, square_1]

for figure in figures:
    print(figure.figure_area())

for figure in figures:
    print(figure.figure_perimetr())