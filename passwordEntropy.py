import math

class PasswordEntropy:
    def __init__(self, password):
        self.password = password

    def entropy(self):
        possible_chars = 0
        if self.count_lowercase() > 0:
            possible_chars += 26
        if self.count_uppercase() > 0:
            possible_chars += 26
        if self.count_integers() > 0:
            possible_chars += 10
        if self.count_special() > 0:
            possible_chars += 32

        password_length = len(self.password)
        entropy = password_length * math.log(possible_chars, 2)
        return entropy

    def count_lowercase(self):
        return sum(1 for c in self.password if c.islower())

    def count_uppercase(self):
        return sum(1 for c in self.password if c.isupper())
    
    def count_integers(self):
        return sum(1 for c in self.password if c.isdigit())

    def count_special(self):
        return sum(1 for c in self.password if not c.isalnum() and not c.isspace())