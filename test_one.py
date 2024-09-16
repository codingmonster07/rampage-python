
unique_list = []
def duplicate_list_items(new_string):
    global i
    i = 1
    new_list = list(new_string)
    for item in new_list:
        if item in new_list[i:]:
            i +=1
            continue
        else:
            if item in new_list[:i-1]:
                i = i+1
                continue
            else:
                if item not in unique_list:
                    unique_list.append(item)
                    # i+=1
                    return i-1
    return -1


new_string = input("Enter the string: ")
b = duplicate_list_items(new_string)
if b :
    print(b)
else:
    print(b)
            
            
        