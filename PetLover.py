from usuarios import autenticar_admin, cadastrar_usuario, atualizar_usuario, apagar_usuario, consultar_usuarios
from clientes import cadastrar_cliente, atualizar_cliente, apagar_cliente, consultar_clientes
from pets import cadastrar_pet, atualizar_pet, apagar_pet, consultar_pets
from serviços import cadastrar_servico, atualizar_servico, apagar_servico, consultar_servicos

usuarios = {}
clientes = {}
pets = {}
servicos = {}

def menu_principal():
    print("\n=== Menu Principal Pet Lover ===")
    print("1. Gerenciar Usuários")
    print("2. Gerenciar Clientes")
    print("3. Gerenciar Pets")
    print("4. Gerenciar Serviços")
    print("5. Sair")

def menu_usuarios():
    print("\n=== Gerenciar Usuários ===")
    print("1. Cadastrar Usuário")
    print("2. Atualizar Usuário")
    print("3. Apagar Usuário")
    print("4. Consultar Usuários")
    print("5. Voltar ao Menu Principal")

def menu_clientes():
    print("\n=== Gerenciar Clientes ===")
    print("1. Cadastrar Cliente")
    print("2. Atualizar Cliente")
    print("3. Apagar Cliente")
    print("4. Consultar Clientes")
    print("5. Voltar ao Menu Principal")

def menu_pets():
    print("\n=== Gerenciar Pets ===")
    print("1. Cadastrar Pet")
    print("2. Atualizar Pet")
    print("3. Apagar Pet")
    print("4. Consultar Pets")
    print("5. Voltar ao Menu Principal")

def menu_servicos():
    print("\n=== Gerenciar Serviços ===")
    print("1. Cadastrar Serviço")
    print("2. Atualizar Serviço")
    print("3. Apagar Serviço")
    print("4. Consultar Serviços")
    print("5. Voltar ao Menu Principal")

def main():
    while True:
        menu_principal()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":  # Gerenciar Usuários
            if not autenticar_admin():
                continue  # Retorna ao menu principal se a autenticação falhar
            while True:
                menu_usuarios()
                opcao_usuario = input("Escolha uma opção de Usuários: ")
                if opcao_usuario == "1":
                    cadastrar_usuario(usuarios)
                elif opcao_usuario == "2":
                    email = input("Digite o email do usuário para atualizar: ")
                    atualizar_usuario(usuarios, email)
                elif opcao_usuario == "3":
                    email = input("Digite o email do usuário para apagar: ")
                    apagar_usuario(usuarios, email)
                elif opcao_usuario == "4":
                    consultar_usuarios(usuarios)
                elif opcao_usuario == "5":
                    break

        elif opcao == "2":  # Gerenciar Clientes
            while True:
                menu_clientes()
                opcao_cliente = input("Escolha uma opção de Clientes: ")
                if opcao_cliente == "1":
                    cadastrar_cliente(clientes)
                elif opcao_cliente == "2":
                    cpf = input("Digite o CPF do cliente para atualizar: ")
                    atualizar_cliente(clientes, cpf)
                elif opcao_cliente == "3":
                    cpf = input("Digite o CPF do cliente para apagar: ")
                    apagar_cliente(clientes, cpf)
                elif opcao_cliente == "4":
                    consultar_clientes(clientes)
                elif opcao_cliente == "5":
                    break

        elif opcao == "3":  # Gerenciar Pets
            while True:
                menu_pets()
                opcao_pet = input("Escolha uma opção de Pets: ")
                if opcao_pet == "1":
                    cadastrar_pet(pets, clientes)
                elif opcao_pet == "2":
                    id_pet = input("Digite o ID do pet para atualizar: ")
                    atualizar_pet(pets, id_pet)
                elif opcao_pet == "3":
                    id_pet = input("Digite o ID do pet para apagar: ")
                    apagar_pet(pets, id_pet)
                elif opcao_pet == "4":
                    consultar_pets(pets)
                elif opcao_pet == "5":
                    break

        elif opcao == "4":  # Gerenciar Serviços
            while True:
                menu_servicos()
                opcao_servico = input("Escolha uma opção de Serviços: ")
                if opcao_servico == "1":
                    cadastrar_servico(servicos)
                elif opcao_servico == "2":
                    id_servico = input("Digite o ID do serviço para atualizar: ")
                    atualizar_servico(servicos, id_servico)
                elif opcao_servico == "3":
                    id_servico = input("Digite o ID do serviço para apagar: ")
                    apagar_servico(servicos, id_servico)
                elif opcao_servico == "4":
                    consultar_servicos(servicos)
                elif opcao_servico == "5":
                    break

        elif opcao == "5":  # Sair
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
