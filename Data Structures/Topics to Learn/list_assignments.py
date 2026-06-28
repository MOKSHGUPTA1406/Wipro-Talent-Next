# 1. Write a program to create a list of 5 integers and display the list items. Access individual elements through index.
def list_q1():
    lst = [10, 20, 30, 40, 50]
    print("List items:", lst)
    print("First element:", lst[0])
    print("Third element:", lst[2])

# 2. Write a program to append a new item to the end of the list.
def list_q2():
    lst = [1, 2, 3]
    lst.append(4)
    print(lst)

# 3. Write a program to reverse the order of the items in the list.
def list_q3():
    lst = [1, 2, 3, 4, 5]
    lst.reverse()
    print(lst)

# 4. Write a program to print the number of occurrences of a specified element in a list.
def list_q4():
    lst = [1, 2, 2, 3, 2, 4]
    print(lst.count(2))

# 5. Write a program to append the items of list1 to list2 in the front.
def list_q5():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list2 = list1 + list2
    print(list2)

# 6. Write a program to insert a new item before the second element in an existing list.
def list_q6():
    lst = [1, 2, 3]
    lst.insert(1, 1.5)
    print(lst)

# 7. Write a program to remove the item from a specified index in a list.
def list_q7():
    lst = [10, 20, 30, 40]
    lst.pop(2)
    print(lst)

# 8. Write a program to remove the first occurrence of a specified element from a list.
def list_q8():
    lst = [1, 2, 3, 2, 4]
    lst.remove(2)
    print(lst)

if __name__ == "__main__":
    list_q1()
