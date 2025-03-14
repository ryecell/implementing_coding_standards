#initialize list variable
user_list = []

#using while loop to ask user for inputs until input is invalid
while True:
    try:
        user_input = int(input("Enter your number: "))
        user_list.append(user_input)

    except ValueError: #filter if user input is invalid
        print("Input invalid. Stopping program...")
        break
#sorting list
user_list.sort(reverse = True)
#print sorted list
print(user_list)
