class Teacher():
    def teach(self):
        print("Учитель - это человек, который обучает других людей")

class School():
    def __init__(self, new_teacher):
        self.teacher = new_teacher
    def start_lesson(self):
        self.teacher.teach()
my_teacher = Teacher()
my_school = School(my_teacher)

print(my_teacher.teach())
print(my_school.start_lesson())