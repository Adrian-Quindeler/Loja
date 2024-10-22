def MostrarProdutos(listaDeProdutos):
    print("\nPRODUTOS:")
    for i in range(len(listaDeProdutos)):
        if listaDeProdutos[i][0] < 10:
            print(f"   {listaDeProdutos[i][0]}  {listaDeProdutos[i][1]:.<29}", end = "")
        else:
            print(f"   {listaDeProdutos[i][0]} {listaDeProdutos[i][1]:.<29}", end = "")
        if listaDeProdutos[i][2] < 100:
            print(f"..{listaDeProdutos[i][2]:.2f}")
        elif listaDeProdutos[i][2] < 1000:
            print(f".{listaDeProdutos[i][2]:.2f}")
        else:
            print(f"{listaDeProdutos[i][2]:.2f}")

def MostrarEspecificações(Especificações, listaDeProdutos):
    print("\nDigite o número do produto para ver as especificações."
          "\nDigite 0 para terminar.\n")
    while True:
        try:
            desejo = int(input("\nnúmero produto: "))
            if desejo == 0:
                break
            elif desejo < 0:
                print("Apenas números maiores que 0\n")
            else:
                for i in range(len(listaDeProdutos)):
                    if desejo == listaDeProdutos[i][0]:
                        print(f"\nEspecificação de {listaDeProdutos[i][1]}:")
                        print(f"    {Especificações[i]}")
                        break
                else:
                    print("Produto não encontrado.\n")
        except:
            print("digite apenas números, e apenas inteiros: \n")

def AdicionarItem(carrinho, listaDeProdutos):
    MostrarProdutos(listaDeProdutos)
    print("\nDigite o número do produto que deseja adicionar."
          "\nDigite 0 para terminar.\n")
    while True:
        try:
            desejo = int(input("Qual produto deseja? "))
            if desejo == 0:
                break
            elif desejo < 0:
                print("Apenas números maiores que 0\n")
            else:
                for i in range(len(listaDeProdutos)):
                    if desejo == listaDeProdutos[i][0]:
                        carrinho.append(listaDeProdutos[i])
                        print(f"{listaDeProdutos[i][1]} Adicionado(a) ao carrinho!\n")
                        break
                else:
                    print("Produto não encontrado.\n")
        except:
            print("digite apenas números\n")

def RemoverItem(carrinho):
    MostrandoCompra(carrinho)
    if len(carrinho) == 0:
        print("\nO carrinho está vazio.")
    else:    
        print("\nDigite o número do produto que deseja remover."
            "\nDigite 0 para terminar.\n")
        while True:
            try:
                desejo = int(input("Qual produto deseja remover? "))
                if desejo == 0:
                    break
                elif desejo < 0:
                    print("Apenas números maiores que 0\n")
                else:
                    for i in range(len(carrinho)):
                        if desejo == carrinho[i][0]:
                            print(f"{carrinho[i][1]} Removido(a) do carrinho!\n")
                            carrinho.remove(carrinho[i])
                            break
                    else:
                        print("Produto não encontrado.\n")
            except:
                print("digite apenas números\n")

def MostrandoCompra(carrinho):
    total = 0
    carrinho.sort()
    print(f"Seu carrinho:")
    for i in range(len(carrinho)):
        total += carrinho[i][2]
        if carrinho[i][0] < 10:
            print(f"   {carrinho[i][0]}  {carrinho[i][1]:.<29}", end = "")
        else:
            print(f"   {carrinho[i][0]} {carrinho[i][1]:.<29}", end = "")
        if carrinho[i][2] < 100:
            print(f"..{carrinho[i][2]:.2f}")
        elif carrinho[i][2] < 1000:
            print(f".{carrinho[i][2]:.2f}")
        else:
            print(f"{carrinho[i][2]:.2f}")
    print(f"   {'O valor total é:':.<32}", end = "")
    if total < 100:
        print(f"..{total:.2f}")
    elif total < 1000:
        print(f".{total:.2f}")
    else:
        print(f"{total:.2f}")

def FinalizarCompra(CEP, carrinho, nome, email):
    if len(carrinho) == 1:
        print(f"Obrigado por comprar na Adrian's & Adrian's {nome},"
        f"\nQualquer novidade, enviaremos para o email: {email}."
        f"\nO produto chegará no CEP informado em até 30 dias."
        "\nAgradecemos sua visita.")
    else:
        print(f"Obrigado por comprar na Adrian's & Adrian's {nome},"
        f"\nQualquer novidade, enviaremos para o email: {email}."
        f"\nOs produtos chegarão no CEP informado em até 30 dias."
        "\nAgradecemos sua visita.")
