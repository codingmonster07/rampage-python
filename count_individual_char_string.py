def count_ind_char(string):
    ind_char = list(string)
    count_aplhabets = 0
    count_numbers = 0
    count_symbols = 0

    for char in ind_char:
        if (ord(char)>=65 and ord(char)<=90) or  (ord(char)>=97 and ord(char)<=122):
            count_aplhabets += 1
        
        elif  (ord(char)>=48 and ord(char)<=57):
            count_numbers += 1
       
        else:
            count_symbols += 1

    return count_aplhabets, count_numbers, count_symbols
    
a,b,c = count_ind_char("Hello123.")
print(f"Letters: {a}, Numbers: {b}, Symbols: {c}")  #



         

