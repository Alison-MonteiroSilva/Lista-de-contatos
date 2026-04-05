def validar_nome(nome):
    nome = nome.strip()

    if nome == "":
        return False

    if any(caractere.isdigit() for caractere in nome):
        return False

    return True

def validar_numero(telefone):
    telefone = telefone.strip()

    if not telefone.isdigit():
        return False

    if len(telefone) < 11:
        return False

    return True

def validar_email(email):
    email = email.strip().lower()

    dominios_validos = ["@gmail.com", "@outlook.com", "@icloud.com"]

    if any(email.endswith(dominio) for dominio in dominios_validos):
        return True

    return False

def formatar_numero(numero):
    numero = numero.strip()

    if len(numero) != 11:
        return numero  # retorna original se não tiver 11 dígitos

    ddd = numero[:2]
    primeiro_digito = numero[2]
    parte1 = numero[3:7]
    parte2 = numero[7:]

    return f"({ddd}) {primeiro_digito} {parte1}-{parte2}"