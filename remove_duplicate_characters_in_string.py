def duplicate_string(string):

    unique_list = []
    letters = list(string)
    
    for letter in letters:
        if letter not in unique_list:
            unique_list.append(letter)
            
            
            
        
    return  ''.join(unique_list)

print(duplicate_string("mickkky"))

