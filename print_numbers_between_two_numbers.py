# ask user for the start and end of the range
start_num = int(input("Enter the first number: "))
end_num = int(input("Enter the last number: "))

#loop printing numbers in between
for num in range(start_num, end_num + 1):
    print(num)
