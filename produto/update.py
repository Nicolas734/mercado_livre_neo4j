def atualizar_produto(session):

    lista_produtos = session.run("MATCH (p:Produto) RETURN p")

    for p in lista_produtos:
        produto = p.value()
        print("\nid: "+ produto.element_id.split(":")[2])
        print("Nome: "+ produto._properties['nome'])
        print("Preço: "+ produto._properties['preco'])

    id_produto = input(str("Digite o id do produto que deseja atualizar: "))

    nome = input(str("Digite o nome do produto: "))
    descricao = input(str("Digite a descrição do produto: "))
    preco = input(str("Digite o preço do produto: "))
    quantidade = input(str("Digite a quantidade de produtos em estoque: "))

    dados = 'p.nome = "' + nome + '", p.descricao = "' + descricao + '", p.preco = "' + preco + '", p.quantidade =  "' + quantidade +'"'

    query = f'MATCH (p:Produto) WHERE ID(p) = {id_produto} SET {dados}'

    session.run(query)

    print("\nDados do produto atualizados com sucesso...")