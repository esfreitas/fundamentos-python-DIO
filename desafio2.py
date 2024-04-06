import textwrap

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar novo usuário
[5] Criar conta
[6] Exibir contas
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"

usuarios = []
contas = []
numero_conta = 1

def depositar(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
            print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("informe o CPF para cadastro: ")
    usuario = buscar_usuario(cpf, usuarios)

    if usuario:
        print("\n Usuário já existe.")
        return
    
    nome = input("informe o nome para cadastro: ")
    data_nascimento = input("informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("informe o endereco (rua, numero - bairro - cidade/UF): ")

    usuarios.append({"nome": nome, "cpf": cpf, "endereco": endereco, "data_nascimento": data_nascimento})
    print("cadastro concluído com sucesso")

def buscar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("informe o CPF do usuário: ")
    usuario = buscar_usuario(cpf, usuarios)

    if usuario:
       print("\n Conta criada com sucesso.")
       return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não localizado, conta não pode ser cadastrada")

def exibir_contas(contas):
    for conta in contas:
        linha = f"""
        Agência:\t{conta['agencia']}
        C/C: \t\t{conta['numero_conta']}
        titular:\t\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato,)

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES,)
        
    elif opcao == "3":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "4":
       criar_usuario(usuarios)
    
    elif opcao == "5":
       conta = criar_conta(AGENCIA, numero_conta, usuarios)

       if conta:
          contas.append(conta)
          numero_conta += 1

    elif opcao == "6":
       exibir_contas(contas)
    
    elif opcao == "0":
        break

    else:
        print("Operação inválida, informe o número da opção desejada.")

