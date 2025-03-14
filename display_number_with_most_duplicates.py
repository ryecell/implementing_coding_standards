#initialize lists
user_list = []

#using while loop to ask user for inputs until input is invalid
while True:
    try:
        user_input = int(input("Enter your number: "))
        user_list.append(user_input)

    except ValueError: #filter if user input is invalid
        print("Input invalid. Stopping program...")
        break

#count frequencies    
counter = max(set(user_list), key=user_list.count)
    
# initial counter
print(counter)
