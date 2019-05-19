import random

en_team = []
chars = ['Naruto','Bayonetta','Sasuke','Erza','Natsu']



while len(en_team) != 3:
    x = random.randrange(0,5)
    while chars[x] not in en_team:
        en_team.append(chars[x])

owned1 = ', '.join(en_team)
text = "The enemy's team is " + owned1

print(text)
