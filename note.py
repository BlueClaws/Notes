#!usr/bin/python
import datetime
while(1):
    x = input(">")
    if(x[:].lower() == 'quit'):
        break;
    with open('MyNotes.txt', 'a') as f:
        f.write('[' + str(datetime.datetime.now()) + '] ' +  x + "\n")
