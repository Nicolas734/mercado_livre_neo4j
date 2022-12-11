from datetime import date

def inserir_vendedor(session):
    dataAtual = date.today()
    execucao = True
    while execucao:

        nome = input(str("Digite o nome do vendedor: "))
        email = input(str('Digite o endereço de email: '))
        cnpj = input(str("Digite o cnpj: "))
        telefone = input(str('Digite o numero do telefone: '))
        data_cadastro = dataAtual.strftime('%d/%m/%Y')

        query = 'CREATE (v:Vendedor{ nome: "' + nome +'", email: "' + email + '", cnpj:"' + cnpj +'", data_cadastro:"' + data_cadastro + '", telefone:"' + telefone + '" })'

        session.run(query)

        opcao = input(str("Deseja cadastrar outro vendedor ? [SIM/NAO] "))

        if opcao.upper() != "SIM":
            execucao = False