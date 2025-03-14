#initialize list variable
user_list = []
user_set = set()
final_list = []

# ask user to input 10 numbers
for num in range(10):
    user_input = int(input("Enter num{num}: ".format(num = num + 1)))
    user_list.append(user_input)
    #create a list for duplicates
    if user_input in user_list:
        final_list.append(user_input)
    else:
        pass
print(final_list)
