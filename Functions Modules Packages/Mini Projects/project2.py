from project2_module import ispalindrome, count_the_vowels, frequency_of_letters

def main():
    names = ["bob", "marcel bentok tanaka"]
    for name in names:
        print(f"Sample input: {name}")
        
        if ispalindrome(name):
            print("Yes it is a palindrome.")
        else:
            print("No it is not a palindrome.")
            
        print(f"No of vowels: {count_the_vowels(name)}")
        print(f"Frequency of letters: {frequency_of_letters(name)}\n")

if __name__ == "__main__":
    main()
