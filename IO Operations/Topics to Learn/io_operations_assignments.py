import os

# 1. Write a program to read the entire content from a txt file and display it to the user.
def read_entire_file(filename):
    with open(filename, 'r') as f:
        print(f.read())

# 2. Write a program to read first n lines from a txt file. Get n as user input.
def read_n_lines(filename):
    n = int(input("Enter number of lines to read: "))
    with open(filename, 'r') as f:
        for _ in range(n):
            line = f.readline()
            if not line:
                break
            print(line, end="")

# 3. Write a program to accept input from user and append it to a txt file.
def append_to_file(filename):
    user_input = input("Enter text to append: ")
    with open(filename, 'a') as f:
        f.write(user_input + "\n")

# 4. Write a program to read contents from a txt file line by line and store each line into a list.
def read_lines_to_list(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines

# 5. Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.
def longest_word(filename):
    with open(filename, 'r') as f:
        words = f.read().split()
    if words:
        return max(words, key=len)
    return None

# 6. Write a program to count the frequency of a user entered word in a txt file.
def count_word_frequency(filename):
    word_to_count = input("Enter word to count: ")
    with open(filename, 'r') as f:
        words = f.read().split()
    count = words.count(word_to_count)
    print(f"Frequency of '{word_to_count}': {count}")

if __name__ == "__main__":
    print("This script contains functions for IO Operations assignments.")
    print("You can import and call these functions passing a valid text file name.")
