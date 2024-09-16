n=0
def find_length(text):
    if text =='':
        return 0
    return 1+ find_length(text[1:])

output = input("Enter a string ")

print(find_length(output))