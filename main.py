from cohort import Cohort
from exercise import Exercise
from instructor import Instructor
from student import Student

# Once you have defined all of your custom types, go to main.py, import the classes you need, and implement the following logic.

# Create 4, or more, exercises.
# Create 3, or more, cohorts.
# Create 4, or more, students and assign them to one of the cohorts.
# Create 3, or more, instructors and assign them to one of the cohorts.
# Have each instructor assign 2 exercises to each of the students.

exercise1 = Exercise("exercise1", "javascript")
exercise2 = Exercise("exercise2", "python")
exercise3 = Exercise("exercise3", "html")
exercise4 = Exercise("exercise4", "css")
cohort1 = Cohort("cohort1")
cohort2 = Cohort("cohort2")
cohort3 = Cohort("cohort3")
student1 = Student("John", "Doe")
student1.cohort = cohort1
student2 = Student("Jane", "Doe")
student2.cohort = cohort2
student3 = Student("Jill", "Doe")
student3.cohort = cohort3
instructor1 = Instructor("Doe", "John")
instructor1.cohort = cohort1
instructor2 = Instructor("Doe", "Jane")
instructor2.cohort = cohort2
instructor3 = Instructor("Doe", "Jill")
instructor3.cohort = cohort3


instructor1.assign_exercise_to_student(student1, exercise1)
instructor1.assign_exercise_to_student(student1, exercise2)
instructor1.assign_exercise_to_student(student2, exercise3)
instructor1.assign_exercise_to_student(student2, exercise4)
instructor2.assign_exercise_to_student(student1, exercise1)
instructor2.assign_exercise_to_student(student1, exercise2)
instructor2.assign_exercise_to_student(student3, exercise3)
instructor2.assign_exercise_to_student(student3, exercise4)
instructor3.assign_exercise_to_student(student2, exercise1)
instructor3.assign_exercise_to_student(student2, exercise2)
instructor3.assign_exercise_to_student(student3, exercise3)
instructor3.assign_exercise_to_student(student3, exercise4)

for cohort in [cohort1, cohort2, cohort3]: 
    for student in cohort.students:
        print(f"{student.first_name} {student.last_name} is working on " + ", ".join([student.exercises[i].name for i in range(len(student.exercises))]) + ".")

        