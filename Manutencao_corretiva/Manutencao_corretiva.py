def mostrar_intro():
    print("\nBem-vindo à Aventura em Texto!")
    print("Você está em uma floresta escura. Uma trilha se estende ao norte e outra ao leste.")


def obter_comando():
    comando = input("\nPara onde você vai? (norte, sul, leste, oeste, sair): ").lower()
    return comando


def processar_comando(comando, localizacao):
    novo_local = localizacao  # Presume que o jogador fique na mesma localização, salvo indicação contrária.

    if comando == "norte":
        if localizacao == "floresta":
            novo_local = "cabana"
            print("\nVocê encontra uma cabana abandonada.")
        else:
            print("\nNão há caminho para o norte aqui.")
    elif comando == "leste":
        if localizacao == "floresta":
            novo_local = "rio"
            print("\nVocê chega a um rio de águas turbulentas.")
        else:
            print("\nNão há caminho para o leste aqui.")
    elif comando == "sul":
        if localizacao == "cabana":
            novo_local = "floresta"
            print("\nVocê retorna à floresta.")
        else:
            print("\nNão há caminho para o sul aqui.")
    elif comando == "oeste":
        if localizacao == "rio":
            novo_local = "floresta"
            print("\nVocê retorna à floresta.")
        else:
            print("\nNão há caminho para o oeste aqui.")
    elif comando == "sair":
        print("\nObrigado por jogar! Até a próxima!")
        return "sair", localizacao
    else:
        print("\nComando inválido. Tente novamente.")

    return comando, novo_local


def explorar_localizacao(localizacao, inventario):
    if localizacao == "cabana":
        print("\nDentro da cabana, você encontra uma chave enferrujada.")
        if "chave" not in inventario:
            inventario.append("chave")
            print("Você adicionou a chave ao seu inventário.")
    elif localizacao == "rio":
        print("\nHá uma ponte frágil sobre o rio.")
        if "chave" in inventario:
            print("Você usa a chave para destravar um mecanismo na ponte e atravessá-la.")
            localizacao = "tesouro"
            print("\nParabéns! Você encontrou um tesouro escondido!")
        else:
            print("Você precisa de uma chave para atravessar a ponte.")
    elif localizacao == "tesouro":
        print("\nVocê já está no tesouro. Aproveite sua conquista!")

    return localizacao, inventario


def jogar():
    localizacao = "floresta"
    inventario = []
    mostrar_intro()

    while True:
        comando = obter_comando()
        if comando == "sair":
            print("\nEncerrando o jogo. Até logo!")
            break
        comando, localizacao = processar_comando(comando, localizacao)
        if comando != "sair":  # Para evitar processar exploração após sair
            localizacao, inventario = explorar_localizacao(localizacao, inventario)


jogar()
