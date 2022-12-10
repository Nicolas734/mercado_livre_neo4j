from neo4j import GraphDatabase

from usuario.selects import buscar_usuarios
from usuario.inserts import inserir_usuario

uri = "neo4j+s://6267f122.databases.neo4j.io"
user = "neo4j"
password = "yzfy4-MPE6IQm3ezIAxSttVuEGeZbU8IqphvqLTinEk"

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
[2] buscar cadastrar usuario
[0] Sair
''')

    opcao = input(str('Escolha uma das opções acima: '))

    match int(opcao):
        case 1:
            buscar_usuarios(session)
        case 2:
            inserir_usuario(session)
        case 0:
            break
        case _:
            print("Operação não entendida...")