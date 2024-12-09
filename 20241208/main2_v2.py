USERS = []

class User:
    def __init__(self, name, password, email, phone=None):
        from random import randint

        self.id = randint(1, 1000)
        self.first_name = name.split(' ')[0]
        self.second_name = name.split(' ')[-1]
        self.password = password + '_secret'        #hashing

        
        