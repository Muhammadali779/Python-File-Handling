with open("Input/numbers.txt", "r") as f:
    lines = f.readlines()

    result = list(filter(lambda n: int(n) % 5 == 0, lines))

with open("Output/output08.txt", "w") as f:
    f.writelines(str(result))