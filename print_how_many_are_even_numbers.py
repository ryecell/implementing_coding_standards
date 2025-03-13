#initialize counter variable
even_counter = 0

#loop ask user to input 10 numbers
for num in range(10):
    num_input = int(input("Enter 10 numbers. {num}: ".format(num = num+1)))
    #check if even
    if num_input % 2 == 0:
        even_counter += 1

