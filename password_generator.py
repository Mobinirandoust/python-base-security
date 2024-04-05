import random

liststring = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'l', 'k', 'j', 'h', 'g',
 'f', 'd', 's', 'a', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
liststrupper =['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'L', 'K', 'J', 'H', 'G',
 'F', 'D', 'S', 'A', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
listnumber = [0,1,2,3,4,5,6,7,8,9]
listevents = ["@", "#", "$", "&", "_", "!", "%"]

typeword = input("Type password: Hard or Normal or Easy?\n")
typeword = typeword.lower()

n = int(input("lengh password:\n "))
lengh = range(0 , n)


if typeword == "easy":
    i = liststring + listnumber
elif typeword == "normal":
    i = liststring + listnumber + listevents
elif typeword == "hard":
    i = liststring + listnumber + listevents + liststrupper


bin = []
a = 40
print("*"*a)

for me in lengh:
    mydrive = random.choice(i)
    print(mydrive)
    bin.append(str(mydrive))
    
print("*"*a)
print("*"*a)
print("Your password:" , "".join(bin) )
print("Your password:" , " ".join(bin) )

# Made with Mobin Iran Dost
