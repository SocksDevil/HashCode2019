# import numpy as np
#
# var = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(var)

import sys
import Gallery

vertical_photos = Gallery.Gallery()
horizontal_photos = Gallery.Gallery()

with open(sys.argv[1]) as input_file:
    num_photos = input_file.readline()

    id = 0
    for line in input_file:
        [orientation, num_tags, tags] = line.rstrip().split(" ", 2)
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


        if orientation == 'H':
            horizontal_photos.gallery.append(Gallery.Photo(id, orientation, num_tags, tags))
        elif orientation == 'V':
            vertical_photos.gallery.append(Gallery.Photo(id, orientation, num_tags, tags))
def intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))

        id += 1

    print(horizontal_photos.gallery)
    print(vertical_photos.gallery)


def exclusive(arr1, arr2):
    return list(set(arr1) - set(arr2))


def calc_points(tags1, tags2):
    return min(len(intersection(tags1, tags2)), len(exclusive(tags1,tags2)), len(exclusive(tags2, tags1)))



