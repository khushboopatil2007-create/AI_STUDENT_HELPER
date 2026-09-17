# AI Student Help Expert System
# This file stores basic student input data.

students = []


def add_student(name, subject, problem):
    student = {
        "name": name,
        "subject": subject,
        "problem": problem
    }

    students.append(student)


def get_students():
    return students