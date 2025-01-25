import sys

def menu():
    print("Cadastro de Clientes\n")
    print("0 - Fim")
    print("1 - Incluir")
    print("2 - Alterar")
    print("3 - Excluir")
    print("4 - Consultar")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        opcao = sys.argv[1]
    else:
        print("Opção não fornecida como argumento.")
        sys.exit(1)
        
    print(f"Opção escolhida: {opcao}")
    
    if opcao == '0':
        print("Fim do programa.")
    elif opcao in ['1', '2', '3', '4']:
        print(f"Você escolheu a opção {opcao}.")
    else:
        print("Opção inválida. Tente novamente.")
