import string
import random
valid=0
while valid==0:
    plaque=''
    plaque += random.choice(string.ascii_uppercase)
    plaque += random.choice(string.ascii_uppercase)
    plaque+='-'
    plaque+= str(random.randrange(1, 10))
    plaque+= str(random.randrange(1, 10))
    plaque+= str(random.randrange(1, 10))
    plaque+='-'
    plaque += random.choice(string.ascii_uppercase)
    plaque += random.choice(string.ascii_uppercase)
    if 'I' in plaque or 'O' in plaque or 'U' in plaque or 'SS' in plaque:
        valid=0
    else:
        valid=1
print (plaque)
