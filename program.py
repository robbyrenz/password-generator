# A program I made on Friday, the 13th, 2019, that generates 20 character-length passwords

import random


def main():
    """The main function of the program"""
    blueprint = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!<>?@#$%^&*()-_=+"
    length = 20  # the length of the password
    password = password_maker(blueprint, length)
    answer(password)


def password_maker(blueprint, length):
    """makes the password according to the length specified"""
    password = ""
    while length > 0:
        char = random.choice(blueprint)  # choose a random letter from letters
        password = password + char  # append it to password
        length = length - 1
    return password


def answer(password):
    """prints out the result of the password to the user"""
    print()
    print("Here is your random password:")
    print(password)
    print()
    print("*****Program Ended*****")
    print()


# call main
if __name__ == "__main__":
    main()
