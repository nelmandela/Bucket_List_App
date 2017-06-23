from classes.bucketlist import BucketList

class User():
    users = []
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.bucketlists = list()

    def login(self, password):
        if self.password == password:
            return True
        else:
            return False

    def create_bucketlist(self, name):
        new_bucketlist = BucketList(name)
        self.bucketlists.append(new_bucketlist)
        return 

