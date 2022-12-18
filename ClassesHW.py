class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Error'

    def _average_homework_grade(self):
        res = sum(*self.grades.values()) / len(*self.grades.values())
        return res

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        f'Средняя оценка за домашние задания: {self._average_homework_grade()}\n'
        f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
        f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance (other, Student):
            print("Not a Student!")
            return
        return self._average_homework_grade() < other._average_homework_grade()    

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def _average_lectures_grade(self):
        result = sum(*self.grades.values()) / len(*self.grades.values())
        return result

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_lectures_grade()}'    
        return res

    def __lt__(self, other):
        if not isinstance (other, Lecturer):
            print("Not a Lecturer")
            return
        return self._average_lectures_grade() < other._average_lectures_grade()    


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error'


    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

best_student = Student('Ruoy', 'Eman', 'Male')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += "Введение в программирование"

common_student = Student('Alex', "Brown", 'Male')
common_student.courses_in_progress += ['Python', 'Git']
common_student.finished_courses += 'Введение в программирование'

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

common_lecturer = Lecturer('Jane', "Right")
common_lecturer.courses_attached = ['Python']

cool_reviewer = Reviewer('Reviewer', 'Body')
cool_reviewer.courses_attached += ['Python']

common_reviewer = Reviewer('Tom', 'Erickson')
common_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 5)

cool_reviewer.rate_hw(common_student, 'Python', 9)
cool_reviewer.rate_hw(common_student, 'Python', 5)

best_student.rate_lecturer(cool_lecturer, 'Python', 10)
common_student.rate_lecturer(common_lecturer, 'Python', 7)

student_list = [best_student, common_student]
lecturer_list = [cool_lecturer, common_lecturer]

students_grades_list = []
def average_student_grade(student_list, course):
    for student in student_list:
        for key, value in student.grades.items():
            if key is course:
                students_grades_list.extend(value)
    result = sum(students_grades_list) / len(students_grades_list)
    print(f'Средний бал по всем студентам курса {course}: {result}')

lecturers_grades_list = []
def average_lecturer_grade(lecturer_list, course):
    for lecturer in lecturer_list:
        for key, value in lecturer.grades.items():
            if key is course:
                lecturers_grades_list.extend(value)
    result = sum(lecturers_grades_list) / len(lecturers_grades_list)
    print(f'Средний бал по всем лекторам курса {course}: {result}')    

average_student_grade(student_list, 'Python')
average_lecturer_grade(lecturer_list, 'Python')

print(cool_lecturer.grades)
print(common_lecturer.grades)
print(best_student.grades)
print(common_student.grades)
print(best_student < common_student)
print(cool_lecturer < common_lecturer)
print(best_student)
print(common_student)
print(cool_lecturer)
print(common_lecturer)
print(cool_reviewer)
print(common_reviewer)
