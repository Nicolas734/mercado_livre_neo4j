def buscar_usuarios(session):
    resultados = session.run("MATCH (n:Usuario) RETURN n ")

    print('Listagem dos usuarios...')

    for r in resultados:

        print(f'id: {r[0].element_id[-2::]}')
        print('nome: {nome}'.format(nome=r[0]._properties['nome']))
        print('email: {email}'.format(email=r[0]._properties['email']))
        print('cpf: {cpf}'.format(cpf=r[0]._properties['cpf']))
        print('rg: {rg}'.format(rg=r[0]._properties['rg']))
        print('data de nascimento: {data_nascimento}'.format(data_nascimento=r[0]._properties['data_nascimento']))
        print('telefone: {telefone}'.format(telefone=r[0]._properties['telefone']))
        print('endereco: {endereco}'.format(endereco=r[0]._properties['endereco']))
        print('\n')