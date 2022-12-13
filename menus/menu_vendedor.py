from vendedor.selects import buscar_vendedores
from vendedor.inserts import inserir_vendedor
from vendedor.update import atualizar_vendedor
from vendedor.delete import excluir_vendedor

def menu_vendedor(session):
    execucao =True

    while execucao:

        print('''
Opções:
[1] Buscar todos os vendedores
[2] Cadastrar um novo vendedor
[3] Atualizar informações de um vendedor
[4] Excluir um vendedor
[0] Voltar
        ''')

        opcao = input(str("Escolha uma opção: "))

        match int(opcao):
            case 1:
                buscar_vendedores(session)
            case 2:
                inserir_vendedor(session)
            case 3:
                atualizar_vendedor(session)
            case 4:
                excluir_vendedor(session)
            case 0:
                execucao = False
                return
            case _:
                print("Operação não entendida...")