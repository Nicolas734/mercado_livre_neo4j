def excluir_produto(session):

    lista_produtos = session.run("MATCH (p:Produto) RETURN p")

    for p in lista_produtos:
        produto = p.value()
        print("\nid: "+ produto.element_id.split(":")[2])
        print("Nome: "+ produto._properties['nome'])
        print("Preço: "+ produto._properties['preco'])

    id_produto = input(str("Digite o id do produto que deseja excluir: "))

    query = f'MATCH (p:Produto) WHERE ID(p) = {id_produto} DELETE p'

    session.run(query)

    print(f"\nProduto de id {id_produto} deletado com sucesso...")