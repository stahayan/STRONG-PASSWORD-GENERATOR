import random
import string

numbers = string.digits
symbols = string.punctuation
lowercases = string.ascii_lowercase
uppercases = string.ascii_uppercase
all_chars = [numbers, symbols, lowercases, uppercases]

password = ""

for j in range(4):
    for i in range(3):
        password += all_chars[j][random.randint(0, 9)]

password = list(password)
random.shuffle(password)

new_pass = ""
new_pass = new_pass.join(password)

print ("Your password:" + (new_pass))