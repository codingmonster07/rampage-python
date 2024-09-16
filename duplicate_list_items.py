



my_list = [2, 'python', 5, 7, 'python', 'java', 5]
duplicate_list = []
i = 0
for key in my_list:
    i=i+1
    if key in my_list[i:]:
        duplicate_list.append(key)
    else:
        i = i+1
        continue
print(duplicate_list)

























# # replace ___ with your code

# # define a list
# my_list = [2, 'python', 5, 7, 'python', 'java', 5]

# # convert list to set, so that
# # unique elements will be selected
# my_set = set(my_list)

# # empty list to store duplicate elements
# repeated_elements = []

# # loop through my_set and check if the element
# # is occurred more than one time in my_list
# for i in my_set:
#     if my_list.count(i) > 1:
#         repeated_elements.append(i)
        

# # print the duplicate elements
# print(repeated_elements)