class User():
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.bucketlists = []
        print(self)
    
    def login(self, password):
        if self.password == password:
            return True
        else:
            return False
    
    def __eq__(self, other):
        if self.email == other.email:
            return True
        else:
            return False

    

