"""
HW 12
Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

Вам предоставлен файл subjects.csv, содержащий предметы. Сейчас в файл записана следующая информация.

Математика,Физика,История,Литература

Создайте класс Student, который будет представлять студента и его успехи по предметам.

Класс должен иметь следующие методы:

__init__(self, name, subjects_file):
конструктор класса, принимающий ФИО студента и имя файла с данными о предметах и оценках.

add_subject(self, subject, grade, test_score):
метод для добавления информации о предмете, оценке и результате теста.

get_average_grade(self):
метод, возвращающий средний балл студента по всем предметам.

get_subjects(self):
метод, возвращающий список всех предметов, по которым есть информация у студента.

Реализовать функцию get_average_grades(students),
которая принимает список студентов и выводит информацию о средних баллах для каждого студента.

Реализовать функцию get_subject_average(students, subject),
которая принимает список студентов и название предмета,
и выводит информацию о среднем балле по этому предмету для каждого студента.

Реализовать функцию get_top_student(students, subject),
которая принимает список студентов и название предмета,
и выводит информацию о студенте с наивысшим средним баллом по этому предмету.
"""
import csv


class FullNameValidation:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        items = value.split()
        for item in items:
            self.validate(item)
        setattr(instance, self.param_name, value)

    # def validate(self, value):
    #     if value:
    #         for char in value:
    #             if char.isdigit():
    #                 raise ValueError(f'Value "{value}" contains digits')
    #         if not value.istitle():
    #             raise ValueError(f'Value "{value}" does not start with the title')

    def validate(self, value):
        if value and value.istitle():
            for char in value:
                if char.isdigit():
                    raise ValueError('ФИО должно состоять только из букв и начинаться с заглавной буквы')
        else:
            raise ValueError('ФИО должно состоять только из букв и начинаться с заглавной буквы')


class Student:
    name = FullNameValidation()

    def __init__(self, name: str, subjects_file: str = 'subjects.csv'):
        self.name = name
        self.subjects_file = subjects_file
        self.subjects = {}
        self.subjects_lst = self.get_subject_lst

    @property
    def get_subject_lst(self):
        subjects_lst = []
        with open('subjects.csv', mode='r', encoding='UTF-8') as file:
            reader = csv.reader(file)
            for row in reader:
                subjects_lst.extend(row)
        return subjects_lst

    def add_subject(self, subject, grade, test_score):
        if subject in self.subjects_lst:
            self.subjects[subject] = {'grade': [grade], 'test_score': [test_score]}

    def add_grade(self, subject, grade):
        if 2 <= grade <= 5:
            if subject in list(self.subjects.keys()):
                self.subjects[subject]['grade'].append(grade)
            else:
                if subject in self.subjects_lst:
                    self.subjects[subject] = {'grade': [], 'test_score': []}
                    self.subjects[subject]['grade'].append(grade)

    def add_test_score(self, subject, test_score):
        if 0 <= test_score <= 100:
            if subject in list(self.subjects.keys()):
                self.subjects[subject]['test_score'].append(test_score)
            else:
                if subject in self.subjects_lst:
                    self.subjects[subject] = {'grade': [], 'test_score': []}
                    self.subjects[subject]['test_score'].append(test_score)

    def get_average_grade(self, subject = None):
        grade_counter = 0
        grade_sum = 0
        if self.subjects and subject is None:
            for key in self.subjects.keys():
                for grade in self.subjects[key]['grade']:
                    grade_sum += grade
                    grade_counter += 1
        elif self.subjects and subject is not None:
            for grade in self.subjects[subject]['grade']:
                grade_sum += grade
                grade_counter += 1
        return grade_sum / grade_counter

    def get_average_test_score(self, subject):
        if subject in list(self.subjects.keys()):
            test_score_counter = 0
            test_score_sum = 0
            for test_score in self.subjects[subject]['test_score']:
                test_score_sum += test_score
                test_score_counter += 1
            return test_score_sum / test_score_counter

    def get_subjects(self):
        if self.subjects:
            return list(self.subjects.keys())

    def __str__(self):
        return f"Студент: {self.name}\nПредметы: {', '.join(self.subjects.keys())}"

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}", "{self.subjects_file}")'


def get_average_grades(students):
    for stud in students:
        print(f'Средний балл студента {stud}: {stud.get_average_grade()}')


def get_subject_average(students, subject):
    for stud in students:
        print(f'Средний балл студента {stud} по {subject}: {stud.get_average_grade(subject)}')


def get_top_student(students, subject):
    stud_rating = {}
    for stud in students:
        stud_rating[stud] = stud.get_average_grade(subject)
    stud_rating = dict(sorted(stud_rating.items(), reverse=True, key=lambda item: item[1]))
    print (list(stud_rating.keys())[0].name)


if __name__ == '__main__':
    student = Student("Иван Иванов", "subjects.csv")

    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)

    student.add_grade("История", 5)
    student.add_test_score("История", 92)

    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")

    average_test_score = student.get_average_test_score("Математика")
    print(f"Средний результат по тестам по математике: {average_test_score}")

    print(student)
    #
    # student2 = Student("Петр Петров", "subjects.csv")
    # student3 = Student("Дмитрий Дмитриев", "subjects.csv")
    # student4 = Student("Лучший Студент", "subjects.csv")
    # student5 = Student("Пятый Студент", "subjects.csv")
    #
    # student2.add_grade("Математика", 2)
    # student2.add_test_score("Математика", 85)
    # student2.add_grade("История", 3)
    # student2.add_test_score("История", 92)
    #
    # student3.add_grade("Математика", 2)
    # student3.add_test_score("Математика", 85)
    # student3.add_grade("История", 2)
    # student3.add_test_score("История", 92)
    #
    # student4.add_grade("Математика", 5)
    # student4.add_test_score("Математика", 100)
    # student4.add_grade("История", 5)
    # student4.add_test_score("История", 100)
    #
    # student5.add_grade("Математика", 3)
    # student5.add_test_score("Математика", 85)
    # student5.add_grade("История", 3)
    # student5.add_test_score("История", 92)
    #
    # stud = [student, student2, student3, student4, student5]
    # get_average_grades(stud)
    # get_subject_average(stud, "Математика")
    # get_subject_average(stud, "История")
    # get_top_student(stud, "Математика")
    # get_top_student(stud, "История")


    # student = Student("123 Иван", "subjects.csv")

