with open("Input/students.txt", "r") as f:
    lines = f.readlines()

    names = list(map(lambda n: n[::-1].title(), lines))

with open("Output/output14.txt", "w") as f:
    f.writelines(names)