# -----------------------------------------------------------------------------
# macro_lex.py
# -----------------------------------------------------------------------------
import ply.lex as lex
import ply.yacc as yacc
from ply.lex import TOKEN
import re
import sys

# reserved Words

reserved = {
    'METHOD_MoveUp': ['evaluate', 'force'],
    'METHOD_INQ': ['status', 'expel', 'gpa'],
    'STUDENT': ['student'],
    'PRINT': ['print'],
}

# tokens
tokens = [
    'INT',
    'EQUALS', 'ID', 'DOT',
    'COMMA', 'LP', 'RP', 'STRING',
] + list(reserved)

# print(tokens)

# Declaration of Basic Regular Expressions
t_EQUALS = r'\='
t_DOT = r'\.'
t_COMMA = r'\,'
t_LP = r'\('
t_RP = r'\)'

# SIP Regular Expressions Patterns
reg_method_moveup = re.compile('|'.join(reserved['METHOD_MoveUp']))
reg_method_inq = re.compile('|'.join(reserved['METHOD_INQ']))
reg_student = re.compile('|'.join(reserved['STUDENT']))
reg_print = re.compile('|'.join(reserved['PRINT']))


# SIP Regular Expressions
@TOKEN(reg_method_moveup.pattern)
def t_METHOD_MoveUp(t):
    return t


@TOKEN(reg_method_inq.pattern)
def t_METHOD_INQ(t):
    return t


@TOKEN(reg_student.pattern)
def t_STUDENT(t):
    return t

@TOKEN(reg_print.pattern)
def t_PRINT(t):
    return t


# Generic Regular Expressions

def t_INT(t):
    r'-?\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_STRING(t):
    r'\"(.+?)\"'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'ID'
    # t.type = reserved.get(t.value, 'ID')  # Check reserved words
    return t


# Ignored characters
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Lexer
lexer = lex.lex(reflags=re.UNICODE)
