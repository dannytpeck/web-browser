def t_NUMBER(token):
    r"[0-9]+"
    token.value = int(token.value)
    return token
