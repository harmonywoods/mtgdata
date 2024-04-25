'''
input stuff
will put more words here later
'''
import csv
filename = input("what file should this info be put into?")
opp = input("Opponent Name:")
format = input("Format:")
selfdeck = input("Your Deck (Use Guild/Shard names):")
oppdeck = input("Opponent Deck (Use Guild/Shard names):")
event = input("Event:")
result = input("Game Results e.g. WLW:")
notes = input("Notes:")
info = ",".join([opp,format,selfdeck,oppdeck,event,result,notes])
with open(filename, mode = 'a') as datafile:
    print(info, file=datafile)