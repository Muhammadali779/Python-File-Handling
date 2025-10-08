with open("Input/students.txt", "r") as f:
    names = f.read().splitlines()

search_name = input("Ism kiriting: ")

if search_name.title() in names:
    result = f"{search_name.title()} faylda mavjud!"
else:
    result = f"{search_name.title} faylda mavjud emas!"

with open("Output/a_names.txt", "w") as f:
    f.write(result)

