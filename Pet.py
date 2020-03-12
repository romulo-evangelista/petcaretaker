# Pet
class Pet:
  def __init__(self): 
    # pet's fome and tedio initalize with 0
    self.fome = 0
    self.tedio = 0
    
    # humor
    self.humor = self.fome + self.tedio
  
  # return humor's level
  def humorLevel(self):
    if self.humor <= 5:
      return "Estou feliz :D"
    elif self.humor > 5 and self.humor <= 10:
      return "Estou ok :)"
    elif self.humor > 10 and self.humor <= 15:
      return "Estou frustrado :/"
    elif self.humor > 15:
      return "Estou deprimido :("
    else: 
      return "Humor não setado"
 
  # Pet talk
  def falar(self):
    print(self.humorLevel())    
  
  # Pet food
  def alimentar(self):
    if self.fome < 4: 
      self.fome = 0
    else:
      self.fome -= 4
    
  # Pet play
  def brincar(self):
    if self.tedio < 4:
      self.tedio = 0
    else:
      self.tedio -= 4
      
  def tempo(self):
    self.fome += 1
    self.tedio += 1
    self.humor = self.fome + self.tedio
    