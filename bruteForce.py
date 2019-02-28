from Gallery import *
from Submission import *
from objectiveFuncs import  *
import random


def bruteforce(gl: Gallery):
    submissions = []
    original_length = len(gl.gallery)
    gallery = gl.gallery
    counter = 0
    while len(gallery) > 0 or counter > original_length:
        submissions.append(Slide([gallery[0].id], gallery[0].tags))
        random_index = random.randint(1, len(gallery) - 1)
        submissions.append(Slide([gallery[random_index].id], gallery[random_index].tags))
        gallery.pop(0)
        gallery.pop(random_index - 1)

    return submissions

def bruteforceV(gl: Gallery):
    photos = []
    submissions = []
    original_length = len(gl.gallery)
    gallery = gl.gallery
    counter = 0
    while len(gallery) > 0 or counter > original_length:
        random_index = random.randint(1, len(gallery) - 1)
        photos.append(Slide([gallery[random_index].id, gallery[0].id], list(set(gallery[random_index].tags) | set(gallery[random_index].tags))))
        gallery.pop(0)
        gallery.pop(random_index - 1)
    gallery = photos

    while len(gallery) > 0 or counter > original_length:
        submissions.append(Slide(gallery[0].id, gallery[0].tags))
        random_index = random.randint(1, len(gallery) - 1)
        submissions.append(Slide(gallery[random_index].id, gallery[random_index].tags))
        gallery.pop(0)
        gallery.pop(random_index - 1)
    return submissions


def randomizer(glV: Gallery, glH: Gallery):
    solutions = []
    points = -1
    best = None
    for _ in range(0, 10e3):
        solution = bruteforce(glH) + bruteforceV(glV)
        new_points = 0
        for i in range(0, len(solution) - 1):
            new_points+= calc_points(solution[i].tags, solution[i + 1].tags)
        if(new_points > points):
            points = new_points
            best = solution
    return best



