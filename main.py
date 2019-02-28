from Submission import Submission
from Submission import Slide

slides = [Slide([0]), Slide([3]), Slide([1, 2])]

sub  = Submission(slides)

sub.submit("meias.txt")