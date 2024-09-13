# Replace ___ with your code

# create a function find_power()
def find_power(base, power):

    # base case
    # power raised to 0 is 1
    if power == 0:
        return 1
    
    # recursively call the function with base and power - 1 as arguments
    #  multiply the recursive call and the value of base
    return find_power(base, power - 1) * base

# take input for base and power 
base = int(input("Enter the base "))
power = int(input("Enter the power "))

# call the find_power() function
result = find_power(base,power)

# print result
print(result)