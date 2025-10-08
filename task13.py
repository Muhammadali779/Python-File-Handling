with open("Input/students.txt", "r") as f:
    lines = f.readlines()

    sorted_names = sorted(lines, reverse= False)

with open("Output/output13.txt", "w") as f:
    f.writelines(sorted_names)