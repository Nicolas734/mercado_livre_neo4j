def excluir_usuario(session):

    lista_usuarios = session.run("MATCH (u:Usuario) RETURN u")

    for u in lista_usuarios:
        usuario = u.value()
        print(f'\nid: {usuario.element_id.split(":")[2]}')
        print('Nome: {nome}'.format(nome = usuario._properties['nome']))
        print('Email: {email}'.format(email = usuario._properties['email']))

    id_usuario = input(str("\nDigite o id do usuario que deseja excluir: "))

    query = f'MATCH (u:Usuario) WHERE ID(u) = {id_usuario} DELETE u'

    session.run(query)

    print(f"\nUsuario de id {id_usuario} deletado com sucesso...")