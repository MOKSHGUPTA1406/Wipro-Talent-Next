import sys
import collections
import re

def find_secret_message(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            
        num_lines = len(lines)
        if num_lines == 0:
            print("File is empty.")
            return
            
        if num_lines > 12:
            time = num_lines - 12
            meridian = "PM"
        elif num_lines == 12:
            time = 12
            meridian = "PM"
        elif num_lines == 24:
            time = 12
            meridian = "AM"
        else:
            time = num_lines
            meridian = "AM"
            
        content = " ".join(lines)
        words = re.findall(r'\b\w+\b', content)
        
        if not words:
            print("No words found in the file.")
            return
            
        word_counts = collections.Counter(words)
        max_word = max(word_counts, key=word_counts.get)
        
        place = max_word.capitalize()
        
        print(f"Meeting time: {time} {meridian}")
        print(f"Meeting place: {place} Street")
        
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        find_secret_message(sys.argv[1])
    else:
        print("Please provide the filename as a command line argument.")
