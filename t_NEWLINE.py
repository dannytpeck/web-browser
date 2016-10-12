def t_NEWLINE(token):
    r'\n'
    token.lexer.lineno += 1
    pass
