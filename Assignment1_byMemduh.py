class Student:
    def __init__(self, name, student_id, courses_and_grades):
        self.name = name
        self.student_id = student_id
        
        if isinstance(courses_and_grades, list):
            self.courses_and_grades = dict(courses_and_grades)
        else:
            self.courses_and_grades = courses_and_grades

    def get_average_grade(self):
        grades = self.courses_and_grades.values()
        
        if not grades:
            return 0.0
        
        total_sum = sum(grades)
        count = len(grades)
        return total_sum / count
    
    def add_course_and_grade(self, course_name, grade):
        self.courses_and_grades[course_name] = grade
    
    def get_honors_courses(self, threshold=90):
        honors_courses = []
        for course, grade in self.courses_and_grades.items():
            if grade >= threshold:
                honors_courses.append(course)
        return honors_courses
    
    def get_unique_grades(self):
        return set(self.courses_and_grades.values())


# Teil 2

# 1.
all_students = []

# Student 1
all_students.append(Student("Anna Schmidt", 1001, {'Mathematik': 95, 'Physik': 88, 'Informatik': 92}))

# Student 2 (Liste von Tupeln -> wird im __init__ in Dict umgewandelt)
all_students.append(Student("Clara Weber", 1003, [('Kunst', 98), ('Sport', 88), ('Musik', 90)]))

# Student 3
all_students.append(Student("Ben Müller", 1002, {'Geschichte': 75, 'Literatur': 80, 'Geografie': 76}))

# 2.
print("--- Auswertung des Studentenmanagers ---")

for student in all_students:
    average = student.get_average_grade()
    
    if average > 80:
        honor_courses = student.get_honors_courses()
        print(f"\n{student.name} hat einen Durchschnitt von {average:.2f} und die folgenden Honor Courses: {honor_courses}.")
    else:
        student.add_course_and_grade("Study Skills", 100)
        print(f"\n{student.name} hatte Durchschnitt {average:.2f}. 'Study Skills' (100) wurde hinzugefügt.")