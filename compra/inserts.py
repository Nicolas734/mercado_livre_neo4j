from datetime import date

def inserir_compra(session):

    lista_usuarios = session.run("MATCH (u:Usuario) RETURN u")

    for u in lista_usuarios:
        usuario = u.value()
        print("id:" + usuario.element_id.split(":")[2])
        print('nome: {nome}'.format(nome=usuario._properties['nome']))
        print('email: {email}'.format(email=usuario._properties['email']))
        print('cpf: {cpf}'.format(cpf=usuario._properties['cpf']))
        print('\n')

    id_usuario = input(str("digite o id do usuario que deseja fazer a compra: "))

    lista_produtos = session.run("MATCH (p:Produto) RETURN p")

    for p in lista_produtos:
        produto = p.value()
        print('id: ' + produto.element_id.split(":")[2])
        print('nome: ' + produto._properties['nome'])
        print('preço: ' + produto._properties['preco'])
        print('\n')

    id_produto = input(str("digite o id do produto que deseja comprar: "))

    dataAtual = date.today()
    data_compra = dataAtual.strftime('%d/%m/%Y')

    session.run(f'''
                MATCH
                    (u:Usuario), (p:Produto)
                WHERE 
                    ID(u) = {id_usuario} AND ID(p) = {id_produto}
                CREATE 
                    (u)-[:COMPROU 
                ''' + '{ data_compra:" '  + str(data_compra) + '"}]->(p)')

    print("Compra realizada com sucesso")