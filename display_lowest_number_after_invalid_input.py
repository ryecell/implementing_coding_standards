# using same format as the unique and duplicate program

# intialize list for user input
user_list = []

# ask user for input
while True: 
    try: # check if user input is valid
        user_input = float(input("Enter your desierd number: "))
        user_list.append(user_input)
                
    except ValueError: #check if user input is invalid
        print("User input invalid. Stopping program....")
        print("The lowest number is: ", min(user_list))
        break