#using while loop to ask user for inputs until input is invalid
user_list = []
counter_list = []
while True:
    try:
        user_input = int(input("Enter your number: "))
        user_list.append(user_input)

    except ValueError: #filter if user input is invalid
        print("Input invalid. Stopping program...")
        break

#count frequencies    
for num in user_list:
    count = user_list.count(num)
    counter_list.append(count)
    
# initial counter
print(str(max(counter_list)))

    