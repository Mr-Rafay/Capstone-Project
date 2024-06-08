#inventory.py
# from map import Map

class clues: 
  
  def __init__(self, name, description, found=False):
   self.name = name
   self.description = description
   self.found = found 

  def find_clues(self):
    self.found = True 
    print(f"you have found a clue: {self.name} - {self.description}")


  def examine_clue(self):
    if self.found:
      print(f"Examining {self.name}: {self.description}")
    else:
      print("You havent found this clue yet")


class cluecollection:
  def __init__(self):
    self.clues = [
      Clues("Fingerprint Kit", "A used to collect finger prints from crime scenes")
      Clues()
      
    ]


  def find_specific_clue(self, clue_name):
    for clue in self.clues:
      if clue.name == clue_name:
        clue.find_clue()
        break


  def examine_specific_clue(self, clue_name):
    for clue in self.clues:
      if clue.name == clue_name:
        clue.examine_clue()
        break
    