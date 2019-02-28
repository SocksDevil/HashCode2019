from Gallery import Gallery, Photo
from  Submission import Submission, Slide


def greedy(gl: Gallery, filename: str):
    submissions = []
    for i in gl.gallery:
        submissions.append(Slide([i]))

    s = Submission(submissions)
    s.submit(filename)

