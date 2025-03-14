# intialize list and variables
user_list = []

# ask user for 10 inputs
for numbers in range(10):
    user_input = (int(input("Enter 10 numbers. Num {numbers}: ".format(numbers = numbers + 1))))
    user_list.append(user_input)
    
list_set = set(user_list) # save the list into a set to remove duplicates and save first entry

#print set
print(list_set)
