# 1. Add a key and value to a dictionary.
def dict_q1():
    d = {0: 10, 1: 20}
    d[2] = 30
    print(d)

# 2. Concatenate following dictionaries to create a new one.
def dict_q2():
    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50, 6:60}
    dic4 = {}
    for d in (dic1, dic2, dic3): dic4.update(d)
    print(dic4)

# 3. Check if a given key already exists in a dictionary.
def dict_q3(d, key):
    return key in d

# 4. Iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values.
def dict_q4():
    d = {'a': 1, 'b': 2, 'c': 3}
    print("Keys:")
    for k in d.keys(): print(k)
    print("Values:")
    for v in d.values(): print(v)
    print("Both:")
    for k, v in d.items(): print(k, v)

# 5. Prepare a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of the keys.
def dict_q5():
    d = {i: i**2 for i in range(1, 16)}
    print(d)

# 6. Sum all the values in a dictionary, considering the values will be of int type.
def dict_q6():
    d = {'a': 100, 'b': 200, 'c': 300}
    print(sum(d.values()))

if __name__ == "__main__":
    dict_q1()
