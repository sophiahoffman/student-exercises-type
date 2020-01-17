from student import Student
from cohort import Cohort
from nss_member import NSS_member

# You must define a type for representing an instructor in code.

# First name
# Last name
# Slack handle
# The instructor's cohort
# The instructor's specialty (e.g. dad jokes, excitement, dancing, etc.)
# A method to assign an exercise to a student

class Instructor(NSS_member):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.specialty: ""

    def assign_exercise_to_student(self, student, exercise):
        student.exercises.append(exercise)

    @property
    def cohort(self):
        return self.__cohort

    @cohort.setter
    def cohort(self, cohort):
        self.__cohort = cohort
        cohort.instructors.append(self)
