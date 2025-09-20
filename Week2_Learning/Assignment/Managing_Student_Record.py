# Create a Python program to represent students with attributes and actions, and manage multiple student records using classes and objects.


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    def is_passing(self):
        return self.grade >= 60

class StudentRecord:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_all_students(self):
        return [student.get_info() for student in self.students]

    def get_passing_students(self):
        return [student.get_info() for student in self.students if student.is_passing()]

record = StudentRecord()
student1 = Student("Mohan", 20, 85)
student2 = Student("Tomy", 22, 55)
student3 = Student("Robo", 19, 70)  
record.add_student(student1)
record.add_student(student2)
record.add_student(student3)
print("All Students:")
for info in record.get_all_students():
    print(info) 