import sys

def menu():
    print("Cadastro de Clientes\n")
    print("0 - fim")
    print("1 - incluir")
    print("2 - alterar")
    print("3 - excluir")
    print("4 - consultar")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        opcao = sys.argv[1]
    else:
        opcao = input("Opção: ")
        
    if opcao == '0':
        print("Fim do programa.")
    elif opcao in ['1', '2', '3', '4']:
        print(f"Você escolheu a opção {opcao}.")
        # Aqui você pode implementar as funcionalidades correspondentes
    else:
        print("Opção inválida. Tente novamente.")
