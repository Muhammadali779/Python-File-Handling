with open("Input/numbers.txt", "r") as f:
    lines = f.readlines()

    numbers = list(map(lambda n: int(n) ** 2, lines))

with open ("Output/output07.txt", "w") as f:
    
    f.writelines(str(numbers))