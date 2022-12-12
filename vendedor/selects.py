def buscar_vendedores(session):

    lista_vendedores = session.run("MATCH (v:Vendedor) RETURN v")

    print("\nListagem dos vendedores cadastrados no sistema...")

    for v in lista_vendedores:
        vendedor = v.value()
        print('\nid: ' + vendedor.element_id.split(":")[2])
        print('Nome: ' + vendedor._properties['nome'])
        print('Email: ' + vendedor._properties['email'])
        print('Cnpj: ' + vendedor._properties['cnpj'])
        print('Telefone: ' + vendedor._properties['telefone'])
        print('Data de cadastro: ' + vendedor._properties['data_cadastro'])

