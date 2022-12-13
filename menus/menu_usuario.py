from usuario.selects import buscar_usuarios
from usuario.inserts import inserir_usuario
from usuario.update import atualizar_usuario
from usuario.delete import excluir_usuario

def menu_usuario(session):
    execucao = True

    while execucao:

        print('''
Opções:
[1] Buscar todos os usuarios
[2] Cadastrar um novo usuario
[3] Atualizar informações de um usuario
[4] Excluir um usuario
[0] Voltar
        ''')

        opcao = input(str("Escolha uma opção: "))

        match int(opcao):
            case 1:
                buscar_usuarios(session)
            case 2:
                inserir_usuario(session)
            case 3:
                atualizar_usuario(session)
            case 4:
                excluir_usuario(session)
            case 0:
                execucao = False
                return
            case _:
                print("Operação não entendida...")