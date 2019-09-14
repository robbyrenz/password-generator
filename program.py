# A program I made on Friday, the 13th, 2019, that generates 20 char passwords

import random


def main():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!<>?"
    times = 20  # the length of the password
    password = ""

    while times > 0:
        letter = random.choice(letters)  # choose a random letter from letters
        password = password + letter  # append it to password
        times = times - 1

    print()
    print("Here is your random password:")
    print(password)
    print()
    print("*****Program Ended*****")
    print()


# call main
if __name__ == "__main__":
    main()
