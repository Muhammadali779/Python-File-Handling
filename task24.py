with open("Input/grades.csv", "r") as f:
    lines = f.readlines()

    students = list(map(lambda n: n.strip().split(","), lines))
    grades = list(filter(lambda n: n[1].isdigit(), students))
    number_grades = [int(n[1]) for n in grades]
    average = sum(number_grades) / len(number_grades)

    result = []
    for name, grade in grades:
        if average < int(grade):
            result.append((name, grade))

    print(result)
