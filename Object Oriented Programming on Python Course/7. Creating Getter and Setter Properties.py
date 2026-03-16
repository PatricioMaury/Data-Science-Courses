# Accessing and Modifying Data:
# 2. The Pythonic Way: Use Properties to Create Getter and Setter Methods.

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    @property
    def email(self):
        print("Email accessed")
        return self._email
    
    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email

user1 = User("dantheman", "dan@gmail.com", "123")
# user1.email = "This is not an email"
print(user1.email)
