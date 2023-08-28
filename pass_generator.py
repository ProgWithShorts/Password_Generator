import random
from string import punctuation, ascii_letters, digits


def generate_password(length):
    chars = punctuation + ascii_letters + digits
    password = []
    for _ in range(length):
        password.append(random.choice(chars))

    password = "".join(password)

    return password


password = generate_password(12)
print("Password--- ", password)
print("Length--- ", len(password))
