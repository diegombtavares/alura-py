#Primeiro código adivinhação
print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

#atribui um valor a variavel numero_secreto
numero_secreto = 42

#input sempre armazina string
chute_str = input("Digite o seu número: ")

print("Você digitou", chute_str)

#transforma a variavel chute_str em int e atribui para chute
chute = int(chute_str)

#Testa se o valor inserido é igual ao numero pré selecionado
print("Você acertou") if numero_secreto == chute else print("Você errou")

print("Fim do jogo")
