import random
import string

 
list_words =('Orange','Porsche','Donald Trump')


wort = random.choice(list_words)
ints=  str((random.randint(32, 126)))

with open('text.txt','w') as file :

    file.write(wort)
    file.write(ints)
    
