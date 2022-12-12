def atualizar_vendedor(session):

    lista_vendedores = session.run("MATCH (v:Vendedor) RETURN v")

    for v in lista_vendedores:
        vendedor = v.value()
        print('\nid: ' + vendedor.element_id.split(":")[2])
        print('Nome: ' + vendedor._properties['nome'])
        print('Email: ' + vendedor._properties['email'])

    id_vendedor = input(str("Digite o id do vendedor que deseja atualizar: "))

    nome = input(str("Digite o nome do vendedor: "))
    email = input(str('Digite o endereço de email: '))
    cnpj = input(str("Digite o cnpj: "))
    telefone = input(str('Digite o numero do telefone: '))

    dados =  'v.nome = "' + nome +'", v.email = "' + email + '", v.cnpj ="' + cnpj +'", v.telefone ="' + telefone + '"'

    query = f'MATCH (v:Vendedor) WHERE ID(v) = {id_vendedor} SET {dados}'

    session.run(query)

    print("\nDados do vendedor atualizados com sucesso...")