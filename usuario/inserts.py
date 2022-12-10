def inserir_usuario(session):

    nome = input(str('Digite o nome do usuario: '))
    email = input(str('Digite o endereço de email: '))
    cpf = input(str('Digite o numero do cpf: '))
    rg = input(str('Digite o numero do rg: '))
    data_nascimento = input(str('Digite a data de nascimento: '))
    telefone = input(str('Digite o numero do telefone: '))
    endereco = input(str('Digite o endereço: '))

    query = 'CREATE (u:Usuario{ nome: "' + nome +'", email: "' + email + '", cpf: "' + cpf + '", rg: "' + rg + '", data_nascimento:"' + data_nascimento + '", telefone:"' + telefone + '", endereco:"' + endereco + '" })'
    session.run(query)
    session.close()

    print('\nUsuario cadastrado com sucesso.')