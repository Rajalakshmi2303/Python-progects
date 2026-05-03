import random
import string
print("password genrator")
length=int(input("enter password length;"))
characters=string.ascii_letters+string.numbers+string.punctuation
password=" "
for i in range(length):
    password+=random.choice(characters)
print("your password is;",password)