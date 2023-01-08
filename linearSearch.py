def linear_search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1
items = [1, 2, 3, 4, 5]

print(linear_search(items, 3))  # prints 2
print(linear_search(items, 6))  # prints -1