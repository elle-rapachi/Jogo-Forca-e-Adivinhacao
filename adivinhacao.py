import random

def jogar():
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")

    numero_secreto = round(random.randrange(1,101)) #gerando números entre 1 e 100
    total_de_tentativas = 0
    pontos = 1000

    print("Escolha o nivel de dificuldade")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Escolha o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    #usando for
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite seu número: "))
        print("Você digitou ", chute)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(chute < 1 or chute > 100):
            print("Por favor, digite um valor entre 1 e 100!")
            continue

    # usando while
    #rodada = 1

    #while (rodada <= total_de_tentativas ):
    #    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    #    chute = int(input("Digite seu número: "))
    #    print("Você digitou ", chute)

    #    acertou = chute == numero_secreto
    #    maior = chute > numero_secreto
    #    menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos! ".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O número é maior que número secreto.")
            elif(menor):
                print("Você errou! Seu número é menor que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos


    print("Fim de jogo!")

if(__name__ == "__main__"):
 jogar()