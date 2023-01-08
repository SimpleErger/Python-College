def bubble_sort(items):
    for i in range(len(items) - 1):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items
items = [5, 2, 3, 1, 4]
print(bubble_sort(items))  # prints [1, 2, 3, 4, 5]
# Bubble sort has a time complexity of O(n^2) in the worst case and 0(n) in the best case