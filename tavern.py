import os
import random
from pathlib import Path
from Npc import Npc

class Tavern:
  project_location = str(Path(__file__).parent)
  lists_folder_location = project_location + '/lists/'

  def __init__(self):
    self.assign_name()
    self.assign_tavern_keeper()
    self.assign_tavern_npcs()

  def assign_name(self):
    adjective_list_file = open(os.path.join(os.path.dirname(self.lists_folder_location), 'adjectives.txt'))
    adjective_lines = adjective_list_file.read().splitlines() 
    adjective_name = random.choice(adjective_lines)

    animal_list_file = open(os.path.join(os.path.dirname(self.lists_folder_location), 'animals.txt'))
    animal_lines = animal_list_file.read().splitlines() 
    animal_name = random.choice(animal_lines)

    self.name = f"{adjective_name.capitalize()} {animal_name}"

  def assign_tavern_keeper(self):
    self.tavern_keeper = Npc()
  
  def assign_tavern_npcs(self):
    self.tavern_npcs = Npc.generate_npc(3)

  def assign_signature_dish(self):
    # TODO - add dish made of three ingredients with a funny name
  
  def describe(self):
    tavern_npc_text = ''
    for npc in self.tavern_npcs:
      tavern_npc_text += f"""
      Name: {npc.first_name} {npc.last_name}
      Race: {npc.race}
      Gender: {npc.gender}
      Vocation: {npc.vocation}
      Alignment: {npc.alignment}
      """
      
    print(
    f"""
  Tavern Name: {self.name}
  
  Tavern Keeper: {self.tavern_keeper.describe()}
  
  Tavern NPCS: {tavern_npc_text}
    """
    )

testTavern = Tavern()
testTavern.describe()

