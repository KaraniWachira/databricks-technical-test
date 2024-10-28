# Write a program that accepts a string as input, capitalizes the first letter of each
# word in the string, and then returns the result string.
# Examples:
# "hi"=> returns "Hi"
# " i love programming"=> returns "I Love Programming"


def capitalize_first_letters(input_string):

    # taking the sentence the user gave us and breaking it into individual words
    words_given = input_string.split()

    # capitalize each letter of each word
    capitalized_words = [word.capitalize() for word in words_given]

    # then put the words back together
    return''.join(capitalized_words)

# user provide a string
user_input = input("Please enter a string: ")

# print the result
print(capitalize_first_letters(user_input))














