# Accesing and Modifying Data:
# 1. The Traditional Way: Make the Data Private and Use Getters and Setters.

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email # Protected attribute, __email would be private and it wouldn't be accessible outside the class.
        self.password = password

    def clean_email(self):
        return self._email.lower().strip()
    
user1 = User("DanTheMan", " Dan@gmail.com  ", "123")

print(user1._email) # Accessing a protected attribute directly (not recommended, but possible). 
# Double underscore for private attribute.
print(user1.clean_email())

