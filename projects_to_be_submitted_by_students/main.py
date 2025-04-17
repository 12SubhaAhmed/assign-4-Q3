import random
import string

def generate_password(length):
    character = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(character) for _ in range(length))
    return password

length = int(input("Enter the desired password length: "))

if __name__ == '__main__':
    print("Generated password: ",generate_password(length))
