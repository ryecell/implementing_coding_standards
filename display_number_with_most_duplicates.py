#using while loop to ask user for inputs until input is invalid
user_list = []
while True:
    try:
        user_input = int(input("Enter your number: "))
        user_list.append(user_input)
    except ValueError:
        print("Input invalid. Stopping program...")
        break