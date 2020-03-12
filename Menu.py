from Pet import Pet

# Menu
class Menu:
  def __init__(self, entrada):
    self.entrada = entrada
    self.pet = Pet()
  
  def start(self):
    while(self.entrada != "exit"):   

      self.pet.tempo()

      print("Para interagir, digite:")
      print("1 - Para ouvir o Pet")
      print("2 - Para alimentar o Pet")
      print("3 - Para brincar com o Pet")
      
      print(self.pet.humor)
      
      self.entrada = input()
      
      if self.entrada == "1":
        self.pet.falar()
      elif self.entrada == "2":
        self.pet.alimentar()
      elif self.entrada == "3":
        self.pet.brincar()
      else: 
        print("Opção inválida")

    
  def finish(self): 
    print("Tchau!")