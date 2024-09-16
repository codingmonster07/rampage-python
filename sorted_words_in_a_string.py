def sort_words(string):
    """Sorts the words in a given string in alphabetical order."""
    words = string.split()
    words.sort()
    return ' '.join(words)

string = input("Enter Strings ")
print(sort_words(string))