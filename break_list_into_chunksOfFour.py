# def big_list(my_list):
#     max = 4
#     # Base case: If my_list has no more elements, return an empty list
#     if len(my_list) == 0:
#         return []
    
#     # Take the first 4 elements (or fewer if the list is shorter)
#     current_chunk = my_list[:max]
    
#     # Recursively process the rest of the list, and return the chunks combined
#     return [current_chunk] + big_list(my_list[max:])

# # Test the function
# result = big_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(result)

chunks = []
num = [1,2,3,4,5,6,7,8,9,0]

for i in range (0,len(num),4):
    chunks.append(num[i:i+4])
    # print(f"{chunks}")

for numbers in chunks:
    print(numbers)
# new_list= []
# for i in range(0,len(num),4):
#     new_list.append(num[i])
# print(new_list)