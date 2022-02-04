import forca
import adivinhacao

def escolha_jogo():
    print("Escolha seu jogo")
    print("********************************")

    print("(1) Forca (2) Adivinhação ")

    jogo = int(input("Escolha o jogo"))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogo adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolha_jogo()