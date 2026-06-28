def main():
    try:
        miles = float(input("How far would you like to travel in miles? "))
        if miles < 3:
            print("I suggest Bicycle to your destination")
        elif 3 <= miles < 300:
            print("I suggest Motor-Cycle to your destination")
        else:
            print("I suggest Super-Car to your destination")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
