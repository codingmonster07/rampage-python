numbers = [5,4,6,2,51,23]
second_largest = 0

largest = numbers[0]
for num in range(1,len(numbers)):
    if  numbers[num] > largest:
        second_largest = largest
        largest = numbers[num]

    else:
        if numbers[num] > second_largest:
            second_largest = numbers[num]


        

print(second_largest)
print(largest)

