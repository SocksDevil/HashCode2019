# import numpy as np
#
# var = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(var)

import sys
from Gallery import *
from Greedy import *
from sort import key

vertical_photos = Gallery()
horizontal_photos = Gallery()

with open(sys.argv[1]) as input_file:
    num_photos = input_file.readline()

    id = 0
    for line in input_file:
        [orientation, num_tags, tags] = line.rstrip().split(" ", 2)
        if orientation == 'H':
            horizontal_photos.gallery.append(Photo(id, orientation, num_tags, tags))
        elif orientation == 'V':
            vertical_photos.gallery.append(Photo(id, orientation, num_tags, tags))

        id += 1

    # print(horizontal_photos.gallery)
    # print(vertical_photos.gallery)

    horizontal_photos.gallery = sorted(horizontal_photos.gallery,key=key)
    vertical_photos.gallery = sorted(vertical_photos.gallery, key=key)

def binary_search(arr, item):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = int((left + right) / 2)

        if arr[middle] == item:
            return True

        if arr[middle] > item:
            right = middle - 1
        else:
            left = middle + 1
    return False




greedy(horizontal_photos, "submission.txt")
# greedy(vertical_photos)
