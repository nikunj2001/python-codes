import random

Pswrd=input("Enter Your Password")
Pswrd=list(Pswrd)
print("".join(Pswrd))

random.shuffle(Pswrd)
print("".join(Pswrd))