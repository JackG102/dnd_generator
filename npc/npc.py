from pathlib import Path
import os
import random

class Npc:
  def __init__(self):
    self.first_name = ''
    self.assign_last_name() 
    self.assign_gender()
    self.assign_race()
    self.assign_vocation()
  
  def assign_gender(self):
    gender_list = ['male', 'female', 'non-binary']
    self.gender = random.choice(gender_list)

  def assign_last_name(self):
    last_name_list_file = open(os.path.join(os.path.dirname(__file__), 'last_name.txt'))
    lines = last_name_list_file.read().splitlines() 
    self.last_name = random.choice(lines)

  def assign_race(self):
    race_list_file = open(os.path.join(os.path.dirname(__file__), 'race.txt'))
    lines = race_list_file.read().splitlines() 
    self.race = random.choice(lines)

  def assign_vocation(self):
    vocation_list_file = open(os.path.join(os.path.dirname(__file__), 'vocation.txt'))
    lines = vocation_list_file.read().splitlines() 
    self.vocation = random.choice(lines)  

testNPC = Npc()
print(testNPC.gender)
print(testNPC.race)
print(testNPC.last_name)
print(testNPC.vocation)