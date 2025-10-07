with open("Input/numbers.txt", "r") as f:
    lines = f.readlines()

    numbers = list(filter(lambda n: int(n) % 2 == 1, lines))

with open ("Output/odd_numbers.txt", "w") as f:
    f.writelines(numbers)