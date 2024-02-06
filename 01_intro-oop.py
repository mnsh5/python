class Cat:
    def __init__(self, name) -> None:
        self.name = name

    def meow(self):
        print(f"{self.name} says: Meoowww... 🐈")

if __name__ == "__main__":
    malala = Cat("Malala")
    malala.meow()
