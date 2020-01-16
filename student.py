from exercise import Exercise
from cohort import Cohort

# You must define a custom type for representing a student in code. A student can only be in one cohort at a time. A student can be working on many exercises at a time.

# Properties
# First name
# Last name
# Slack handle
# The student's cohort
# The collection of exercises that the student is currently working on

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.handle = ""
        self.exercises = []

    @property
    def cohort(self):
        return self.__cohort


    @cohort.setter
    def cohort(self, cohort):
        self.__cohort = cohort
        cohort.students.append(self)
    