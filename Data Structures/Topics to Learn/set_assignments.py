# 1. Write a program to remove a given item from the set.
def set_q1():
    s = {1, 2, 3, 4}
    s.discard(3)
    print(s)

# 2. Write a program to create an intersection of sets.
def set_q2():
    s1 = {1, 2, 3}
    s2 = {2, 3, 4}
    print(s1.intersection(s2))

# 3. Write a program to create an union of sets.
def set_q3():
    s1 = {1, 2, 3}
    s2 = {3, 4, 5}
    print(s1.union(s2))

# 4. Write a program to find the maximum and minimum value in a set.
def set_q4():
    s = {10, 20, 5, 40}
    print("Max:", max(s))
    print("Min:", min(s))

if __name__ == "__main__":
    set_q1()
