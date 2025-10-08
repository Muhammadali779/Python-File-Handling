with open("Input/grades.csv", "r") as f:
    grades = f.readlines()

students = list(map(lambda n: n.strip().split(","), grades))

grades = list(filter(lambda n: n[1].isdigit(), students))

numbers_grades = [int(n[1]) for n in grades]

average = sum(numbers_grades) / len(numbers_grades)


with open("Output/output20.txt", "w") as f:
    f.write(f"Barcha baholarning o`rtachasi: {average}")
