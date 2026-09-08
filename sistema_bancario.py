#Fiz essa função para validar se o valor digitado pelo usuário é um numero válido
def valida_vlr_inserido(texto):
    # Remove espaços em branco
    texto = texto.strip()

    # Verifica se sobrou algo além de espaços vazios
    if texto == "":
        return None

    # Transforma vírgula em ponto
    texto = texto.replace(",", ".")

    # Não permite valores negativos
    if texto[0] == "-":
        return None

    tem_ponto = False # Inicia antes do loop

    # Verifica caractere por caractere se é um número válido
    for caractere in texto:
        if caractere == ".":
            if tem_ponto:
                return None  # mais de um ponto não é válido
            tem_ponto = True
        elif not caractere.isdigit():
            return None  # qualquer coisa que não seja dígito ou ponto é inválido

    # Se não tinha ponto nem vírgula, considera como inteiro (.00)
    if not tem_ponto:
        texto += ".00"

    return float(texto)


def deposito(int: valor_operacao):
    global saldo
    saldo += valor_operacao
    
def saque(int: valor_operacao):
    global saldo
    saldo -= valor_operacao

extrato = """
=========================  
=== Extrato da Conta ====
=========================

"""


menu = """
========================    
=== Sistema Bancário ===
========================

Operações Disponíveis:

1 - Deposito
2 - Saque
3 - Extrato
4 - Sair

========================

Informe a operação desejada: 
"""

saldo = 0.00
limite = 500.00
extrato += "Saldo Inicial: R$ 0.00\n\n"
numero_saques = 0
LIMITE_SAQUES = 3
valor_operacao = 0.00

while True:

    opcao = input(menu)
    
    if opcao == "1":
        print("")
        print("Depósito")
        valor_operacao = valida_vlr_inserido(input("Informe o valor a ser depositado: "))
        
        if valor_operacao is not None:
            print(f"Valor a ser depositado: {valor_operacao:.2f}")
            extrato += f"Realizado Depósito de:   R$ {valor_operacao:.2f}\n"
            extrato += f"Valor antes do depósito: R$ {saldo:.2f}\n"
            deposito(valor_operacao)
            extrato += f"Saldo após o depósito:   R$ {saldo:.2f}\n \n"
            print("Deposito realizado com sucesso!")
        else:
            print("ERRO: Informe um valor válido")
        
        
    elif opcao == "2":
        print("")
        print("Opção escolhida: Saque")
        print("")
        
        if numero_saques < 3:
            valor_operacao = int(input("Informe o valor que deseja retirar: "))
            if valor_operacao is not None:
                if valor_operacao <= 500:
                    if saldo >= valor_operacao:
                        numero_saques += 1
                        extrato += f"Realizado saque no valor de R$ {valor_operacao:.2f}\n"
                        extrato += f"Valor antes do saque:       R$ {saldo:.2f}\n"
                        saque(valor_operacao)
                        extrato += f"Saldo após o saque:         R$ {saldo:.2f}\n \n"
                        print("")
                        print(f"Saque realizado com sucesso no valor de R$ {valor_operacao:.2f}!")
                    else:
                        print("")
                        print("Não foi possível realizar a operação")
                        print(f"Valor informado excedeu o saldo disponível")
                else:
                    print("")
                    print("Não foi possível realizar a operação")
                    print(f"Valor acima do permitido por saque: R$ {limite:.2f}")
            else:
                print("ERRO: Informe um valor válido")
        else:
            print("")
            print("Não foi possível realizar a operação")
            print(f"Numero limite de saques diários atingidos: {LIMITE_SAQUES}\n")
        
        
    elif opcao == "3":
        print("")
        print("Opção escolhida: Extrato")
        print("")
        
        extrato += "====== Fim Extrato ======\n"
        extrato += "=========================\n"
        print(extrato)
    
    elif opcao == "4":
        print("========================")
        print("Saindo...")
        print("========================")
        break
        
    else:
        print("Opção Inválida, informe um numero de 1 a 4 de acordo com a opção desejada")