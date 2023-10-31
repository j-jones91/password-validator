import re

class PasswordValidator:
    def __init__(self):
        self.password = ""
    
    def input_password(self):
        self.password = input("Please enter a password: ")

    def is_valid(self):
        return (
            len(self.password) > 8 and
            bool(re.search(r'[A-Z]', self.password)) and
            bool(re.search(r'[a-z]', self.password)) and
            bool(re.search(r'[0-9]', self.password)) and
            "_" in self.password
        )

    def validate_password(self):
        self.input_password()
        if self.is_valid():
            return "Password is valid"
        else:
            return "Password is invalid."

if __name__ == "__main__":
    validator = PasswordValidator()
    print(validator.validate_password())
