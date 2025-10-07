with open("Input/numbers.txt", "r") as f:
    lines = f.readlines()

    result = []

    numbers = list(map(str, lines))
    for i in numbers:
        x = len(i.strip())
        result.append(f"{x} - xonali son")


with open("Output/output09.txt", "w") as f:
    f.writelines(str(result))
