from compra.selects import buscar_compras
from compra.inserts import inserir_compra

def menu_compra(session):
    execucao = True

    while execucao:

        print('''
Opções:
[1] Buscar todas as compras
[2] Cadastrar uma nova compra
[0] Voltar
        ''')

        opcao = input(str("Escolha uma opção: "))

        match int(opcao):
            case 1:
                buscar_compras(session)
            case 2:
                inserir_compra(session)
            case 0:
                execucao = False
                return
            case _:
                print("Operação não entendida...")