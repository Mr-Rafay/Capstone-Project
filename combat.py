class Combat:
  def __init__(self, character1, character2):
      self.character1 = character1
      self.character2 = character2

  def attack(self, attacker, defender):
      """
      Simulate an attack from attacker to defender.
      """
      # Simple attack logic: 10% of current health as damage
      damage = max(1, int(0.1 * defender.health))
      defender.take_damage(damage)

  def combat_round(self):
      """
      A single round of combat where each character attacks once.
      """
      if self.character1.is_alive():
          self.attack(self.character1, self.character2)
      if self.character2.is_alive():
          self.attack(self.character2, self.character1)

  def combat_until_one_defeated(self):
      """
      Continue combat rounds until one of the characters is defeated.
      """
      while self.character1.is_alive() and self.character2.is_alive():
          self.combat_round()

      if not self.character1.is_alive():
          print(f"{self.character1.name} is defeated!")
      if not self.character2.is_alive():
          print(f"{self.character2.name} is defeated!")