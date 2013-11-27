#!/usr/bin/env python
#from acb import stats
import time, csv, acb

player = ['B2H','A1O']   
#player = ['A1O']       
    
file_source = open('players2.csv','r')
players = ['XXX'] 

for linea in file_source:
    id = linea.split(';')[3]
    players.append(id)    

# ['XXX', 'id_acb',

for x in players[2:]:
    data = acb.stats(x)
    time.sleep(0.3)
    out = csv.writer(open("players3.csv","a"), delimiter=',')
    out.writerow(data)
#    print data
    
file_source.close()
