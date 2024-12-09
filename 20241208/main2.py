USERS = []

class User:
    def __init__(self, name, password, email, phone=None):
        from random import randint
        self.id = randint(1, 1000)
        self.first_name = name.split(' ')[0]
        self.last_name = name.split(' ')[1]
        self.password = password + '_secret'    #hashing
        self.email = email
        self.phone = phone

        user_data = {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password': self.password,
            'email': self.email,
            'phone': self.phone
        }
        USERS.append(user_data)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
arjun = User('Arjun Pokharel','Password00&&' ,'arjunpokharel10@gmail.com')

print(arjun)
