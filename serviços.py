def cadastrar_servico(servicos):
    print("Cadastrar Serviço")
    id_servico = input("ID do Serviço: ")
    descricao = input("Descrição: ")
    valor = float(input("Valor: R$ "))
    orientacao = input("Orientação: ")
    servicos[id_servico] = {'id_servico': id_servico, 'descricao': descricao, 'valor': valor, 'orientacao': orientacao}
    print("Serviço cadastrado com sucesso!")

def atualizar_servico(servicos, id_servico):
    if id_servico in servicos:
        print("Atualizar dados do serviço")
        descricao = input(f"Descrição ({servicos[id_servico]['descricao']}): ")
        valor = float(input(f"Valor ({servicos[id_servico]['valor']}): R$ "))
        orientacao = input(f"Orientação ({servicos[id_servico]['orientacao']}): ")
        servicos[id_servico].update({'descricao': descricao, 'valor': valor, 'orientacao': orientacao})
        print("Serviço atualizado com sucesso!")
    else:
        print("Serviço não encontrado!")

def apagar_servico(servicos, id_servico):
    if id_servico in servicos:
        del servicos[id_servico]
        print("Serviço apagado com sucesso!")
    else:
        print("Serviço não encontrado!")

def consultar_servicos(servicos):
    print("Serviços cadastrados:")
    for id_servico, servico in servicos.items():
        print(f"ID: {id_servico}, Descrição: {servico['descricao']}, Valor: R$ {servico['valor']}")
