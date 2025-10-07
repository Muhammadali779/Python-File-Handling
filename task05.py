with open("Input/numbers.txt", "r") as file:
    lines = file.readlines()

    numbers = list(map(int, lines))
    result = sum(numbers) / len(numbers)

with open("Output/output05.txt", "w") as file:
    file.write(f"Average : {result}")