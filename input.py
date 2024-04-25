'''
input stuff
will put more words here later
'''
import csv
filename = input("what file should this info be put into?")
opp = input("Opponent Name:")
oppdeck = input("Opponent Deck (Use Guild/Shard names):")
result = input("Game Results e.g. WLW:")
notes = input("Notes:")
info = ",".join([opp,oppdeck,result,notes])
with open(filename, mode = 'a') as datafile:
    print(info, file=datafile)