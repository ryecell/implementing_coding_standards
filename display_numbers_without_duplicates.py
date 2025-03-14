user_list = []
num_list = []
unique_list = []
#ask the user for input
for num in range(10):
    num_input = int(input("Enter num{num}: ".format(num = num+1)))
    user_list.append(num_input)

#filtering duplicates
for unique_numbers in user_list:
    if unique_numbers not in num_list:
        num_list.append(unique_numbers)



print(num_list)

  
