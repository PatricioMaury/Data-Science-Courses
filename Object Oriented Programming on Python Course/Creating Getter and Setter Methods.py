# Creating Getter and Setter Methods
# Accesing and Modifying Data:
# 1. The Traditional Way: Make the Data Private and Use Getters and Setters.

from datetime import datetime

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email # Protected attribute
        self.password = password

    def get_email(self):
        print(f"Email accessed at {datetime.now()}")
        return self._email # Getter method
    
    def set_email(self, new_email):
        if "@" in new_email:
            self._email = new_email # Setter method

user1 = User("DanTheMan", "dan@gmail.com", "123")
print(user1.get_email())

user1.set_email("danny@outlook.com")
print(user1.get_email())


