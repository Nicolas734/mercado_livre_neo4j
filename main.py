from neo4j import GraphDatabase

from menus.menu_usuario import menu_usuario
from menus.menu_produto import menu_produto
from menus.menu_vendedor import menu_vendedor
from menus.menu_compra import menu_compra

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
[1] Menu do usuario
[2] Menu do produto
[3] Menu do vendedor
[4] Menu da compra
[0] Sair
''')

    opcao = input(str('Escolha uma das opções acima: '))

    match int(opcao):
        case 1:
            menu_usuario(session)
        case 2:
            menu_produto(session)
        case 3:
            menu_vendedor(session)
        case 4:
            menu_compra(session)
        case 0:
            execucao = False
            break
        case _:
            print("Operação não entendida...")