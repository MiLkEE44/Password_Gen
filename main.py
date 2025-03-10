import random

# This is what is being randomly selected to create the password.  
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Input from the user. 
print("How long do you want your password to be?")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# string where the password where be store. 
password = []

# Loops where the range is between 0 and the user input. 
# Password.append(random choice(letters)) will randomly choose from the referenced list 
# and append it to the password list, it will add the amount the user ask for. 
for char in range (0, nr_letters):
    password.append(random.choice(letters))

for char in range (0, nr_symbols):
    password.append(random.choice(symbols))

for char in range (0, nr_numbers):
    password.append(random.choice(numbers))
    
# Random.shuffle(password) will shuffle the appended password list, 
# and .join will make the list a string again.
random.shuffle(password)
password = "".join(password)
print(f"This is your password: {password}")
