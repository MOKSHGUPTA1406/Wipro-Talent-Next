def ispalindrome(name):
    clean_name = name.replace(" ", "").lower()
    return clean_name == clean_name[::-1]

def count_the_vowels(name):
    vowels = "aeiouAEIOU"
    return sum(1 for char in name if char in vowels)

def frequency_of_letters(name):
    clean_name = name.replace(" ", "").lower()
    freq = {}
    for char in clean_name:
        freq[char] = freq.get(char, 0) + 1
        
    freq_order = []
    seen = set()
    for char in clean_name:
        if char not in seen:
            freq_order.append(f"{char}-{freq[char]}")
            seen.add(char)
            
    return ", ".join(freq_order)
