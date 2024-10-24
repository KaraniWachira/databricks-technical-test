# Write a Python function that checks whether a word or phrase is palindrome or
# not.
# Note: A palindrome is word, phrase, or sequence that reads the same
# backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run"


def is_palindrome(input_string):

    # Remove any leading or trailing whitespace from the input string
    input_string = input_string.strip()

    # Convert the input string to lowercase to make the comparison case-insensitive
    input_string = input_string.lower()

    # Remove any non-alphanumeric characters from the input string
    input_string = ''.join(e for e in input_string if e.isalnum())

    # Compare the input string with its reverse to satisfy the objective. If they are the same, the input string is a palindrome
    return input_string == input_string[::-1]

def main():
    # input from the user
    new_string = input("Enter a word or phrase: ")

    # Check if the input is a palindrome
    if is_palindrome( new_string):
        print(f"'{ new_string}' is a palindrome.")
    else:
        print(f"'{ new_string}' is not a palindrome.")

if __name__ == "__main__":
    main()