def thousand_separators(num):
#     return "{:,}".format(num)
# # Test the function
# print(thousand_separators(1234567))  # Outputs: 1,234,
# print(thousand_separators(1234567890))  # Outputs: 1,
    str_num = str(num)
    str_list = list(str_num)
    rev_list = str_list[::-1]
    # print(rev_list)
    # rev_list.insert(3,',')
    change = len(rev_list)
    for  i in range(3,change+4,4):
        rev_list.insert(i,',')
        
    # print(len(rev_list))
    # print(rev_list)
    string = "hello"
    become = "world"
    become +=string
    print(become)
    return ''.join(rev_list[::-1])





print(thousand_separators(1000000000000000))