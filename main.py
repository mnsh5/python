class Cat:
    def __init__(self, catname, city) -> None:
        self.catname = catname
        self.city = city

    def greeting(self):
        print(f"Hello {self.catname} from {self.city}!")



if __name__ == "__main__":
    lola = Cat("Lola", "Catur City")
    lola.greeting()


