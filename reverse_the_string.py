def reverse_string(string):
    new_string = ''
    neu_list = []
    new_list = list(string)
    
    for value in new_list:
        if value != ' ':
            new_string += value
        else:
            neu_list.append(new_string)  # Append the current word
            new_string = ''  # Reset the new_string to start capturing the next word

    # Append the last word (since there's no space after it)
    neu_list.append(new_string)
    
    # Reverse the list and join it back into a string
    rev_list = neu_list[::-1]
    rev_string = ' '.join(rev_list)
    
    return rev_string

# Input from user
string = input("Enter The String: ")
print(reverse_string(string))

