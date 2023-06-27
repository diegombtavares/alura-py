def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da forca!***")
    print("*********************************")
    
    palavra_secreta = "python"
    
    enforcou = False
    acertou = False
    
    #Enquanto(True)
    while(not enforcou and not acertou):
        
        chute = input("Qual letra? ")
        
        index = 0 
        
        for letra in palavra_secreta:
            if(chute == letra):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1
        
        print("Jogando...")

    print("Fim do jogo")

#chama a função jogar
if(__name__ == "__main__"):
    jogar()