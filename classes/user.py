class User():
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        #temporary to display bucketlists
        self.bucketlists = ["Sky Diving", "New Language", "Bungee Jumping"]
        print(self)

    def login(self, password):
        if self.password == password:
            return True
        else:
            return False
