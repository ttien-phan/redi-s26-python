students = {"Alice": [85, 92, 78], "Bob": [70, 88, 91], "Charlie": [95, 90, 93]}


def studentsAverage(studentsList):
    studentsAvrg = {}
    for name, grades in studentsList.items():
        studentsAvrg[name] = sum(grades) / len(grades)
    return studentsAvrg


def studentsHighest(studentsList):
    highestGrade = {}
    for name, grades in studentsList.items():
        highestGrade[name] = max(grades)
    return highestGrade


def studentsLowest(studentsList):
    lowestGrade = {}
    for name, grades in studentsList.items():
        lowestGrade[name] = min(grades)
    return lowestGrade


def resultStudent(studentsList):
    average = studentsAverage(studentsList)
    result = {}
    for name, avrgGrade in average.items():
        if avrgGrade >= 85:
            result[name] = "Pass"
        else:
            result[name] = "Fail"
    return result


def classAvrg(students):
    grades = []
    averages = studentsAverage(students)
    for name, grade in averages.items():
        grades.append(grade)
    classAvrg = sum(grades) / len(grades)
    return classAvrg


def bestStudent(students):
    student = ""
    currGrade = 0
    average = studentsAverage(students)
    for name, grade in average.items():
        if grade > currGrade:
            currGrade = grade
            student = name
    return student

def studentReport(students):
    averages = studentsAverage(students)
    highest = studentsHighest(students)
    lowest = studentsLowest(students)
    results = resultStudent(students)
    report = {}

    for name in students:
        report[name] = {
            "average" : averages[name],
            "highest" : highest[name],
            "lowest" : lowest[name],
            "result" : results[name]
        }

    return report

print(studentReport(students))