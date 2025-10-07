with open("Input/numbers.txt", "r") as f:
    lines = f.readlines()

    mx = max(lines, key= int)

with open("Output/output03.txt", "w") as f:
    f.write(f"Max number is : {mx}")