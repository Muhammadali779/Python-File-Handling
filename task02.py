with open("Input/numbers.txt", "r") as file:
    lines = file.readlines()

    numbers = list(map(int, lines))
    result = sum(numbers)

with open("Output/output02.txt", "w") as file:
    file.write(f"Yig`indi: {result}")