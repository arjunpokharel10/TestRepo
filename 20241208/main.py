class Container:

    def __init__(self, items):
        self.items = items.split(',')

    
    def display_items(self):
        print(''.join(self.items))

    def __len__(self):
        return len(self.items)


china_to_us_container = Container('iphone, charger')
nepal_to_us_container = Container('carpet, pasmita')

print(china_to_us_container)

