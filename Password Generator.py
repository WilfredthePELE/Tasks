# This Project is about Password Generator

import random

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '^', '$', '*', '(', ')', '-', '_', '+', '|', ':', ';', '.', '?']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
           'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print("Welcome to Password Generator")
n_letters = int(input("How many Letters would you like in your password? \n"))  #4
n_symbols = int(input("How many Symbols would you like in your password? \n"))
n_numbers = int(input("How many Numbers would you like in your password? \n"))
password_list = []
for i in range(1, n_letters + 1):
    char = random.choice(letters)
    password_list = password_list + list(char)

for i in range(1, n_symbols + 1):
    sym = random.choice(symbols)
    password_list = password_list + list(sym)

for i in range(1, n_numbers + 1):
    num = random.choice(numbers)
    password_list = password_list + list(num)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(password)