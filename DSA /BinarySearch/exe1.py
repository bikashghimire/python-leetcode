""" Binary search"""
# print(5 // 2)


def  binary_search(arr, target):
    size = len(arr) - 1
    start = 0
    end = size
    while (start <= end):
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

sorted_list = [10,23,35,45,50,70,85]
target = 50

result = binary_search(sorted_list, target)
print(result) # 4
