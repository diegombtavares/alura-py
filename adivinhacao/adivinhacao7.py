#Adicão de números aleatórios
import random
print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

#Geração de um numero randomico de 1 a 100 utilizando o randrange
numero_secreto = random.randrange(1,101)
total_de_tentativas = 3

print(numero_secreto)

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

    #Declaração variável boas práticas
    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    #Testa se o valor inserido é igual ao numero pré selecionado
    if (acertou):
        print("Você acertou!")
        break #Termina a interação do for
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o numero secreto")
        if(menor):
            print("Você errou! O seu chute foi menor que o numero secreto")

    rodada = rodada + 1

print("Fim do jogo")