#initialize value
number_of_odd = 0

#ask user for 10 numbers
for num in range(1, 11):
    number = int(input("Enter 10 numbers. {num}: ".format(num = num)))
    # check numbers if odd
    if number % 2 == 1:
        number_of_odd += 1
        
#print number of odd
print(number_of_odd)    
