from collections import Counter

with open("Input/grades.csv", "r") as f:
    grades = f.readlines()

students = list(map(lambda n: n.strip().split(","), grades))
grades = list(filter(lambda n: n[1].isdigit(), students))
numbers_grades = [int(n[1]) for n in grades]


counted = Counter(numbers_grades)

with open("Output/output23.txt", "w") as f:
    f.write("Har bir baho nechi marta qatnashgan:\n")
    for grade, count in counted.items():
        f.write(f"Baho {grade}: {count} marta\n")
