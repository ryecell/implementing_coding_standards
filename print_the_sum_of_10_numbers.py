# ask the user to input 10 numbers
sum_numbers = 0
for num in range(1, 11):
    number = int(input("Enter 10 numbers. {num}: ".format(num = num)))
    sum_numbers += number

#print total
print(sum_numbers)