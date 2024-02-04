class User:
    def __init__(self, username, country) -> None:
        self.username = username
        self.country = country

    def get_user(self):
        return f"Hello {self.username} from {self.country}"


if __name__ == "__main__":
    john = User("John", "USA")
    print(john.get_user())

