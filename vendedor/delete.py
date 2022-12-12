def excluir_vendedor(session):

    lista_vendedores = session.run("MATCH (v:Vendedor) RETURN v")

    for v in lista_vendedores:
        vendedor = v.value()
        print('\nid: ' + vendedor.element_id.split(":")[2])
        print('Nome: ' + vendedor._properties['nome'])
        print('Email: ' + vendedor._properties['email'])

    id_vendedor = input(str("Digite o id do vendedor que deseja excluir: "))

    query = f'MATCH (v:Vendedor) WHERE ID(v) = {id_vendedor} DETACH DELETE v'

    session.run(query)

    print(f"\nVendedor de id {id_vendedor} deletado com sucesso...")