class BucketList():
    bucketlists = {}

    def __init__(self, name):
        self.name = name
        self.finished = False

    def __repr__(self):
        return self.name
