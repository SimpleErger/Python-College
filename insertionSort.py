def insertion_sort(items):
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j - 1]:
            items[j], items[j - 1] = items[j - 1], items[j]
            j -= 1
    return items
items = [5, 2, 3, 1, 4]
print(insertion_sort(items))  # prints [1, 2, 3, 4, 5]
# Insertion sort has a time complexity of O(n^2) in the worst case and 0(n) in the best case