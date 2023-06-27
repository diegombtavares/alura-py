#Adição do While
print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

#atribui um valor a variavel numero_secreto
numero_secreto = 42
total_de_tentativas = 3
rodada = 1 

#Enquanto o valor da rodada for menor que o numero de tentativas continua o laço
while(rodada <= total_de_tentativas):
    print("Tentativa", rodada, "de", total_de_tentativas)
    #input sempre armazina string
    chute_str = input("Digite o seu número: ")
    print("Você digitou", chute_str)
    #transforma a variavel chute_str em int e atribui para chute
    chute = int(chute_str)

    #Declaração variável boas práticas
    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    #Testa se o valor inserido é igual ao numero pré selecionado
    if (acertou):
        print("Você acertou")
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o numero secreto")
        if(menor):
            print("Você errou! O seu chute foi menor que o numero secreto")

    rodada = rodada + 1

print("Fim do jogo")
