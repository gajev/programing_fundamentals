class Class:
    __students_count = 22
    average_grade = 0

    def __init__(self, name, students=[], grades=[]):
        self.name = name
        self.students = students
        self.grades = grades

    def add_student(self, name: str, grade: float):
        if Class.__students_count > 0:
            self.students.append(name)
            self.grades.append(grade)
            Class.__students_count -= 1
            Class.average_grade = sum(self.grades) / len(self.grades)

    def get_average_grade(self):
        return self.average_grade

    def __repr__(self):
        return f"The students in {self.name}:" + f" {', '.join(self.students)}." + \
               f" Average grade: {self.average_grade:.2f}"

a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)