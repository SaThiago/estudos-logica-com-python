import textwrap

def criar_usuario(usuarios):
    """Cria um novo usuário (cliente) no sistema."""
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n*** Já existe um usuário com esse CPF! ***")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cpf_numeros = "".join(filter(str.isdigit, cpf))
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf_numeros, "endereco": endereco})
    print("\n=== Usuário criado com sucesso! ===")

def criar_conta(agencia, usuarios, contas):
    """Cria uma nova conta, vinculando a um usuário existente."""
    cpf = input("Informe o CPF do titular da conta: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        numero_conta = len(contas) + 1
        contas.append({
            "agencia": agencia, "numero_conta": numero_conta, "usuario": usuario,
            "saldo": 0.0, "n_saques": 0,
            "ultimo_dep": None, "ultimo_saq": None, "ultima_ope": None
        })
        print(f"\n=== Conta C/C: {numero_conta}, Ag: {agencia} criada com sucesso para {usuario['nome']}! ===")
        return

    print("\n*** Usuário não encontrado. Criação de conta falhou. ***")

def listar_contas(contas):
    """Exibe uma lista formatada de todas as contas."""
    if not contas:
        print("\nNenhuma conta cadastrada.")
        return
    print("\n================ LISTA DE CONTAS ================")
    for conta in contas:
        info_conta = f"""
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            Saldo:\t\tR$ {conta['saldo']:.2f}
        """
        print(textwrap.dedent(info_conta))
        print("-" * 50)

def filtrar_usuario(cpf, usuarios):
    """Função auxiliar para encontrar um usuário pelo CPF."""
    cpf_numeros = "".join(filter(str.isdigit, cpf))
    usuarios_filtrados = [u for u in usuarios if u["cpf"] == cpf_numeros]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def depositar(conta, /):
    """Executa o depósito na conta especificada."""
    valor = float(input("Digite o valor a ser depositado: "))
    while valor < 0:
        valor = float(input("Digite um valor válido: "))
    
    if valor > 0:
        conta['saldo'] += valor
        conta['ultimo_dep'] = valor
        conta['ultima_ope'] = 'd'
        print(f"Seu saldo é de: R$ {conta['saldo']:.2f}")
    else:
        print("Opção inválida. Tente novamente.")

def sacar(*, conta, limite_saques):
    """Executa o saque na conta especificada."""
    saldo = conta['saldo']
    n_saques = conta['n_saques']

    if n_saques < limite_saques:
        saque = float(input("Digite o valor a ser sacado: "))
        while saque < 0 or saque > saldo:
            if saque < 0:
                saque = float(input("Digite um valor válido: "))
            elif saque > saldo:
                saque = float(input("Saldo insuficiente. Digite um novo valor: "))
        
        if saque >= 0 and saque <= saldo:
            conta['saldo'] -= saque
            conta['ultimo_saq'] = saque
            conta['ultima_ope'] = 's'
            conta['n_saques'] += 1
            print(f"Seu saldo é de: R$ {conta['saldo']:.2f}")
            if (limite_saques - conta['n_saques'] > 0):
                print(f"Você ainda pode fazer {limite_saques - conta['n_saques']} saque(s) hoje.")
            else:
                print("Limite de saques por dia atingido!")
    else:
        print("Número de saques/dia atingido!")

def exibir_extrato(conta, /):
    """Exibe o extrato simples da conta especificada."""
    print("\n================ EXTRATO =================")
    print(f"Titular: {conta['usuario']['nome']}")
    print(f"Conta: {conta['numero_conta']}")
    print("-" * 40)

    if conta['ultima_ope'] == 'd':
        print(f"Último depósito: R$ {conta['ultimo_dep']:.2f}")
    elif conta['ultima_ope'] == 's':
        print(f"Último saque: R$ {conta['ultimo_saq']:.2f}")
    else:
        print("Não foram realizadas movimentações.")
    
    print(f"\nSaldo: R$ {conta['saldo']:.2f}")
    print("==========================================\n")

def main():
    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    
    opcoes = {
        'd': 'Depositar', 's': 'Sacar', 'e': 'Extrato',
        'nu': 'Novo Usuário', 'nc': 'Nova Conta', 'lc': 'Listar Contas',
        'q': 'Sair'
    }

    while True:
        entrada = input(textwrap.dedent("""
        Escolha uma opção:
            [d] Depositar      [nu] Novo Usuário
            [s] Sacar          [nc] Nova Conta
            [e] Extrato        [lc] Listar Contas
            [q] Sair
        Digite a opção desejada: """)).strip().lower()
        
        if not entrada or entrada not in opcoes:
            print("Opção inválida. Tente novamente.")
            continue
        
        opcao = entrada
        print(f"\nVocê escolheu: ({opcoes[opcao]})")

        if opcao == 'q':
            break
        elif opcao == 'nu':
            criar_usuario(usuarios)
        elif opcao == 'nc':
            criar_conta(AGENCIA, usuarios, contas)
        elif opcao == 'lc':
            listar_contas(contas)
        elif opcao in ['d', 's', 'e']:
            if not contas:
                print("\n*** Não há contas cadastradas para realizar operações. ***")
                continue
            
            num_conta_input = int(input("Informe o número da conta: "))
            conta_selecionada = next((c for c in contas if c["numero_conta"] == num_conta_input), None)

            if conta_selecionada:
                if opcao == 'd':
                    depositar(conta_selecionada)
                elif opcao == 's':
                    sacar(conta=conta_selecionada, limite_saques=LIMITE_SAQUES)
                elif opcao == 'e':
                    exibir_extrato(conta_selecionada)
            else:
                print("\n*** Conta não encontrada! ***")

# Ponto de Entrada do Programa
if __name__ == "__main__":
    main()