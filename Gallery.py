class Gallery:
    def __init__(self):
        self.gallery = []


class Photo:
    def __init__(self, id, orientation, num_tags, tags):
        self.id = id
        self.orientation = orientation
        self.num_tags = num_tags
        self.tags = tags
        self.used = False

    def __repr__(self):
        return "({0}, {1}, {2}, {3})".format(self.id, self.orientation, self.num_tags, self.tags.split())
