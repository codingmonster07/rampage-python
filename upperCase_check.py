def check(string):
    new_list = list(string)
    index_list = []
    i=0

    for key in new_list:
        if key.isupper():
            index_list.append(i)
            i+=1
        else:
            i=i+1
            continue

    return index_list

string = input("Enter A string ")
print(check(string))