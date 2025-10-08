with open("Input/grades.csv", "r") as f:
    grades = f.readlines()

students = list(map(lambda n: n.strip().split(","), grades))
grades = list(filter(lambda n: n[1].isdigit(), students))
numbers_grades = [int(n[1]) for n in grades]

students_list = []
grade_5 = numbers_grades.count(5)
for name, grade in grades:
    if int(grade) == 5:
        students_list.append(name)



with open("Output/high_scores.csv", "w") as f:
    f.write(f"Bahosi 5 bo`lganlar Talabalar: {students_list}")
    