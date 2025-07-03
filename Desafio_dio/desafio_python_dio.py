#
saldo = 0
n_saques = 0
limite_saques = 3
ultimo_dep = None
ultimo_saq = None
ultima_ope = None

opcoes = {'d': 'Depositar', 's': 'Sacar', 'e': 'Extrato', 'q': 'Sair'}

while True:
    entrada = input("""Escolha uma opção:
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    Digite a opção desejada: """).strip().lower()
    opcao = entrada[0]  
    if opcao in opcoes:
        print(f"Você escolheu: ({opcoes[opcao]})")
        if opcao == 'd':
            valor = float(input("Digite o valor a ser depositado: "))
            while valor < 0:
                valor = float(input("Digite um valor válido: "))
            if valor > 0:
                saldo = saldo + valor
                ultimo_dep = valor
                ultima_ope = 'd'
                print (f"Seu saldo é de: R$ {saldo:.2f}")
            else:
                print("Opção inválida. Tente novamente.")
        elif opcao == 's':
            if n_saques < limite_saques:
                saque = float(input("Digite o valor a ser sacado: "))
                while saque < 0 or saque > saldo:
                    if saque < 0:
                        saque = float(input("Digite um valor válido: "))
                    elif saque > saldo:
                        saque = float(input("Saldo insuficiente. Digite um novo valor: "))
                if saque >= 0 and saque <= saldo:
                    saldo = saldo - saque
                    ultimo_saq = saque
                    ultima_ope = 's'
                    n_saques = n_saques + 1
                    print(f"Seu saldo é de: R$ {saldo:.2f}")
                    if (limite_saques - n_saques > 1):
                        print(f"Você pode sacar mais {limite_saques - n_saques} vezes!")
                    elif (limite_saques - n_saques == 1):
                        print(f"Você pode sacar mais {limite_saques - n_saques} vez!")
                    else:
                        print("Limite de saques por dia atingido!")
                else:
                    print("Opção inválida. Tente novamente.")
            else:
                print("Número de saques/dia atingido!")
                continue         
        elif opcao == 'e':
            print("\n================ EXTRATO =================")
            if ultima_ope == 'd':   
                print(f"Último depósito: R$ {ultimo_dep:.2f}")
            elif ultima_ope == 's':
                print(f"Último saque: R$ {ultimo_saq:.2f}")
            else:
                print("Não foram realizadas movimentações.")
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================\n")                  
        elif opcao == 'q':
            break
    else:
        print("Opção inválida. Tente novamente.")



