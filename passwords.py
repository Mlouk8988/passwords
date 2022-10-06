

  
# Passwords progrmme 

import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u' ,'v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the programme passwords  :\n")

n_letters = int(input("how mant laters you want in your password ?\n"))
n_symbols = int(input(f"how many symbols would you like ?\n "))
n_numbers = int(input(f"how many numbers would you like ?\n"))

password = []
for N in range(1,n_letters + 1) :
  password.append(random.choice(letters))
  
for N in range(1,n_symbols + 1) :
  password += random.choice(symbols)
  
for N in range(1,n_numbers + 1) :
  password += random.choice(numbers)

print(password) 
random.shuffle(password)
print(password)
mode = ""
for char in password :
  mode += char

print(f"your password is : {mode}")
  
  





