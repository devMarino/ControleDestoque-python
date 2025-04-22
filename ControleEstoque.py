from ControlApp import*
from datetime import datetime
produtos = {}
vendas = []
#cadastrar produtos
def cadastro():
    print('CADASTRO DE PRODUTOS')
    print()
    produto = input("Digite o NOME do produto que deseja inserir: ").lower().strip()
    if produto in produtos:
        print("Nome de produto já cadastrado.")
        return
    
    categoria = input("Digite a CATEGORIA do produto: ").lower().strip()
    try:
        preco = float(input(f"Digite o PREÇO do produto: "))
        qtd = int(input(f"Digite a QUANTIDADE em estoque: "))
    except ValueError:
        print("Erro: preço e quantidade devem ser números")
        return
    print()
    
    produtos[produto] = {
        'categoria': categoria,
        'preco': preco,
        'qtd': qtd
    }
    
    print(f"Produto: {produto}, Categoria: {categoria}, Preço: R${preco:.2f}, Quantidade: {qtd} unidades")
    print("Adicionado com sucesso!")
    
#alteração de produtos/Remover produtos  
def alterar_produto():
    print('ALTERAÇÃO DE PRODUTO')
    print()
    #validando se o produto está na lista
    nome_buscar = input("Nome do produto que deseja alterar: ").lower().strip()
    produto_achou = None
    if nome_buscar in produtos:
        produto_achou = nome_buscar
        print(f"{nome_buscar}, foi encontrado.")

    #se nao achar produto, volta pro menu    
    if produto_achou is None:
        print(f"{nome_buscar} não existe. Retornando para o Menu")
        return
    #menu de alteração
    while True:
        print(f"Dados Atuais: Produto: {produto_achou}, Categoria: {produtos[produto_achou]['categoria']}, Preço: R${produtos[produto_achou]['preco']:.2f}, Quantidade: {produtos[produto_achou]['qtd']}")
        opc = int(input("\n1.Alterar NOME do Produto\n2.Alterar CATEGORIA do produto\n3.Alterar PREÇO do Produto\n4.Alterar QUANTIDADE do Produto\n5.Sair\nSelecione: "))
        #alterar o nome do produto
        if opc == 1:
            nome_novo = input(f"Digite o novo nome: ").lower().strip()
            produtos[nome_novo] = produtos.pop(produto_achou) #altera o nome
            #limpar o nome antigo do produtos.pop(produto_achou), evitar conflitos na prox.vez que editar
            produto_achou = nome_novo
            print("Alterado com sucesso.")
        if opc == 2:
            nova_categoria = input("Digite a nova categoria: ").lower().strip()
            produtos[produto_achou]['categoria'] = nova_categoria
            print('Alterado com sucesso.')
        elif opc == 3:
            novo_preco = float(input("Digite o novo preço: ")) 
            produtos[produto_achou]['preco'] = novo_preco
            print("Alterado com sucesso.")
        elif opc == 4:      
            nova_qtd = int(input('Digite a nova quantidade: '))
            produtos[produto_achou]['qtd'] = nova_qtd
            print("Alterado com sucesso.")
        elif opc == 5:
            print("Voltando para o MENU...")
            break
def remover_produto():
    if not produtos:
        print("Não é possível remover, Não existe produtos cadastrados")
        return
    buscar_remover = input("Digite o nome do produto que deseja remover: ")
    if buscar_remover in produtos:
            resp = int(input(f"Produto: {buscar_remover}, foi encontrado. Deseja remover? 1.SIM/2.NÃO \nSelecione: "))
    if resp != 1:
        print(f"{buscar_remover}, não foi removido. Voltando para o Menu...")
        return
    else:    
        del produtos[buscar_remover]
        print("Removido com sucesso.")
         
        
def listar_estoque():
    if not produtos:
        print("Não há produtos cadastrados, insira produtos.")
        return

    print("LISTA DE ESTOQUE POR CATEGORIA")
    print()
#percorre a categoria e unifica nomes de categorias repetidas
    categorias = set([produto['categoria'] for produto in produtos.values()])
    for categoria in categorias:
        print(f"\nCategoria: {categoria.upper()}")
        for nome, produto in produtos.items():
            if produto['categoria'] == categoria:
                print(f'Produto: {nome}, Preço: R${produto["preco"]:.2f}, {produto["qtd"]} unidades')

def vendas_produto():
    if not produtos:
        print("Não há produtos cadastrados, insira produtos.")
        return
    
    print("--REGISTRAR VENDA--")
    print()
    while True:
        venda_procurar = input('Digite o produto que deseja registrar a venda / digite "0" para sair: ').lower().strip()
    #sair do loop    
        if venda_procurar == "0":
            print("Retornando para o Menu")
            break
    #verificando se existe produto no dicionário do cadastro, se não existir da break 
        if venda_procurar in produtos:
            venda_achou = produtos[venda_procurar]
        else:
            print(f"{venda_procurar} não existe. Retornando para o Menu")
            break
        
        print(f"\nProduto: {venda_procurar}")
        print(f"Preço: R${venda_achou['preco']:.2f}")
        print(f"Quantidade em estoque: {venda_achou['qtd']} unidades")
    
        try:
            qtd_vendida = int(input("Quantidade vendida: "))
        except:
            print("Erro: Digite um número válido.")
            continue
        if qtd_vendida == 0:
            print("Nada foi vendido, voltando para o Menu")
            break
        #verificando se está vendendo mais que o estoque possui
        if qtd_vendida > venda_achou['qtd']:
            print("Impossível, não é possível vender mais do que o estoque possui.")
            continue
            
            #total vendido 
        total_vendas = qtd_vendida * venda_achou['preco']
        venda_achou['qtd'] -= qtd_vendida
            #salvando o nome,quantidade e total vendidos
        vendas.append({
            'produto': venda_procurar,
            'preco_real': venda_achou['preco'],
            'qtdVendido': qtd_vendida,
            'total_vendido': total_vendas,
            "data_hora": datetime.now().strftime('%d/%m/%Y - %H:%M:%S') 
            })
        print(f"Venda registrada! Produto: {venda_procurar}, Total: R${total_vendas:.2f}")

#relatório de vendas
def relatorio_vendas():
    if not vendas:
        print("Não há vendas registradas.")
        return
    
    print("\n-- RELATÓRIO DE VENDAS --")
    print()
    escolha = int(input(f"\n1.Relatório: Total Arrecadado\n2.Relatório: filtro por Data\nSelecione: "))
    if escolha == 1:
        print("-- RELATÓRIO TOTAL ARRECADADO --")
        total_renda = 0
        #estrutura for in enumerate, percorre a lista por indices 
        for indice, venda in enumerate(vendas, 1):
            print(f"{indice}. {venda['produto'].capitalize()} - {venda['qtdVendido']} unid. - R${venda['total_vendido']:.2f} - {venda['data_hora']}")
            total_renda += venda['total_vendido']
        #saída na tela valor arrecadado
        print(f"\nTotal arrecadado: R${total_renda:.2f}")
    elif escolha == 2:
        filtro = input("Digite a DATA (%d/%m/%Y): ")
        existe_venda = False
        print("-- RELATÓRIO POR DATA/HORA --")
        for indice, venda in enumerate(vendas,1):
            if venda['data_hora'].startswith(filtro): #filtra a data
                print(f"\n{venda['data_hora']}\n{indice}. {venda['produto'].capitalize()} - {venda['qtdVendido']} unid. - R${venda['preco_real']:.2f} ")
                existe_venda = True
        if existe_venda == False:
            print(f"Não houve vendas registradas na data: {filtro}")
            