def count_repeated_chars(sentence):
    # Convert sentence to list of characters and remove spaces
    char_list = list(sentence.replace(' ', ''))

    # Dictionary to store character counts
    repeated_char_count = {}

    # Count occurrences of each character
    for char in char_list:
        if char in repeated_char_count:
            repeated_char_count[char] += 1
        else:
            repeated_char_count[char] = 1

    # Filter characters that appear more than once
    repeated_chars = {char: count for char, count in repeated_char_count.items() if count > 1}
    print(repeated_char_count)

    return repeated_chars

# Example usage
sentence = "hello World"
repeated_characters = count_repeated_chars(sentence)
print(repeated_characters)


        

    


    




















