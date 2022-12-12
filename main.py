from neo4j import GraphDatabase

from usuario.selects import buscar_usuarios
from usuario.inserts import inserir_usuario
from usuario.update import atualizar_usuario
from usuario.delete import excluir_usuario

from vendedor.inserts import inserir_vendedor
from vendedor.selects import buscar_vendedores
from vendedor.update import atualizar_vendedor
from vendedor.delete import excluir_vendedor

from produto.inserts import inserir_produto
from produto.selects import buscar_produtos
from produto.update import atualizar_produto
from produto.delete import excluir_produto

from compra.inserts import inserir_compra
from compra.selects import buscar_compras

uri = "neo4j+s://c5e4de7a.databases.neo4j.io"
user = "neo4j"
password = "4LPL3ZekXAfhwKOUe8QzZd-LveQm_mvNhqjEPIVJalI"

try:
    driver = GraphDatabase.driver(uri, auth=(user, password))
    session = driver.session()
    print("Conexão bem sucedida...")
except Exception as erro:
    print("Falha ao criar conexão com o driver", erro)

execucao = True

while execucao:
    print('''
[1] buscar usuarios
[2] cadastrar usuario
[3] cadastrar vendedor
[4] cadastrar produto
[5] cadastrar compra
[6] buscar vendedores
[7] buscar produtos
[8] buscar compras
[9] atualizar usuario
[10] atualizar vendedor
[11] atualizar produto
[12] excluir usuario
[13] excluir vendedor
[14] excluir produto
[0] Sair
''')

    opcao = input(str('Escolha uma das opções acima: '))

    match int(opcao):
        case 1:
            buscar_usuarios(session)
        case 2:
            inserir_usuario(session)
        case 3:
            inserir_vendedor(session)
        case 4:
            inserir_produto(session)
        case 5:
            inserir_compra(session)
        case 6:
            buscar_vendedores(session)
        case 7:
            buscar_produtos(session)
        case 8:
            buscar_compras(session)
        case 9:
            atualizar_usuario(session)
        case 10:
            atualizar_vendedor(session)
        case 11:
            atualizar_produto(session)
        case 12:
            excluir_usuario(session)
        case 13:
            excluir_vendedor(session)
        case 14:
            excluir_produto(session)
        case 0:
            execucao = False
            break
        case _:
            print("Operação não entendida...")