import os
import random
from pathlib import Path
import Npc

class Tavern:
  project_location = str(Path(__file__).parent)
  lists_folder_location = project_location + '/lists/'

  def __init__(self):
    self.assign_name()
    self.assign_tavern_keeper()

  def assign_name(self):
    adjective_list_file = open(os.path.join(os.path.dirname(self.lists_folder_location), 'adjectives.txt'))
    adjective_lines = adjective_list_file.read().splitlines() 
    adjective_name = random.choice(adjective_lines)

    animal_list_file = open(os.path.join(os.path.dirname(self.lists_folder_location), 'animals.txt'))
    animal_lines = animal_list_file.read().splitlines() 
    animal_name = random.choice(animal_lines)

    self.name = f"{adjective_name.capitalize()} {animal_name}"

  def assign_tavern_keeper(self):
    self.bar_keeper = Npc()
  
  def assign_tavern_npcs(self):

    # def describe(self):
    #   print(
    #   f"""
    #   Name: {self.name}
    #   """
    #   )

testTavern = Tavern()
print(testTavern.name)

