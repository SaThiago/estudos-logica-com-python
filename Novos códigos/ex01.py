# Definição de variáveis e listas
lista_compras = []  # Lista vazia para armazenar os itens
opcao = ""  # Variável para armazenar a escolha do usuário

print("Bem-vindo ao Gerenciador de Lista de Compras!")

# Loop para permitir múltiplas operações
while opcao != "4":
    print("\nEscolha uma opção:")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Exibir lista")
    print("4 - Sair")
    opcao = input("Digite o número da opção: ")

    if opcao == "1":  # Adicionar item
        item = input("Digite o nome do item para adicionar: ")
        lista_compras.append(item)  # Adiciona o item à lista
        print(f"'{item}' foi adicionado à lista!")
    
    elif opcao == "2":  # Remover item
        item = input("Digite o nome do item para remover: ")
        if item in lista_compras:
            lista_compras.remove(item)  # Remove o item da lista
            print(f"'{item}' foi removido da lista!")
        else:
            print(f"'{item}' não está na lista.")

    elif opcao == "3":  # Exibir lista
        if lista_compras:
            print("\nItens na sua lista de compras:")
            for i, item in enumerate(lista_compras, 1):
                print(f"{i}. {item}")
        else:
            print("Sua lista de compras está vazia.")
    
    elif opcao == "4":  # Sair
        print("Encerrando o programa. Até mais!")
    else:
        print("Opção inválida. Tente novamente.")