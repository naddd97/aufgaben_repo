import random 

versuche_max = 5
versuche =  0

random_zahl= random.randrange(1, 20)


while versuche < versuche_max :

    user_guees= int(input('Eine erratene Zahl geben (vom 1 bis 20):'))

    if  user_guees==random_zahl: 
        print ('gut geraten !') 
        versuche += 5

    elif user_guees - random_zahl in [1,2, 3]:
        print ('Du bis 1 oder 2 oder 3 ziffern entfernt von der richtige lösung ')
        versuche += 1

    elif user_guees < random_zahl :
        print ('Zu klein ! Großere Zahl geben !')
        versuche += 1
        

    elif user_guees > random_zahl :
        print ('Zu Groß ! kleinere Zahl geben !')
        versuche += 1


