with open("Input/numbers.txt", "r") as file:
    lines = file.readlines()

    numbers = list(map(int, lines))

with open("Output/output01.txt", "w") as file:
    for number in numbers:
        file.writelines(f"{str(number)}")