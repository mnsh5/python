class Cat:
    def __init__(self) -> None:
        self.cats = []

    def __len__(self):
        return len(self.cats)

    def __getitem__(self, i):
        return self.cats[i]

    def __repr__(self):
        return f'<Cat {self.cats}>'

    def __str__(self):
        return f'<Cat with {len(self)} cats.>'

if __name__ == "__main__":
    malala = Cat()
    malala.cats.append("Malala")
    malala.cats.append("Lola")
    malala.cats.append("Uali")
    print(len(malala))

    print(malala.__getitem__(1))
    print(malala.__repr__())
    print(malala.__str__())
