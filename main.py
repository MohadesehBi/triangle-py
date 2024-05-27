length = int(input("Please select a length for printing triangle:"))

if length < 2:
    print("Your input is not valid! please enter a number more than 1. for example: 2,7,20,110")
    return True

for row in range(1, length + 1):
    print("*" * row)
