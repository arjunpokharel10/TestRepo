class FootballPlayer:
    def __init__(self, name, age, club, position):
        self.name = name
        self.age = age
        self.club = club
        self.position = position

    def display_player(self):
        print(f"{self.name} plays with {self.club}.")



ronaldo = FootballPlayer("Christiano Ronaldo", 36, "Manchester United", "Striker")
neymar = FootballPlayer("Neymar Junior", 29, "Manchester City", "Striker")

ronaldo.display_player()
neymar.display_player()