from Gallery import Gallery, Photo
from  Submission import Submission, Slide
from objectiveFuncs import *


def greedyV(gl: Gallery, filename: str):
    submissions = []
    gallery = gl.gallery
    while(len(gallery) > 0):
        current_photo = gallery[0]
        current_index = 0
        gallery.pop(0)
        current_points = 0
        photo = 0
        photo2 = 0
        for i in range(0, len(gallery) - 3):
            photo = Photo([current_photo.id, gallery[i].id], "V", len(current_photo.tags) + len(gallery[i].tags), current_photo.tags + gallery[i].tags)
            photo2 = Photo([gallery[i + 1].id, gallery[i + 2].id], "V", len(gallery[i+1].tags) + len(gallery[i + 2].tags), gallery[i + 1].tags + gallery[i + 2].tags)
            if calc_points(photo.tags, photo2.tags) > current_points:
                current_index = i
        submissions.append(Slide(photo.id))
        submissions.append(Slide(photo2.id))
        gallery.pop(current_index)


    return submissions

