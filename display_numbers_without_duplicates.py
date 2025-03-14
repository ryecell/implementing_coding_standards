user_list = []
#ask the user for input
for num in range(10):
    num_input = int(input("Enter num{num}: ").format(num = num))
    user_list.append(num_input)

if num_input not in user_list:
    print(user_list)
    