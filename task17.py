with open("Input/students.txt", "r") as f:
    names = f.readlines()
    first_A = list(filter(
        lambda n : n.lower().startswith("a"),
        names
    ))

with open("Output/a_names.txt", "w") as f:
    f.writelines(first_A)