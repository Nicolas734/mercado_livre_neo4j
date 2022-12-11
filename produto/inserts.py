from datetime import date
import uuid


def inserir_produto(session):
    lista_vendedores = session.run("MATCH (n:Vendedor) RETURN n ")

    for vendedor in lista_vendedores:
        print('id: ' + vendedor[0].element_id[-2::])
        print('Nome: ' + vendedor[0]._properties['nome'])
        print('Email: ' + vendedor[0]._properties['email'])


    id_vendedor = input(str("Digite o id do vendedor que deseja cadastrar um produto: "))

    dataAtual = date.today()
    nome = input(str("Digite o nome do produto: "))
    descricao = input(str("Digite a descrição do produto: "))
    preco = input(str("Digite o preço do produto: "))
    quantidade = input(str("Digite a quantidade de produtos em estoque: "))
    data_postagem = dataAtual.strftime('%d/%m/%Y')
    codigo_identificacao = str(uuid.uuid1())



    query_inserir_produto = 'CREATE (p:Produto { codigo_identificacao:"' + codigo_identificacao + '", nome:"' + nome + '", descricao:"' + descricao + '", preco:"' + preco + '", quantidade: "' + quantidade +'", data_postagem: "' + data_postagem +'"})'
    session.run(query_inserir_produto)


    query = '''
        MATCH
            (v:Vendedor), (p:Produto)
        WHERE ID(v) = {id_vendedor} and p.codigo_identificacao = "{cod_id}"
        CREATE (v)-[:VENDE]->(p)
    '''.format(id_vendedor = id_vendedor, cod_id = codigo_identificacao)

    session.run(query)