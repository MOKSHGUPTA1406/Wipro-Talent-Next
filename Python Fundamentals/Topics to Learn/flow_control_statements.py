# 1. Write a program to check if a given number is Positive, Negative, or Zero.
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# 2. Write a program to check if a given number is odd or even.
def check_odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# 3. Given two non-negative values, print true if they have the same last digit
def last_digit(a, b):
    return (a % 10) == (b % 10)

# 4. Write a program to print numbers from 1 to 10 in a single row with one tab space.
def print_1_to_10():
    for i in range(1, 11):
        print(i, end="\t")
    print()

# 5. Write a program to print even numbers between 23 and 57. Each number should be printed in a separate row.
def print_evens_23_to_57():
    for i in range(24, 57, 2):
        print(i)

# 6. Write a program to check if a given number is prime or not.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 7. Write a program to print prime numbers between 10 and 99.
def print_primes_10_to_99():
    for num in range(10, 100):
        if is_prime(num):
            print(num, end=" ")
    print()

# 8. Write a program to print the sum of all the digits of a given number.
def sum_of_digits(num):
    num = abs(num)
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

# 9. Write a program to reverse a given number and print.
def reverse_number(num):
    is_negative = num < 0
    num = abs(num)
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + (num % 10)
        num //= 10
    if is_negative:
        reversed_num = -reversed_num
    return reversed_num

# 10. Write a program to find if the given number is palindrome or not
def is_palindrome(num):
    num_str = str(num)
    if num_str == num_str[::-1]:
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")

if __name__ == "__main__":
    # Test cases can be run here
    print("Testing some functions:")
    print("1.", check_number(-5))
    print("2.", check_odd_even(4))
    print("3.", last_digit(7, 17))
    print("4.", end=" ")
    print_1_to_10()
    print("6.", is_prime(17))
    print("8.", sum_of_digits(1234))
    print("9.", reverse_number(1234))
    print("10.", end=" ")
    is_palindrome(110011)
