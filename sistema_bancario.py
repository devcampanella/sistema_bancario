menu = """ 
[a] Depositar
[b] Sacar
[c] Extrato
[d] Transferir
[e] Consultar saldo
[f] Alterar limite de saque
[g] Histórico de transações
[h] Recarga de celular
[i] Pagamento de contas
[j] Sair

=> """

saldo = 0
limite = 500
extrato = ""
historico = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "a":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            historico.append(f"Depósito: R$ {valor:.2f}")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "b":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            historico.append(f"Saque: R$ {valor:.2f}")
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "c":
        print("\n*************** EXTRATO *****************")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("******************************************")

    elif opcao == "d":
        valor = float(input("Informe o valor da transferência: "))
        if valor > 0 and valor <= saldo:
            saldo -= valor
            extrato += f"Transferência: R$ {valor:.2f}\n"
            historico.append(f"Transferência: R$ {valor:.2f}")
            print(f"Transferência de R$ {valor:.2f} realizada com sucesso.")
        else:
            print(
                "Operação falhou! Verifique se o valor é válido e se há saldo suficiente.")

    elif opcao == "e":
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "f":
        novo_limite = float(input("Informe o novo limite de saque: "))
        if novo_limite > 0:
            limite = novo_limite
            print(f"Limite de saque alterado para R$ {limite:.2f}")
        else:
            print("Operação falhou! O limite deve ser maior que zero.")

    elif opcao == "g":
        print("\n================ HISTÓRICO ================")
        if not historico:
            print("Nenhuma transação registrada.")
        else:
            for transacao in historico:
                print(transacao)
        print("==========================================")

    elif opcao == "h":
        valor = float(input("Informe o valor da recarga: "))
        if valor > 0 and valor <= saldo:
            saldo -= valor
            print(f"Recarga de R$ {valor:.2f} realizada com sucesso.")
            historico.append(f"Recarga: R$ {valor:.2f}")
        else:
            print(
                "Operação falhou! Verifique se o valor é válido e se há saldo suficiente.")

    elif opcao == "i":
        valor = float(input("Informe o valor da conta a ser paga: "))
        if valor > 0 and valor <= saldo:
            saldo -= valor
            print(f"Pagamento de R$ {valor:.2f} realizado com sucesso.")
            historico.append(f"Pagamento: R$ {valor:.2f}")
        else:
            print(
                "Operação falhou! Verifique se o valor é válido e se há saldo suficiente.")

    elif opcao == "j":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
