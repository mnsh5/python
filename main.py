class User:
    def __init__(self, username, city) -> None:
        self.username = username
        self.city = city

    def greeting(self):
        if self.username == "Jack Sparrow" and self.city == "London":
            print(f"Hello {self.username}! We are in {self.city}!")
        else:
            print("Are you Captain Barbosa?")

if __name__ == "__main__":
    user_instance = User("Jack Sparrow", "London")
    user_instance.greeting()

    user_instance2 = User("Will Turner", "St Martin")
    user_instance2.greeting()
