from Gallery import Gallery, Photo
from  Submission import Submission, Slide
from objectiveFuncs import *


def greedy(gl: Gallery, filename: str):
    submissions = []
    gallery = gl.gallery
    while(len(gallery) > 0):
        current_photo = gallery[0]
        current_index = 0
        gallery.pop(0)
        current_points = 0
        for i in range(0, len(gallery)):
            if calc_points(gallery[i].tags, current_photo.tags) > current_points:
                current_index = i
        submissions.append(Slide([current_photo.id]))
        submissions.append(Slide([gallery[current_index].id]))
        gallery.pop(current_index)


    return submissions

