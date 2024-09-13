



num_list =[1,3,4,5,6,7,8,9,10]
n = len(num_list)


for i in range(1,n+1):
    if i in num_list:
        continue
    else:
        print(i)    # This will never be executed because of the return statement

