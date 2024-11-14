from validacoes import hash_senha

def autenticar_admin():
    admin_senha = "admin123"
    senha = input("Digite a senha do administrador: ")
    if hash_senha(senha) == hash_senha(admin_senha):
        return True
    else:
        print("Senha incorreta!")
        return False

def cadastrar_usuario(usuarios):
    print("Cadastrar Usuário")
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    tipo = input("Tipo (A - Administrador, U - Usuário): ").upper()
    if tipo not in ['A', 'U']:
        print("Tipo inválido!")
        return
    senha_hash = hash_senha(senha)
    usuarios[email] = {'nome': nome, 'email': email, 'senha': senha_hash, 'tipo': tipo}
    print("Usuário cadastrado com sucesso!")

def atualizar_usuario(usuarios, email):
    if email in usuarios:
        print("Atualizar dados do usuário")
        nome = input(f"Nome ({usuarios[email]['nome']}): ")
        senha = input(f"Senha ({usuarios[email]['senha']}): ")
        tipo = input(f"Tipo ({usuarios[email]['tipo']}): ").upper()
        usuarios[email] = {'nome': nome, 'email': email, 'senha': hash_senha(senha), 'tipo': tipo}
        print("Usuário atualizado com sucesso!")
    else:
        print("Usuário não encontrado!")

def apagar_usuario(usuarios, email):
    if email in usuarios:
        del usuarios[email]
        print("Usuário apagado com sucesso!")
    else:
        print("Usuário não encontrado!")

def consultar_usuarios(usuarios):
    print("Usuários cadastrados:")
    for email, usuario in usuarios.items():
        tipo = "Administrador" if usuario['tipo'] == 'A' else "Usuário"
        print(f"Nome: {usuario['nome']}, Email: {email}, Tipo: {tipo}")
