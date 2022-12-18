class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name) 

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.lectures_attached and course in self.courses_in_progress:
            if course in lecturer.lecturer_grade:
                lecturer.lecturer_grade[course] += [grade]
            else:
                lecturer.lecturer_grade[course] = [grade]
        else:
            return 'Error'

    def _average_homework_grade(self):
        res = sum(*self.grades.value()) / len(*self.grades.values())
        return res

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        f'Средняя оценка за домашние задания: {self._average_homework_grade()}\n'
        f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
        f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt___(self, other):
        if not isinstance (other, Student):
            print("Not a Student!")
            return
        return self._average_homework_grade() < other._average_homework_grade()    

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
class Lecturer(Mentor):
    lectures_attached = []
    lecturer_grade = {}

    def _average_lectures_grade(self):
        result = sum(*self.lecturer_grade.values()) / len(*self.lecturer_grade.values())
        return result

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_lectures_grade()}'    
        return res

    def __lt___(self, other):
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

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
dmitry_titiaev = Reviewer('Dmitry', 'Titiaev')
print (dmitry_titiaev)