import random

class Game():
    def __init__(self):
        self.option = None
        self.__total = 0

    def menu(self):
        print("-------------Pedra, Papel e Tesoura-------------\n")
        print(f"(1) Pedra\n(2) Papel\n(3) Tesoura\n(0) Sair\nTotal de Vitorias: {self.__total}")
        
    def jogar(self):
        opt = int(input("Faça sua jogada: "))
        self.option = opt
    
    def main(self):
        while self.option != 0:
            self.menu()
            self.jogar()
            
            comp = random.randint(1, 3)
            #condições para vitória
            if self.option == 1 and comp == 3:
                print("A maquina jogou tesoura, você venceu!\n")
                self.__total += 1
                
            elif self.option == 2 and comp == 1:
                print("A maquina jogou pedra, você venceu!\n")
                self.__total += 1
                
            elif self.option == 3 and comp == 2:
                print("A maquina jogou papel, você venceu!\n")
                self.__total += 1
            
            #condições para derrota
            elif comp == 3 and self.option == 2:
                print("A maquina jogou tesoura, você perdeu!\n")
                
            elif comp == 1 and self.option == 3:
                print("A maquina jogou pedra, você venceu!\n")
                
            elif comp == 2 and comp == 1:
                print("A maquina jogou papel, você venceu!\n")
                
            #empate
            elif self.option == comp:
                print("Empate!")

            else:
                break
                
                
teste = Game()                
teste.main()

#pedra 1 > tesoura 3
#papel 2 > pedra 1
#tesoura 3 > papel 2