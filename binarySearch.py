def binary_search(items, target):
    low = 0
    high = len(items) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1
items = [1, 2, 3, 4, 5]

print(binary_search(items, 3))  # prints 2
print(binary_search(items, 6))  # prints -1