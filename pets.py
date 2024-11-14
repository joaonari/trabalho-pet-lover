def cadastrar_pet(pets, clientes):
    print("Cadastrar Pet")
    id_pet = input("ID do Pet: ")
    nome = input("Nome do Pet: ")
    categoria = input("Categoria (canino, felino, etc): ")
    raca = input("Raça: ")
    data_nascimento = input("Data de Nascimento (dd/mm/yyyy): ")
    cpf_dono = input("CPF do Dono: ")
    if cpf_dono in clientes:
        pets[id_pet] = {'id_pet': id_pet, 'nome': nome, 'categoria': categoria, 'raca': raca, 'data_nascimento': data_nascimento, 'cpf_dono': cpf_dono}
        print("Pet cadastrado com sucesso!")
    else:
        print("Cliente não encontrado!")

def atualizar_pet(pets, id_pet):
    if id_pet in pets:
        print("Atualizar dados do pet")
        nome = input(f"Nome ({pets[id_pet]['nome']}): ")
        categoria = input(f"Categoria ({pets[id_pet]['categoria']}): ")
        raca = input(f"Raça ({pets[id_pet]['raca']}): ")
        data_nascimento = input(f"Data de Nascimento ({pets[id_pet]['data_nascimento']}): ")
        pets[id_pet].update({'nome': nome, 'categoria': categoria, 'raca': raca, 'data_nascimento': data_nascimento})
        print("Pet atualizado com sucesso!")
    else:
        print("Pet não encontrado!")

def apagar_pet(pets, id_pet):
    if id_pet in pets:
        del pets[id_pet]
        print("Pet apagado com sucesso!")
    else:
        print("Pet não encontrado!")

def consultar_pets(pets):
    print("Pets cadastrados:")
    for id_pet, pet in pets.items():
        print(f"ID: {id_pet}, Nome: {pet['nome']}, Categoria: {pet['categoria']}")
