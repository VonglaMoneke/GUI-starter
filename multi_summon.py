import random

money = 0
chars = ['Naruto','Bayonetta','Sasuke','Erza','Natsu']
owned =['Naruto','Sasuke']
x = random.randrange(0,4)
y = random.randrange(0,4)
z = random.randrange(0,4)
if chars[x] in owned:
    print('Already owned',chars[x])
    money = money+50
    print('You have been compensated 50 credits')
    print('New total is',money)
else:
    print('New charcter added',chars[x])
    owned.append(chars[x])
    print(owned)
if chars[y] in owned:
    print('Already owned',chars[y])
    money = money+50
    print('You have been compensated 50 credits')
    print('New total is',money)
else:
    print('New charcter added',chars[y])
    owned.append(chars[y])
    print(owned)
if chars[z] in owned:
    print('Already owned',chars[z])
    money = money+50
    print('You have been compensated 50 credits')
    print('New total is',money)
else:
    print('New charcter added',chars[z])
    owned.append(chars[z])
    print(owned)
