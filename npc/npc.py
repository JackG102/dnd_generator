from pathlib import Path
import os
import random

class Npc:
  def __init__(self):
    self.first_name = ''
    self.assign_last_name() 
    self.assign_gender()
    self.race = ''
    self.vocation = ''

  def assign_last_name(self):
    last_name_list_file = open(os.path.join(os.path.dirname(__file__), 'last_name.txt'))
    lines = last_name_list_file.read().splitlines() 
    self.last_name = random.choice(lines)

  def assign_gender(self):
    gender_list = ['male', 'female', 'non-binary']
    self.gender = random.choice(gender_list)

testNPC = Npc()
print(testNPC.gender)
print(testNPC.last_name)