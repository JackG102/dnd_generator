import os
import random

class Npc:
  def __init__(self):
    self.assign_alignment()
    self.assign_gender()
    self.assign_first_name()
    self.assign_last_name()
    self.assign_race()
    self.assign_vocation()
  
  def assign_alignment(self):
    alignment_list = [
      'lawful good', 
      'neutral good', 
      'chaotic good', 
      'lawful neutral',
      'true neutral',
      'chaotic neutral',
      'lawful evil',
      'neutral evil',
      'chaotic evil'
    ]

    self.alignment = random.choice(alignment_list)

  def assign_first_name(self):
    list = ['first_name_male.txt', 'first_name_female.txt']

    if self.gender == 'male':
      first_name_list_file_name = list[0]
    elif self.gender == 'female':
      first_name_list_file_name = list[1]
    else:
      first_name_list_file_name = random.choice(list)

    first_name_list_file = open(os.path.join(os.path.dirname(__file__), first_name_list_file_name))
    lines = first_name_list_file.read().splitlines() 
    self.first_name = random.choice(lines)
  
  def assign_last_name(self):
    last_name_list_file = open(os.path.join(os.path.dirname(__file__), 'last_name.txt'))
    lines = last_name_list_file.read().splitlines() 
    self.last_name = random.choice(lines)
  
  def assign_gender(self):
    gender_list = ['male', 'female', 'non-binary']
    self.gender = random.choice(gender_list)

  def assign_race(self):
    race_list_file = open(os.path.join(os.path.dirname(__file__), 'race.txt'))
    lines = race_list_file.read().splitlines() 
    self.race = random.choice(lines)

  def assign_vocation(self):
    vocation_list_file = open(os.path.join(os.path.dirname(__file__), 'vocation.txt'))
    lines = vocation_list_file.read().splitlines() 
    self.vocation = random.choice(lines) 

  def describe(self):
    print(
    f"""
    Name: {self.first_name} {self.last_name}
    Race: {self.race}
    Gender: {self.gender}
    Vocation: {self.vocation}
    Alignment: {self.alignment}
    """
    )