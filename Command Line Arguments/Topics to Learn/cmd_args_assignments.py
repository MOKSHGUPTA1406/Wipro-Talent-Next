import sys
import os

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    args = sys.argv[1:]
    
    if len(args) == 2:
        # 1. Accept two numbers as command line arguments and display their sum.
        try:
            num1 = float(args[0])
            num2 = float(args[1])
            print("Sum:", num1 + num2)
        except ValueError:
            print("Please provide two valid numbers for Assignment 1.")
            
    elif len(args) == 1:
        # 2. Accept a welcome message through command line arguments and display the file name along with the welcome message.
        filename = os.path.basename(sys.argv[0])
        message = args[0]
        print(f"File: {filename}, Welcome Message: {message}")
        
    elif len(args) == 10:
        # 3. Accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.
        try:
            numbers = [int(x) for x in args]
            prime_sum = sum(x for x in numbers if is_prime(x))
            print("Sum of prime numbers:", prime_sum)
        except ValueError:
            print("Please provide 10 valid integers for Assignment 3.")
            
    else:
        print("Usage:")
        print(" Assignment 1 (Sum two numbers): python script.py <num1> <num2>")
        print(" Assignment 2 (Welcome message): python script.py <message>")
        print(" Assignment 3 (Sum of 10 primes): python script.py <n1> <n2> ... <n10>")

if __name__ == "__main__":
    main()
