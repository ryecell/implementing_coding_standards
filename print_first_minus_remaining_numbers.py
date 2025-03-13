#intialize variable
first_number = int(input("Enter your first number: "))

#loop for the remaining numbers
for num in range(1,10):
    remaining_numbers = int(input("Enter the rest of the numbers: "))
    first_number -= remaining_numbers
print(first_number)
