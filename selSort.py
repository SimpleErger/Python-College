def selection_sort(items):
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if items[j] < items[min_index]:
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items
items = [5, 2, 3, 1, 4]
print(selection_sort(items))  # prints [1, 2, 3, 4, 5]
