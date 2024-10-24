# Write a program that takes an integer as input and returns an integer with
# reversed digit ordering.
# Examples:
# For input 500, the program should return 5.
# For input -56, the program should return -65.
# For input -90, the program should return -9.
# For input 91, the program should return 19.


# function that reverses the number
def reverse_integer(n):
    # Check if the number is negative, and if found negative, store the sign separately
    sign = -1 if n < 0 else 1
    n *= sign

    # Initialize a variable to store the reversed number
    reversed_n = 0

    # Loop until there are no more digits left in the number
    while n > 0:
        # Get last digit of the number
        digit = n % 10

        # Add the digit to reversed number
        reversed_n = reversed_n * 10 + digit

        # Remove the last digit from the number
        n //= 10

    # Return the reversed number with the correct sign
    return sign * reversed_n

def main():
    # user input
    user_input = input("Provide an integer: ")

    # convert the user's input into an integer
    try:
        n = int(user_input)
    except ValueError:
        # otherwise print an error message
        print("Invalid input. Please enter a valid integer.")
        return

    # Reverse the number using the reverse_integer function above
    reversed_n = reverse_integer(n)

    # Print the reversed number
    print(f"The reversed integer is: {reversed_n}")

if __name__ == "__main__":
    main()

































