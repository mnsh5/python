class Cat:
    def __init__(self, name) -> None:
        self.name = name

    def meow(self):
        print(f"My 🐈 {self.name} said Meoowww")


if __name__ == "__main__":
    malala = Cat("Malala")
    malala.meow()

