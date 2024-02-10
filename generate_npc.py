from Npc import *

number_of_npcs = input('How many NPCs do you want to generate? ')
number = 0
npc_list = []

while number < int(number_of_npcs):
  npc_list.append(Npc())
  number +=1

for npc in npc_list:
  npc.describe()
