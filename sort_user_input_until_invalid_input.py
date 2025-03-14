# using same format as the lowest until invalid input program
# intialize list for user input
user_list = []

# ask user for input
while True: 
    try: # check if user input is valid
        user_input = float(input("Enter your number: ")) #float is used to include user input decimals
        user_list.append(user_input)
                
    except ValueError: #check if user input is invalid
        print("User input invalid. Stopping program....")
        user_list.sort() #separated sort function to sort list first before printing value of list
        print("The sorted number list is: ", user_list)
        break
