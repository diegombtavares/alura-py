#Calculo de pontuação do jogo
import random

print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

#Geração de um numero randomico de 1 a 100 utilizando o randrange
numero_secreto = random.randrange(1,101)
total_de_tentativas = 0
pontos = 100

print("Qual nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Díficil")

nivel = int(input("Defina o nivel que deseja jogar: "))

#Seleção do nível de dificuldade
if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

#Enquanto o valor da rodada for menor que o numero de tentativas continua o laço
for rodada in range(1, total_de_tentativas + 1) :
    #String interpolation (format atribui os valores das variaveis dentro do {})
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    #input sempre armazina string
    chute_str = input("Digite um número de 1 a 100: ")
    print("Você digitou", chute_str)
    #transforma a variavel chute_str em int e atribui para chute
    chute = int(chute_str)

    #Verifia se o valor inserido está dentro de 1 a 100
    if(chute < 1 or chute >100):
        print("Você deve digitar um número entre 1 e 100")
        continue #Continua com a próxima interaçã do for lá em cima

    #Declaração das condições
    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    #Testa se o valor inserido é igual ao numero pré selecionado
    if (acertou):
        print("Você acertou e fez {} pontos!".format(pontos))
        break #Termina a interação do for
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o numero secreto")
        if(menor):
            print("Você errou! O seu chute foi menor que o numero secreto")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print("Fim do jogo")