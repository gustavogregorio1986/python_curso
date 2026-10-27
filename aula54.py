# Lista de compras inicial vazia
lista_compras = []

while True:
    print("\n--- MENU ---")
    opcao = input("Selecione [i]nserir, [l]istar, [a]pagar ou [s]air: ").lower()

    # 1. INSERIR ITEM
    if opcao == 'i':
        item = input('Digite o valor que deseja inserir: ')
        if item.strip():  # Garante que não vai adicionar um item vazio
            lista_compras.append(item)
            print(f'"{item}" foi adicionado com sucesso!')
        else:
            print('O item não pode estar vazio.')

    # 2. LISTAR ITENS
    elif opcao == 'l':
        if not lista_compras:
            print('Sua lista de compras está vazia.')
        else:
            print('\n--- SUA LISTA DE COMPRAS ---')
            # Usamos enumerate para mostrar o índice de cada item
            for indice, item in enumerate(lista_compras):
                print(f'{indice} - {item}')

    # 3. APAGAR ITEM
    elif opcao == 'a':
        if not lista_compras:
            print('A lista está vazia, não há o que apagar.')
            continue

        # Mostra a lista atual para ajudar o usuário a escolher o índice
        print('\n--- ITENS ATUAIS ---')
        for indice, item in enumerate(lista_compras):
            print(f'{indice} - {item}')

        indice_str = input('Digite o índice (número) do item que deseja apagar: ')

        # Tratamento de erro: verifica se o usuário digitou realmente um número inteiro
        if indice_str.isdigit():
            indice = int(indice_str)
            
            # Tratamento de erro: verifica se o índice existe na lista (evita quebra por índice inexistente)
            if 0 <= indice < len(lista_compras):
                item_removido = lista_compras.pop(indice)
                print(f'"{item_removido}" foi removido com sucesso!')
            else:
                print('Erro: O índice digitado não existe na lista.')
        else:
            print('Erro: Por favor, digite apenas números inteiros válidos.')

    # 4. SAIR DO PROGRAMA
    elif opcao == 's':
        print('Encerrando o programa. Até mais!')
        break

    # OPÇÃO INVÁLIDA
    else:
        print('Opção inválida! Escolha apenas [i], [l], [a] ou [s].')