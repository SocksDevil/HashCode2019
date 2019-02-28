class Gallery:
    def __init__(self):
        self.gallery = []


class Photo:
    def __init__(self, orientation, tags):
        self.orientation = orientation
        self.tags = tags

    def __repr__(self):
        print((self.orientation, len(self.tags), self.tags.split()))
