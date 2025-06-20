import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
a=""
b=""
c=""
password_list=[]
for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    #a += random_char
    password_list.append(random_char)
# print(random_char)
for num in range(1, nr_numbers + 1):
    random_num = random.choice(numbers)
    #b += random_num
    password_list.append(random_num)
    #print(random_num)
for symbol in range(1, nr_symbols + 1):
    random_symbol = random.choice(symbols)
    #c+=random_symbol
    password_list.append(random_symbol)
    #print(random_symbol)
random.shuffle(password_list)
password = ''.join(password_list)
print(f"New Password: {password}")
