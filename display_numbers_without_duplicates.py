user_list = []
num_set = set()
final_num_set = set()

#ask the user for input
for num in range(10):
    num_input = int(input("Enter num{num}: ".format(num = num+1)))
    user_list.append(num_input)

#filtering numbers with duplicates
for unique_num in user_list:
    if unique_num not in num_set:
        num_set.add(unique_num)
        final_num_set.add(unique_num)
    else:
        final_num_set.discard(unique_num)

#print filtered list
print("The numbers without duplicates are:", list(final_num_set))

  
