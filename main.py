class User:
    def __init__(self, username, city) -> None:
        self.username = username
        self.city = city

    def greeting(self):
        print(f"Hello {self.username} from {self.city}!")

class Pirate(User):
    def __init__(self, username, city, ship_name) -> None:
        super().__init__(username, city)
        self.ship_name = ship_name

    def pirate_greeting(self):
        print(f"Arrr! {self.username} aboard the {self.ship_name} in {self.city}!")

class Captain(Pirate):
    def __init__(self, username, city, ship_name, crew) -> None:
        super().__init__(username, city, ship_name)
        self.crew = crew

    def captain_greeting(self):
        print(f"Ahoy! I'm Captain {self.username} of the {self.ship_name}. Crew, assemble!")

if __name__ == "__main__":
    jack_sparrow = Captain("Jack Sparrow", "Caribbean", "Black Pearl", ["Gibbs", "Barbossa", "Will Turner"])
    jack_sparrow.captain_greeting()

    elizabeth_swann = Pirate("Will Turner", "Port Royal", "Interceptor")
    elizabeth_swann.pirate_greeting()
    elizabeth_swann.greeting()

