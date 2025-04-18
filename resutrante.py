import datetime

# Estruturas de Dados
estoque = []
cardapio = []
mesas = []
pedidos = []

# mostrar o estoque
def mostrar_estoque():
    print("\nEstoque:")
    print("Código | Nome | Quantidade | Unidade | Preço Unitário | Validade")
    for item in estoque:
        print(f"{item['codigo']} | {item['nome']} | {item['quantidade']} | {item['unidade']} | {item['preco']} | {item['validade']}")

#  cadastrar produto no estoque
def cadastrar_produto():
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    unidade = input("Digite a unidade de medida: ")
    preco = float(input("Digite o preço unitário: "))
    validade = input("Digite a data de validade (dd/mm/yyyy): ")
    validade = datetime.datetime.strptime(validade, "%d/%m/%Y").date()

    estoque.append({
        'codigo': codigo,
        'nome': nome,
        'quantidade': quantidade,
        'unidade': unidade,
        'preco': preco,
        'validade': validade
    })
    print("Produto cadastrado com sucesso!")

#  adicionar um item ao cardápio
def adicionar_ao_cardapio():
    nome = input("Digite o nome do prato: ")
    descricao = input("Digite a descrição do prato: ")
    preco = float(input("Digite o preço do prato: "))
    ingredientes = input("Digite os ingredientes necessários (separados por vírgula): ").split(',')
    
    cardapio.append({
        'nome': nome,
        'descricao': descricao,
        'preco': preco,
        'ingredientes': ingredientes
    })
    print("Prato adicionado ao cardápio!")

# mostrar cardápio
def mostrar_cardapio():
    print("\nCardápio:")
    for prato in cardapio:
        print(f"{prato['nome']} - {prato['descricao']} - R${prato['preco']} - Ingredientes: {', '.join(prato['ingredientes'])}")
        
def cadastrar_mesa():
    numero_mesa = int(input("Digite o número da mesa: "))
    capacidade = int(input("Digite a capacidade da mesa: "))
    status = input("Digite o status da mesa (Ocupada/Desocupada): ")
    
    mesas.append({
    'numero': numero_mesa,
    'capacidade': capacidade,
    'status': status,
    'itens': []  
})

    print("Mesa cadastrada com sucesso!")
    
def mostrar_mesas():
    print("\nMesas:")
    for mesa in mesas:
        print(f"Mesa {mesa['numero']} - Capacidade: {mesa['capacidade']} pessoas - Status: {mesa['status']}")

    
# Registrar pedidos
def registrar_pedido():
    numero_mesa = int(input("Digite o número da mesa: "))
    
    mesa_encontrada = None
    for mesa in mesas:
        if mesa['numero'] == numero_mesa:
            mesa_encontrada = mesa
            break

    if mesa_encontrada is None:
        print("Mesa não encontrada!")
        return

    print(f"Pedido registrado para a mesa {numero_mesa}!")

    pedido = []
    continuar = True
    while continuar:
        mostrar_cardapio()
        prato_nome = input("Digite o nome do prato que deseja adicionar ao pedido (ou 'sair' para finalizar): ")
        if prato_nome.lower() == 'sair':
            continuar = False
        else:
            # Verifica se o prato existe no cardápio
            prato = next((p for p in cardapio if p['nome'].lower() == prato_nome.lower()), None)
            
            if prato:
                # Verifica se o prato já está no pedido da mesa
                if prato in mesa_encontrada['itens']:
                    print(f"O prato {prato_nome} já foi adicionado ao pedido.")
                else:
                    pedido.append(prato)
                    print(f"Prato {prato_nome} adicionado ao pedido!")
            else:
                print("Prato não encontrado no cardápio!")

    # Adiciona os itens diretamente à mesa
    mesa_encontrada['itens'].extend(pedido)

    # Calcula o total do pedido
    total_pedido = sum(item['preco'] for item in pedido)

    
    pedidos.append({
        'mesa': numero_mesa,
        'itens': pedido,
        'total': total_pedido  # Adiciona o total ao pedido
    })


    print("Itens após adicionar ao pedido:")
    for item in mesa_encontrada['itens']:
        print(f"- {item['nome']} - R${item['preco']} - Ingredientes: {', '.join(item['ingredientes'])}")

    print(f"Pedido registrado para a mesa {numero_mesa}!")



# Aqui você mostra os pedidos feitos
def mostrar_pedidos():
    if not pedidos:  # Verifica se a lista de pedidos está vazia
        print("Não há pedidos registrados.")
    else:
        print("\nPedidos:")
        for pedido in pedidos:
            print(f"Mesa {pedido['mesa']}:")
            for item in pedido['itens']:
                print(f" - {item['nome']} - R${item['preco']} - Ingredientes: {', '.join(item['ingredientes'])}")

            
