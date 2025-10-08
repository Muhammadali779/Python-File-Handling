with open("Input/students.txt", "r") as f:
    lines = f.readlines()

    names = list(map(str, lines))

with open("Output/output11.txt", "w") as f:
    f.writelines(names)