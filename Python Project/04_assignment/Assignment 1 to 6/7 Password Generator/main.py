import random

print("Welcome To Your Password Generator")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRTUVWXYZ!@$%^&*().,?0123456789'

number = int(input('Amount of passwords to gererate: '))

length = int(input('Input Your password length: '))

print('\nhere are your password: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
