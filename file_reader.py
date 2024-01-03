link = input('Bitte gebe das Link von der Text Datei ')

datei = open(link, 'rt')

for line in datei : 

    lin=line.split()
    anzahl =len(lin) 
print (anzahl)
    