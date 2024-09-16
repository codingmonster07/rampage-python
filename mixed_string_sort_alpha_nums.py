def mixed_string(string):
    alpha = []
    nums = []
    for i in string:
        if i.isalpha():
            alpha.append(i)
        else:
            nums.append(i)
    
    print(alpha)
    print(nums)
    
    for i in range(len(alpha)):
        for j in range(i+1, len(alpha)):
            if alpha[i] > alpha[j]:
                alpha[i], alpha[j] = alpha[j], alpha[i]
    return alpha, nums
    
    
alpha, nums = mixed_string("a1b2c3d4")

def num_sum(nums):
    sum = 0
    for i in nums:
        sum += int(i)
    return sum
new_nums = num_sum(nums)
print(''.join(alpha) + str(new_nums))

