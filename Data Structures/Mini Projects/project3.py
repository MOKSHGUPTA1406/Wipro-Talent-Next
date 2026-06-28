def main():
    student_marks = {
        "Krishna": [67, 68, 69],
        "Arjun": [70, 98, 63],
        "Malika": [52, 56, 60]
    }
    
    query_name = input("Enter a name: ")
    
    if query_name in student_marks:
        marks = student_marks[query_name]
        average = sum(marks) / len(marks)
        if average.is_integer():
            print(f"Average percentage mark: {int(average)}")
        else:
            print(f"Average percentage mark: {average:.2f}")
    else:
        print("Student not found.")

if __name__ == "__main__":
    main()
