name = input('Name der Datei')

wünsch_txt = input('schreibe deinen wünsch txt')

with open (name,'w') as fw:

    fw.write(wünsch_txt)


