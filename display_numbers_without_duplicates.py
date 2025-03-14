user_list = []
num_list = []
#ask the user for input
for num in range(10):
    num_input = int(input("Enter num{num}: ".format(num = num+1)))
    user_list.append(num_input)

for num_input in user_list:
    if num_input not in num_list:
        num_list.append(num_input)
print(num_list)
