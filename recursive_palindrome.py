# string = "level"
# # print(string[1:-1])
# i = 0

# for char in string:
#     i -=1
#     if char == string[::-1+i]:
#         print("Pallindrome")
#     else:
#         print("Not a Pallindrome")

string = "level"
i = 0
is_palindrome = True  # Assume it's a palindrome unless proven otherwise

# Loop through half of the string
for i in range(len(string) // 2):
    if string[i] != string[-(i + 1)]:  # Compare from both ends
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not a Palindrome")











def palindrome(string):
    if len(string) <= 1:
        return True
    if string[0]!=string[-1]:
        return False
    
    return palindrome(string[1:-1])

output = palindrome("level")
if output is False:
    print("Not a Palindrome")
elif output is True:
    print("Plaindrome")
else:
    print("Invalid")