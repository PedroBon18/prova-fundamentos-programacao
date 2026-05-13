total_vendas_realizadas = 0
total_bruto_vendido = 0
total_descontos_concedidos = 0
total_liquido_vendido = 0

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
        
        valor_bruto = valor_unitario * quantidade
        
        if valor_bruto < 100:
            taxa_desconto = 0
        elif valor_bruto < 500:
            taxa_desconto = 5
        elif valor_bruto < 1000:
            taxa_desconto = 10
        else:
            taxa_desconto = 15
            
        valor_desconto = valor_bruto * (taxa_desconto / 100)
        valor_final = valor_bruto - valor_desconto
        
        total_vendas_realizadas += 1
        total_bruto_vendido += valor_bruto
        total_descontos_concedidos += valor_desconto
        total_liquido_vendido += valor_final

        print(f"\nValor bruto da venda: R$ {valor_bruto:.2f}")
        print(f"Desconto aplicado: {taxa_desconto}%")
        print(f"Valor do desconto: R$ {valor_desconto:.2f}")
        print(f"Valor final da venda: R$ {valor_final:.2f}\n")
    
    elif opcao == '2':
        if total_vendas_realizadas == 0:
            print("Nenhuma venda registrada até o momento.\n")
        else:
            print("=== RESUMO PARCIAL ===\n")
            print(f"Total de vendas realizadas: {total_vendas_realizadas}")
            print(f"Total bruto vendido: R$ {total_bruto_vendido:.2f}")
            print(f"Total de descontos concedidos: R$ {total_descontos_concedidos:.2f}")
            print(f"Total líquido vendido: R$ {total_liquido_vendido:.2f}\n")
    
    elif opcao == '3':
        print("=== RESUMO FINAL ===\n")
        print("")
        print(f"Total de vendas realizadas: {total_vendas_realizadas}")
        print(f"Total bruto vendido: R$ {total_bruto_vendido:.2f}")
        print(f"Total de descontos concedidos: R$ {total_descontos_concedidos:.2f}")
        print(f"Total líquido vendido: R$ {total_liquido_vendido:.2f}\n")
        print("")
        print("Sistema encerrado.")
        break
    else:
        print("Opção inválida! Tente novamente.\n")