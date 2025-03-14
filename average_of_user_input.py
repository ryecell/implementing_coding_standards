#initialize list variable
user_list = []
counter = 0

#using while loop to ask user for inputs until input is invalid
while True:
    try:
        user_input = int(input("Enter your number: "))
        user_list.append(user_input)
        #number of inputs counter
        counter += 1

    except ValueError: #filter if user input is invalid
        print("Input invalid. Stopping program...")
        break

#print the calculated average using sum(user_list)/counter
print(sum(user_list)/counter)
