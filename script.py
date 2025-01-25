python
def menu():
    print("Cadastro de Clientes\n")
    print("0 - fim")
    print("1 - incluir")
    print("2 - alterar")
    print("3 - excluir")
    print("4 - consultar")
    
    opcao = input("Opção: ")
    return opcao

while True:
    opcao = menu()
    if opcao == '0':
        print("Fim do programa.")
        break
    elif opcao in ['1', '2', '3', '4']:
        print(f"Você escolheu a opção {opcao}.")
        # Aqui você pode implementar as funcionalidades correspondentes
    else:
        print("Opção inválida. Tente novamente.")
