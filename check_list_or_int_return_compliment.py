def to_from_list(n):
    if type(n) is int:
        new_list = [int(digit)  for digit in str(n)]

        return new_list
    elif type(n)==list:
        length = len(n)-1
        new_num = 0
        for num in n:
            
            new_num = (num*(10**length))+new_num
            length = length-1
        return  new_num

              
