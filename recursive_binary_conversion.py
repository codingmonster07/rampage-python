



def find_binary(decimal):
    if decimal == 0:
        return ""

    # recursively divide decimal by 2 
    # and concatenate remainder to the result
    return find_binary(decimal // 2) + str(decimal % 2)

binary_representation = find_binary(12)
print(binary_representation)