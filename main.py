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


def intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))


def union(arr1, arr2):
    return list(set(arr1) | set(arr2))


def exclusive(arr1, arr2):
    return list(set(arr1) - set(arr2))


def calc_points(tags1, tags2):
    return min(len(intersection(tags1, tags2)), len(exclusive(tags1, tags2)), len(exclusive(tags2, tags1)))


# horizontal_photos = greedy(horizontal_photos)
# vertical_photos = greedy(vertical_photos)
#
# sub = Submission(horizontal_photos + vertical_photos)

# BRUTEFORCE MANHOSO
slide_show = []
hori_total = len(horizontal_photos.gallery)
vert_total = len(vertical_photos.gallery)
used_vert = 0
inverted_vert = vertical_photos.gallery[::-1]
for i in range(hori_total):
    photo1 = horizontal_photos.gallery[i]
    tags1 = horizontal_photos.gallery[i].tags
    slide_show.append(Slide([photo1.id]))

    if used_vert == vert_total:
        continue

    for j in range(vert_total):
        photo2 = vertical_photos.gallery[j]
        if photo2.used:
            continue
        tags2 = vertical_photos.gallery[j].tags
        photo2.used = True

        for k in range(vert_total):
            photo3 = inverted_vert[k]
            if photo3.used:
                continue
            tags3 = inverted_vert[k].tags

            vert_union = union(tags2, tags3)
            if calc_points(tags1, vert_union) > 0:
                slide_show.append(Slide([photo2.id, photo3.id]))
                photo3.used = True
                used_vert += 2
                break
        break


sub = Submission(slide_show)
sub.submit("output.txt")