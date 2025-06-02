import re

def validar_email(email):
    """Valida se o e-mail está em um formato correto (sem espaços)"""
    return bool(re.match(r"^\S+@\S+\.\S+$", email))

def validar_senha(senha):
    """Valida se a senha tem pelo menos 8 caracteres"""
    return len(senha) >= 8