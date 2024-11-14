import hashlib
import re

def validar_cpf(cpf):
    cpf = ''.join(cpf.split())
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = 11 - (soma1 % 11)
    if digito1 > 9:
        digito1 = 0
    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = 11 - (soma2 % 11)
    if digito2 > 9:
        digito2 = 0
    return cpf[-2:] == f'{digito1}{digito2}'

def validar_cep(cep):
    return bool(re.match(r'^\d{5}-\d{3}$', cep))

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()
