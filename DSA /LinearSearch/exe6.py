"""Linear search"""
def linear_search(arr, target):
    size = len(arr)
    for i in range(0, size):
        if arr[i] == target:
            return i
    return -1