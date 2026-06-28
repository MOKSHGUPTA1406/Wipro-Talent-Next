# 1. Write a program to print the 4th element from first and 4th element from last in a tuple.
def tuple_q1():
    tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print("4th from first:", tup[3])
    print("4th from last:", tup[-4])

# 2. Write a program to check whether an element exists in a tuple or not.
def tuple_q2(tup, elem):
    return elem in tup

# 3. Write a program to convert a list into a tuple.
def tuple_q3():
    lst = [1, 2, 3]
    tup = tuple(lst)
    print(tup)

# 4. Write a program to find the index of an item in a tuple.
def tuple_q4():
    tup = (10, 20, 30, 40)
    print(tup.index(30))

# 5. Write a program to replace last value of tuples in a list to 100.
def tuple_q5():
    lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
    new_lst = [t[:-1] + (100,) for t in lst]
    print(new_lst)

if __name__ == "__main__":
    tuple_q1()
