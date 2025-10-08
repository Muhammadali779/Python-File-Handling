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



with open("Output/output22.txt", "w") as f:
    f.write(f"Bahosi 5 bo`lganlar soni: {grade_5} ta \nVa ular : {students_list}")
    