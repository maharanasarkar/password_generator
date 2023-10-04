import random


lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
sp_char = "!@#$%^&*()<>?:;"


def GeneratePassword():
    string = lower + upper + number + sp_char
    length = 25
    password = "".join(random.sample(string, length))


    print(password)


GeneratePassword()

