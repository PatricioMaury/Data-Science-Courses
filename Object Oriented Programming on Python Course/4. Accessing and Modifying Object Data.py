class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def say_hi_to_user(self, user):
        print(
            f"Sending message to {user.username}: Hi {user.username}, it's {self.username}"
            )

user1 = User('DanTheMan', 'dan@gmail.com', '123')
user2 = User('Batman', 'bat@outlook.com', 'abc')

user2.say_hi_to_user(user1)

print(user1.email)
user1.email = 'danny'
print(user1.email)
