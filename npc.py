import random

class Npc:
  def __init__(self, first_name, last_name, gender, race, vocation):
    self.first_name = first_name
    self.last_name = last_name
    self.gender = gender
    self.race = race
    self.vocation = vocation

  def assignGender(self):
    gender_list = ['male', 'female', 'non-binary']
    self.gender = random.choice(gender_list)

testNPC = Npc('Jack', 'Garratt', 'foo', 'human', 'developer')
print(testNPC.gender)
testNPC.assignGender()
print(testNPC.gender)