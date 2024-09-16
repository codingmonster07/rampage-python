# def change_cases(string):
#     str_list = list(string)
#     pas_list = list(string)
#     new_list = []
#     i = 0
#     new_list[0]  = str_list[0].upper()
#     # print(str_list[0])
#     if '_'in str_list:
#         for i in range(0,len(str_list)):
#             if str_list[i]!='_':
                
#                 new_list.append(str_list[i])
            
                
#             else:
#                 new_list[i+1] = str_list[i+1].upper()
        
#         return ''.join(str_list)
#     else:
#         pas_list[0]=pas_list[0].lower()
#         for  i in range(1,len(pas_list)):
#             if ord(pas_list[i]) >=65 and ord(pas_list[i]) <=90:
#                 pas_list[i] = chr(ord(pas_list[i])+32)
#                 pas_list.insert(i,'_')
#         return  ''.join(pas_list)
    

# print(change_cases("hello_world"))




def change_cases(string):
    # Convert the input string to a list of characters
    str_list = list(string)
    pas_list = list(string)
    new_list = []
    
    # Check if the string contains '_'
    if '_' in str_list:
        for i in range(len(str_list)):
            if str_list[i] != '_':
                # Add the character to new_list if it's not an underscore
                new_list.append(str_list[i])
            else:
                # Change the next character to uppercase if '_' is found
                if i + 1 < len(str_list):
                    new_list.append(str_list[i + 1].upper())
                i += 1  # Skip the next character since we already processed it
        return ''.join(new_list)
    else:
        # If no underscores are present, convert to lowercase with underscores for PascalCase
        pas_list[0] = pas_list[0].lower()
        i = 1
        while i < len(pas_list):
            if ord(pas_list[i]) >= 65 and ord(pas_list[i]) <= 90:  # If uppercase
                pas_list[i] = chr(ord(pas_list[i]) + 32)  # Convert to lowercase
                pas_list.insert(i, '_')  # Insert an underscore before the lowercase letter
                i += 1  # Move past the inserted underscore
            i += 1
        return ''.join(pas_list)

# Test case
print(change_cases("hello_world____"))  # Output: helloWorld
print(change_cases("HelloWorld"))   # Output: hello_world
