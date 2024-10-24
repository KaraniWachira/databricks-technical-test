# Write a Python function to check whether a string is pangram or not. (Assume
# the string passed in does not have any punctuation)
# Note: Pangrams are words or sentences containing every letter of the
# alphabet at least once. For example: "The quick brown fox jumps over the
# lazy dog"

def is_pangram(input_string):

    # Convert the input string to lowercase to make the comparison case-insensitive
    input_string = input_string.lower()

    # Create a set of all lowercase English letters
    alphabet = set("abcdefghijklmnopqrstuvwxyz")

    input_letters = set(input_string)

    # Check if the set of input letters is a superset of the alphabet
    # If it is, the input string is a pangram
    return alphabet.issubset(input_letters)

def main():
    # user input string
    input_string = input("Enter a string: ")

    # Check if the input is a pangram
    if is_pangram(input_string):
        print(f"'{input_string}' is a pangram.")
    else:
        print(f"'{input_string}' is not a pangram.")

if __name__ == "__main__":
    main()















