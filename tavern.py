import os
import random
import sys
from pathlib import Path
from npc import Npc

class Tavern:

  def __init__(self):
    self.assign_name()

  def assign_name(self):
    project_location = str(Path(__file__).parent.parent)
    lists_folder_location = project_location + '/lists/'

    adjective_list_file = open(os.path.join(os.path.dirname(lists_folder_location), 'adjectives.txt'))
    adjective_lines = adjective_list_file.read().splitlines() 
    adjective_name = random.choice(adjective_lines)

    animal_list_file = open(os.path.join(os.path.dirname(lists_folder_location), 'animals.txt'))
    animal_lines = animal_list_file.read().splitlines() 
    animal_name = random.choice(animal_lines)

    self.name = f"{adjective_name.capitalize()} {animal_name}"

    # def describe(self):
    #   print(
    #   f"""
    #   Name: {self.name}
    #   """
    #   )

testTavern = Tavern()
print(testTavern.name)

