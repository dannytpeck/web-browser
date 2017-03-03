import ply.lex as lex

def test_lexer(lexer,input_string):
lexer.input(input_string)
    result = [ ]
    while True:
        tok = lexer.token()
        if not tok: break
        result = result + [tok.type]
    return result

tokens = (
        'ANDAND',       # &&
        'COMMA',        # ,
        'DIVIDE',       # /
        'ELSE',         # else
        'EQUAL',        # =
        'EQUALEQUAL',   # ==
        'FALSE',        # false
        'FUNCTION',     # function
        'GE',           # >=
        'GT',           # >
#       'IDENTIFIER',   #### Not used in this problem.
        'IF',           # if
        'LBRACE',       # {
        'LE',           # <=
        'LPAREN',       # (
        'LT',           # <
        'MINUS',        # -
        'NOT',          # !
#       'NUMBER',       #### Not used in this problem.
        'OROR',         # ||
        'PLUS',         # +
        'RBRACE',       # }
        'RETURN',       # return
        'RPAREN',       # )
        'SEMICOLON',    # ;
#       'STRING',       #### Not used in this problem.
        'TIMES',        # *
        'TRUE',         # true
        'VAR',          # var
)

states = (
    ('comment', 'exclusive'),   # /* ... */
)

def t_comment(t):
    r'\/\*'
    t.lexer.begin('comment')

def t_comment_end(t):
    r'\*\/'
    t.lexer.lineno += t.value.count('\n')
    t.lexer.begin('INITIAL')
    pass

def t_comment_error(t):
    t.lexer.skip(1)

def t_eolcomment(t):
    r'//.*'
    pass

t_ANDAND = r'&&'
t_COMMA = r','
t_DIVIDE = r'/'
t_EQUALEQUAL = r'=='
t_EQUAL = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_SEMICOLON = r';'
t_MINUS = r'-'
t_NOT = r'!'
t_OROR = r'\|\|'
t_PLUS = r'\+'
t_TIMES = r'\*'
t_LE = r'<='
t_LT = r'<'
t_GT = r'>'
t_GE = r'>='

def t_IDENTIFIER(t):
    r'[A-Za-z][A-Za-z_]*' # IDENTIFIER
    return t

def t_NUMBER(t):
    r'-?[0-9]+(?:\.[0-9]*)?' # NUMBER
    t.value = float(t.value)
    return t

def t_STRING(t):
    r'"([^"\\]|(\\.))*"' # STRING
    t.value = t.value(1:-1) # strip off "
    return t

t_ignore = ' \t\v\r' # whitespace
t_comment_ignore = ' \t\v\r'

def t_newline(t):
    r'\n'
    t.lexer.lineno += 1

def t_error(t):
    print "JavaScript Lexer: Illegal character " + t.value[0]
    t.lexer.skip(1)

# We have included two test cases to help you debug your lexer. You will
# probably want to write some of your own.

lexer = lex.lex()

def test_lexer(input_string):
  lexer.input(input_string)
  result = [ ]
  while True:
    tok = lexer.token()
    if not tok: break
    result = result + [tok.type]
  return result

input1 = """ - !  && () * , / ; { || } + < <= = == > >= else false function
if return true var """

output1 = ['MINUS', 'NOT', 'ANDAND', 'LPAREN', 'RPAREN', 'TIMES', 'COMMA',
'DIVIDE', 'SEMICOLON', 'LBRACE', 'OROR', 'RBRACE', 'PLUS', 'LT', 'LE',
'EQUAL', 'EQUALEQUAL', 'GT', 'GE', 'ELSE', 'FALSE', 'FUNCTION', 'IF',
'RETURN', 'TRUE', 'VAR']

print test_lexer(input1) == output1

input2 = """
if // else mystery
=/*=*/=
true /* false
*/ return"""

output2 = ['IF', 'EQUAL', 'EQUAL', 'TRUE', 'RETURN']

print test_lexer(input2) == output2
