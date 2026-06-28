# 1. Write a program to count the number of upper and lower case letters in a String.
def string_q1(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    print("Upper:", upper, "Lower:", lower)

# 2. Write a program that will check whether a given String is Palindrome or not.
def string_q2(s):
    return s == s[::-1]

# 3. Given a string, return a new string made of n copies of the first 2 chars of the original string where n is the length of the string.
def string_q3(s):
    if len(s) >= 2:
        return s[:2] * len(s)
    return s

# 4. Given a string, if the first or last character is 'x', return the string without those 'x' character, else return the string unchanged.
def string_q4(s):
    if s.startswith('x'):
        s = s[1:]
    if s.endswith('x'):
        s = s[:-1]
    return s

# 5. Given a string and an integer n, return a string made of n repetitions of the last n characters of the string.
def string_q5(s, n):
    if n >= 0 and n <= len(s):
        return s[-n:] * n if n > 0 else ""
    return s

if __name__ == "__main__":
    string_q1("Hello World")
