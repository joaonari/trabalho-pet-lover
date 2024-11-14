from validacoes import validar_cpf, validar_cep

def cadastrar_cliente(clientes):
    print("Cadastrar Cliente")
    nome = input("Nome: ")
    cpf = input("CPF (somente números): ")
    celular = input("Celular: ")
    email = input("Email: ")
    cep = input("CEP (XXXXX-XXX): ")
    sexo = input("Sexo (M/F): ").upper()
    if not validar_cpf(cpf) or not validar_cep(cep):
        print("Dados inválidos (CPF ou CEP)")
        return
    clientes[cpf] = {'nome': nome, 'cpf': cpf, 'celular': celular, 'email': email, 'cep': cep, 'sexo': sexo}
    print("Cliente cadastrado com sucesso!")

def atualizar_cliente(clientes, cpf):
    if cpf in clientes:
        print("Atualizar dados do cliente")
        nome = input(f"Nome ({clientes[cpf]['nome']}): ")
        celular = input(f"Celular ({clientes[cpf]['celular']}): ")
        email = input(f"Email ({clientes[cpf]['email']}): ")
        cep = input(f"CEP ({clientes[cpf]['cep']}): ")
        sexo = input(f"Sexo ({clientes[cpf]['sexo']}): ").upper()
        clientes[cpf] = {'nome': nome, 'cpf': cpf, 'celular': celular, 'email': email, 'cep': cep, 'sexo': sexo}
        print("Cliente atualizado com sucesso!")
    else:
        print("Cliente não encontrado!")

def apagar_cliente(clientes, cpf):
    if cpf in clientes:
        del clientes[cpf]
        print("Cliente apagado com sucesso!")
    else:
        print("Cliente não encontrado!")

def consultar_clientes(clientes):
    print("Clientes cadastrados:")
    for cpf, cliente in clientes.items():
        print(f"Nome: {cliente['nome']}, CPF: {cpf}, Email: {cliente['email']}")