def calcular_conta():
    numero_mesa = int(input("Digite o número da mesa: "))
    
    # Verifica se a mesa existe
    mesa_encontrada = None
    for mesa in mesas:
        if mesa['numero'] == numero_mesa:
            mesa_encontrada = mesa
            break

    if mesa_encontrada is None:
        print("Mesa não encontrada!")
        return

    print(f"Conta calculada para a mesa {numero_mesa}!")

    # Exibe os itens da mesa de maneira legível
    print("Itens da mesa:")
    for item in mesa_encontrada['itens']:
        print(f"- {item['nome']} - R${item['preco']} - Ingredientes: {', '.join(item['ingredientes'])}")
    
    # Calcula o valor total do pedido
    total_pedido = sum(item['preco'] for item in mesa_encontrada['itens'])

    print(f"Total do pedido: R${total_pedido}")

    # Pergunta pela forma de pagamento
    pagamento = input("Qual será a forma de pagamento? (Dinheiro/Cartão): ")
    if pagamento.lower() == 'dinheiro':
        troco = float(input("Digite o valor que você irá pagar: "))
        print(f"Troco: R${troco - total_pedido:.2f}")
    else:
        print("Crédito ou débito?")
        print("1. Crédito")
        print("2. Débito")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            print("Pagamento efetuado com sucesso!")
        else:
            print("Pagamento efetuado com sucesso!")
    
    mesas.remove(mesa_encontrada)
    print(f"Mesa {numero_mesa} liberada!")
    print("Obrigado pela visita!")
    
def relatorio_vendas():
    if not pedidos:
        print("Não há pedidos registrados.")
    else:
        print("\nRelatório de Vendas:")
        for pedido in pedidos:
            print(f"Mesa {pedido['mesa']} - Total: R${pedido['total']:.2f}")

    item_mais_vendido = max(pedidos, key=lambda pedido: sum(item['preco'] for item in pedido['itens']))
    print(f"Item mais vendido: {item_mais_vendido['itens'][0]['nome']}")
    
    valor_medio_mesa = sum(pedido['total'] for pedido in pedidos) / len(pedidos)
    print(f"Valor médio por mesa: R${valor_medio_mesa}")

# Função para exibir o menu principal
def menu_principal():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Gestão de Estoque")
        print("2. Gestão da Cozinha")
        print("3. Gestão de Mesas e Pedidos")
        print("4. Gestão de Pagamentos")
        print("5. Relatórios")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_estoque()
        elif opcao == '2':
            menu_cozinha()
        elif opcao == '3':
            menu_pedidos()
        elif opcao == '4':
            menu_pagamentos()
        elif opcao == '5':
            relatorios()
        elif opcao == '6':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Submenu de Gestão de Estoque
def menu_estoque():
    while True:
        print("\n--- Gestão de Estoque ---")
        print("1. Cadastrar Produto")
        print("2. Consultar Estoque")
        print("3. Voltar ao Menu Principal")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            mostrar_estoque()
        elif opcao == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

# Submenu de Gestão da Cozinha
def menu_cozinha():
    while True:
        print("\n--- Gestão da Cozinha ---")
        print("1. Adicionar Prato ao Cardápio")
        print("2. Mostrar Cardápio")
        print("3. Voltar ao Menu Principal")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_ao_cardapio()
        elif opcao == '2':
            mostrar_cardapio()
        elif opcao == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

# Submenu de Gestão de Pedidos
def menu_pedidos():
    while True:
        print("\n--- Gestão de Pedidos ---")
        print("1. Cadastrar Mesa")
        print("2. Mostrar Mesas")
        print("3. Registrar Pedido")
        print("4. Mostrar Pedidos")
        print("5. Voltar ao Menu Principal")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_mesa()
        elif opcao == '2':
            mostrar_mesas()
        elif opcao == '3':
            registrar_pedido()
        elif opcao == '4':
            mostrar_pedidos()   
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_pagamentos():
    while True:
        print("\n--- Gestão de Pagamentos ---")
        print("1. Calcular Conta")
        print("2. Voltar ao Menu Principal")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            calcular_conta()
        elif opcao == '2':
            break
        else:
            print("Opção inválida. Tente novamente.")
            
def relatorios():
    while True:
        print("\n--- Relatórios ---")
        print("1. Relatório de Vendas")
        print("2. Voltar ao Menu Principal")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            relatorio_vendas()
        elif opcao == '2':
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu_principal()