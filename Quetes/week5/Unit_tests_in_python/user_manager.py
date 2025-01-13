class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, name, age):
        if name in self.users:
            raise ValueError("User already exists")
        self.users[name] = age

    def user_exists(self, name):
        return name in self.users

    def delete_user(self, name):
        if name not in self.users:
            raise ValueError("User not found")
        del self.users[name]
