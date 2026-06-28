# 1. Write a program to accept two numbers from the user and perform division.
def q1_division():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 / num2
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# 2. Write a program to accept a number from the user and check whether it's prime or not.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def q2_prime_check():
    try:
        num = int(input("Enter a number: "))
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
    except Exception as e:
        print(f"An error occurred: {e}")

# 3. Write a program to accept the file name to be opened from the user, if file exist print the contents of the file in title case
def q3_read_file_title_case():
    filename = input("Enter file name: ")
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(content.title())
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# 4. Declare a list with 10 integers and ask the user to enter an index.
def q4_check_index():
    lst = [10, -5, 20, 0, -15, 30, -25, 40, -35, 50]
    try:
        idx = int(input("Enter an index (0-9): "))
        val = lst[idx]
        if val > 0:
            print(f"Value {val} is positive.")
        elif val < 0:
            print(f"Value {val} is negative.")
        else:
            print("Value is zero.")
    except IndexError:
        print("Error: Index out of range.")
    except ValueError:
        print("Error: Please enter a valid integer index.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("This file contains solutions for the Exception Handling assignments.")
    print("Call the individual functions (e.g. q1_division()) to test them.")
