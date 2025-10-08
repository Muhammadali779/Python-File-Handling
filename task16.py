with open("Input/students.txt", "r") as f:
    lines = f.readlines()

    names = list(filter(lambda n: len(n.strip()) > 5, lines))



with open("Output/output16.txt", "w") as f:
    f.writelines(names)