import ply.lex as lex

tokens = (
    'LANGLE',      # <
    'LANGLESLASH', # </
    'RANGLE',      # >
    'EQUAL',       # =
    'STRING',      # "hello"
    'WORD',        # Welcome!
)

t_ignore = ' ' # shortcut for whitespace

def t_NEWLINE(token):
    r'\n'
    token.lexer.lineno += 1
    pass

def t_LANGLESLASH(token):
    r'</'
    return token

def t_LANGLE(token):
    r'<'
    return token

def t_RANGLE(token):
    r'>'
    return token

def t_EQUAL(token):
    r'='
    return token

def t_STRING(token):
    r'"[^"]*"'
    token.value = token.value[1:-1]
    return token

def t_WORD(token):
    r'[^ <>\n]+'
    return token

def t_NUMBER(token):
    r"[0-9]+"
    token.value = int(token.value)
    return token

webpage = """This is
<b>webpage!"""

htmllexer = lex.lex()
htmllexer.input(webpage)
while True:
    tok = htmllexer.token()
    if not tok: break
    print tok
