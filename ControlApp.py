from ControleEstoque import*

def menu():
    while True:
        op = int(input("\nCONTROLE DE ESTOQUE\n1.Inserir Produto\n2.Alterar Produtos\n3.Remover Produtos\n4.Listar Estoque\n5.Registrar Venda\n6.Relatório de Vendas\n7.Sair\nSelecione: "))

        if op == 1:
            cadastro()
        elif op == 2:
            alterar_produto()
        elif op == 3:
            remover_produto()
        elif op == 4:
            listar_estoque()
        elif op == 5:
            vendas_produto()
        elif op == 6:
            relatorio_vendas()
        elif op == 7:
            break
        
    


if __name__ == "__main__":
    menu()


