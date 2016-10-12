def t_STRING(token):
    r'"[^"]*"'
    token.value = token.value[1:-1]
    return token
