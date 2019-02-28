class Gallery:
    def __init__(self):
        self.gallery = []


class Photo:
    def __init__(self, orientation, num_tags, tags):
        self.orientation = orientation
        self.num_tags = num_tags
        self.tags = tags

    def __repr__(self):
        print((self.orientation, self.num_tags, self.tags.split()))
