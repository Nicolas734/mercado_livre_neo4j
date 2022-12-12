def buscar_produtos(session):

    lista_produtos = session.run("MATCH (p:Produto) RETURN p")

    print("\nListagem dos produtos cadastrados no sistema...")

    for p in lista_produtos:
        produto = p.value()
        print("\nid: "+ produto.element_id.split(":")[2])
        print("Nome: "+ produto._properties['nome'])
        print("Descricao: "+ produto._properties['descricao'])
        print("Preço: "+ produto._properties['preco'])
        print("Quantidade: "+ produto._properties['quantidade'])
        print("Data de postagem: "+ produto._properties['data_postagem'])