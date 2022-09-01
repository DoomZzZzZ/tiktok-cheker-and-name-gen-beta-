import random

chars = "abcdefghijklmnopqrstuvwxyz1234567890"

while 1:
    password_len = int(input("How many lettes should your username have : "))
    password_count = int(input("How many usernames do you want to create : "))
    for x in  range (0,password_count):
        password = ""
        for x in range(0,password_len):
                password_chars = random.choice(chars)
                password       = password + password_chars
        print("", password)