def binary_search(arr, item):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = int((left + right) / 2)

        if arr[middle] == item:
            return True

        if arr[middle] > item:
            right = middle-1
        else:
            left = middle+1
    return False


def intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))


def exclusive(arr1, arr2):
    return list(set(arr1) - set(arr2))


def calc_points(tags1, tags2):
    return min(len(intersection(tags1, tags2)), len(exclusive(tags1,tags2)), len(exclusive(tags2, tags1)))



