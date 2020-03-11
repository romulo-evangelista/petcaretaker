from Pet import Pet

# Menu
class Menu:
  def __init__(self, entrada):
    self.entrada = entrada
    self.pet = Pet()
  
  def start(self):
    while(self.entrada != "exit"):   
      print("Para interagir, digite:")
      print("1 - Para ouvir o Pet")
      print("2 - Para alimentar o Pet")
      print("3 - Para brincar com o Pet")
      
      opcao = input()
      
      if opcao == "1":
        self.pet.falar()
      elif opcao == "2":
        self.pet.alimentar()
      elif opcao == "3":
        self.pet.brincar()
      else: 
        print("Opção inválida")
        
      self.entrada = input()
    
  def finish(): 
    print("Tchau!")