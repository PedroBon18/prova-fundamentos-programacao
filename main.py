while True:
    print("=== SISTEMA DE VENDAS ===")
    print("")
    print("1 - Registrar venda")
    print("2 - Ver resumo parcial")
    print("3 - Encerrar sistema")
    print("")
    opcao = input("Escolha uma opção: ")
    print()

    if opcao == '1':
        nome_produto = input("Nome do produto: ")
        valor_unitario = float(input("Valor unitário: "))
        quantidade = int(input("Quantidade: "))
        print()
        
    elif opcao == '3':
        break