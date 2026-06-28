# 1. Write a function to return the sum of all numbers in a list.
def sum_list(lst):
    return sum(lst)

# 2. Write a function to return the reverse of a string.
def reverse_string(s):
    return s[::-1]

# 3. Write a function to calculate and return the factorial of a number (a non-negative integer).
def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 4. Write a function that accepts a string and prints the number of upper case letters and lower case letters in it.
def count_cases(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    print("No. of Upper case characters:", upper)
    print("No. of Lower case Characters:", lower)

# 5. Write a function to print the even numbers from a given list.
def even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

# 6. Write a function that takes a number as a parameter and checks whether the number is prime or not.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    print("Sum:", sum_list([8, 2, 3, 0, 7]))
    print("Reverse:", reverse_string("1234abcd"))
    print("Factorial 5:", factorial(5))
    count_cases("Hello World")
    print("Even numbers:", even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print("Is 7 prime?", is_prime(7))
