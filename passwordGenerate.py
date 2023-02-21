import random
import string

class Generator:
    def __init__(self, length):
        self.length = length
        

    def generate_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(self.length))
        return password

    def check_special_characters(self,password:str)->bool:
        special_char = string.punctuation
        for char in password:
            if char in special_char:
                return True
        return False