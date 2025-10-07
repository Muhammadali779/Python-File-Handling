with open("Input/numbers.txt", "r") as f:
    numbers = f.readlines()
    
    filtered = list(filter(
        lambda p: int(p) % 2 == 0,
        numbers

    ))

with open("Output/output04.txt", "w") as f:
    f.write("".join(filtered))