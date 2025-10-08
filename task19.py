with open("Input/grades.csv", "r") as f:
    grades = f.readlines()

    students = list(map(str, grades))

with open("Output/output19.txt", "w") as f:
    f.writelines(students)