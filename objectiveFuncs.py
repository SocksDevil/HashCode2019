def intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))

def exclusive(arr1, arr2):
    return list(set(arr1) - set(arr2))


def calc_points(tags1, tags2):
    return min(len(intersection(tags1, tags2)), len(exclusive(tags1, tags2)), len(exclusive(tags2, tags1)))
