def main():
    people_facts = {
        "Jeff": "Is afraid of Dogs.",
        "David": "Plays the piano.",
        "Jason": "Can fly an airplane."
    }
    
    for person, fact in people_facts.items():
        print(f"{person}: {fact}")
        
    print()
    
    # Change a fact about one of the people
    people_facts["Jeff"] = "Is afraid of heights."
    
    # Add an additional person and corresponding fact
    people_facts["Jill"] = "Can hula dance."
    
    for person, fact in people_facts.items():
        print(f"{person}: {fact}")

if __name__ == "__main__":
    main()
