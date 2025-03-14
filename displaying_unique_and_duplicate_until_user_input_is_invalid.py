# intialize list for user input
user_list = []
# ask user for input
while True: 
    try: # check if user input is valid
        user_input = float(input("Enter your desierd number: "))
        user_list.append(user_input)
        if user_input not in user_list:
            print("The number is unique")
        else:
            print("The number is a duplicate")
    except ValueError:
        break
        