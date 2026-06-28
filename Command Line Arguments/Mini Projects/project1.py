import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python project1.py <likes_string> <dislikes_string> <given_string>")
        return
        
    like_str = sys.argv[1]
    dislike_str = sys.argv[2]
    given_str = sys.argv[3]
    
    likes = set(like_str.split('-'))
    dislikes = set(dislike_str.split('-'))
    given = given_str.split('-')
    
    happiness = 0
    for num in given:
        if num in likes:
            happiness += 1
        elif num in dislikes:
            happiness -= 1
            
    print(happiness)

if __name__ == "__main__":
    main()
