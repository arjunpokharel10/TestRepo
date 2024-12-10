# create a class called father
# create a class called son which inherits from father
# son should inherit bank balance method from father
# son should override habit method


class Father:
    def __init__(self):
        print('i am your father')

    def balance(self):
        print('bank balance: 100')
    
    def habit(self):
        print('sleeping, eating, running, training')


class Son(Father):
    def __init__(self):
        print('i am your son')

    def habit(self):
        print('training', 'running', 'coding')



son1 = Son()
print(son1.balance())
print(son1.habit())