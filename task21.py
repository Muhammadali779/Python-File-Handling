with open("Input/grades.csv", "r") as f:
    grades = f.readlines()

students = list(map(lambda n: n.strip().split(","), grades))
grades = list(filter(lambda n: n[1].isdigit(), students))
numbers_grades = [int(n[1]) for n in grades]

mx_grade = max(numbers_grades)

for name, grade in grades:
    if int(grade) == mx_grade:
        top_student = name
        break

with open("Output/output21.txt", "w") as f:
    f.write(f"Eng yuqori ball: {mx_grade}\n")
    f.write(f"O`quvchi: {top_student}")
