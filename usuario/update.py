def atualizar_usuario(session): 

    lista_usuarios = session.run("MATCH (u:Usuario) RETURN u")

    for u in lista_usuarios:
        usuario = u.value()

        print(f'\nid: {usuario.element_id.split(":")[2]}')
        print('Nome: {nome}'.format(nome = usuario._properties['nome']))
        print('Email: {email}'.format(email = usuario._properties['email']))

    id_usuario = input(str("\nDigite o id do usuario que deseja atualizar as informções: "))

    nome = input(str('Digite o novo nome do usuario: '))
    email = input(str('Digite o novo endereço de email: '))
    cpf = input(str('Digite o novo numero do cpf: '))
    rg = input(str('Digite o novo numero do rg: '))
    data_nascimento = input(str('Digite a nova data de nascimento: '))
    telefone = input(str('Digite o novo numero do telefone: '))
    endereco = input(str('Digite o novo endereço: '))

    dados = 'u.nome = "' + nome +'", u.email = "' + email + '", u.cpf = "' + cpf + '", u.rg = "' + rg + '", u.data_nascimento = "' + data_nascimento + '", u.telefone = "' + telefone + '", u.endereco = "' + endereco + '"'

    query = f'MATCH (u:Usuario) WHERE ID(u) = {id_usuario} SET {dados}'

    session.run(query)

    print("\nDados do usuario atualizados com sucesso...")