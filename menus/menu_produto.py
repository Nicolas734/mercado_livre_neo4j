from produto.selects import buscar_produtos
from produto.inserts import inserir_produto
from produto.update import atualizar_produto
from produto.delete import excluir_produto

def menu_produto(session):
    execucao = True

    while execucao:

        print('''
Opções:
[1] Buscar todos os produtos
[2] Cadastrar um novo produto
[3] Atualizar informações de um produto
[4] Excluir um produto
[0] Voltar
        ''')

        opcao = input(str("Escolha uma opção: "))

        match int(opcao):
            case 1:
                buscar_produtos(session)
            case 2:
                inserir_produto(session)
            case 3:
                atualizar_produto(session)
            case 4:
                excluir_produto(session)
            case 0:
                execucao = False
                return
            case _:
                print("Operação não entendida...")