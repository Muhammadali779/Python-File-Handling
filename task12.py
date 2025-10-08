with open("Input/students.txt", "r") as f:
    lines = f.readlines()

    names = len(list(map(str, lines)))

with open("Output/output12.txt", "w") as f:
    f.writelines(f"{names} ta ismlar bor")