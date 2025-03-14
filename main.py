name = input("Enter the name here: ")

if name == "aum":
    print("Awesome name!")
else:
    print("Silly name")

print("=====")  # Step 1
i = 0  # Step 2
print(name + " is a ", end="")  # Step 2

while i < 10:  # Step 3
    print("silly ", end="")  # Step 4
    i += 1  # Step 5

print("name!")  # Step 6
