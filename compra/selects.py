def buscar_compras(session):

    # MATCH (u:Usuario)-[c:COMPROU] ->(p:Produto) RETURN *

    lista_compras = session.run('MATCH (u:Usuario)-[c:COMPROU] ->(p:Produto) RETURN *')

    for c in lista_compras:
        compra = c.value()
        print("\nInformações da compra")
        print("id: " + compra.element_id.split(":")[2])
        print(f"Data da compra: {compra._properties['data_compra']}")
        for informacoes_compra in compra.nodes:
            label = list(informacoes_compra.labels)
            if label[0] == "Usuario":
                print("Informações do cliente: {nome}, email: {email}".format(nome = informacoes_compra._properties['nome'], email = informacoes_compra._properties['email']))
            if label[0] == "Produto":
                print("Produto: {nome}, preco: {preco}".format( nome = informacoes_compra._properties['nome'], preco = informacoes_compra._properties['preco']))