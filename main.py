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

        if orientation == 'H':
            horizontal_photos.gallery.append(Gallery.Photo(id, orientation, num_tags, tags))
        elif orientation == 'V':
            vertical_photos.gallery.append(Gallery.Photo(id, orientation, num_tags, tags))

        id += 1

    print(horizontal_photos.gallery)
    print(vertical_photos.gallery)
