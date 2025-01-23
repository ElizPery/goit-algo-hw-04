def merge_k_lists(arr):
    if len(arr) <= 1:
        return arr
    
    result = arr[:]
    while len(result) > 1:
        merge_res = merge(result[0], result[1])
        result.pop(1)
        result.pop(0)
        result.insert(0, merge_res)
    return result[0]

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Merge smaller elements first
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # If there are elements in the left or right half,
        # add them to the result
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

lists = [[9, 10], [1, 4, 5], [1, 3, 4], [2, 6], [6, 7, 8]]
merged_list = merge_k_lists(lists)
print("Sorted list:", merged_list)
