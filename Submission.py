class Submission:
    def __init__(self, slide_show):
        self.slide_show = slide_show

    def submit(self, filename):
        with open(filename, "w") as output_file:
            output_file.write(str(len(self.slide_show)) + "\n")

            for i in self.slide_show:
                for j in i.id:
                    output_file.write(str(j))
                    output_file.write(" ")
                output_file.write("\n")

        # f = open(filename, "w")
        # f.write(str(len(self.slide_show)))
        # f.write("\n")
        # for i in self.slide_show:
        #     for j in i.IDs:
        #         f.write(str(j))
        #         f.write(" ")
        #     f.write("\n")


class Slide:
    def __init__(self, IDs, tags):
        self.id = IDs
        self.length = len(IDs)
        self.tags = tags
