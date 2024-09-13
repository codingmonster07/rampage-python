def remove_zeroes(n):
    new_string = str(n)
    new_list = list(new_string)

    for num in new_list:
        if num =='0':
            new_list.append('0')
            new_list.remove('0')
        else:
            continue
    return ''.join(new_list)

n = int(input("Enter a number"))
print(remove_zeroes(n))
