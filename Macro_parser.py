import ply.yacc as yacc
import Macrolex as macrolex
from MacroAlgorithms import *

tokens = macrolex.tokens

global student


# ===========================================================================================
# Parsing rules
# ===========================================================================================

def p_statement(p):
    '''statement : method
                    | assignment
                    | empty
                   '''
    p[0] = p[1]


def p_assignment(p):
    '''assignment : stu_assignment
                  | method_assignment
                    '''
    p[0] = p[1]
    # print('Assignment: {0}'.format(p[0]))

def p_method(p):
    '''method : method_moveup
                | method_print
                '''

    p[0] = p[1]
    # print('Method: {0}'.format(p[0]))

def p_method_print(p):
    '''method_print : ID DOT PRINT'''
    p[0] = (p[3], str(p[1]))
    if str(p[1]) == 'Register':
        for student in Register:
            print(student.name)
    if str(p[1]) == 'full':
        for student in fullQualified:
            print(student.name)
    if str(p[1]) == 'half':
        for student in halfQualified:
            print(student.name)
    if str(p[1]) == 'quarter':
        for student in quarterQualified:
            print(student.name)
    if str(p[1]) == 'none':
        for student in notQualified:
            print(student.name)


def p_method_moveup(p):
    '''method_moveup : ID DOT METHOD_MoveUp '''
    p[0] = (p[3], str(p[1]))

    if str(p[3]) == "evaluate":
        for student in Register:
            if student.name == str(p[1]):
                student.evaluate()
                return

    if str(p[3]) == "force":
        for student in Register:
            if student.name == str(p[1]):
                student.force()
                return


def p_stu_assignment(p):
    '''stu_assignment : STUDENT EQUALS ID COMMA ID COMMA ID COMMA ID COMMA ID'''
    p[0] = (p[2], p[1], p[3])
    for student in Register:
        if student.name == str(p[3]):
            print('Invalid name')
            return
    Register.append(Student(str(p[3]), str(p[5]), str(p[7]), str(p[9]), str(p[11])))


def p_method_assignment(p):
    '''method_assignment : ID DOT METHOD_INQ'''
    p[0] = (p[2], str(p[1]), p[3])
    if str(p[3]) == "status":
        for student in Register:
            if student.name == str(p[1]):
                student.status()
                return
    if str(p[3]) == "expel":
        for student in Register:
            if student.name == str(p[1]):
                student.expel()
                return
    if str(p[3]) == "gpa":
        for student in Register:
            if student.name == str(p[1]):
                student.printGPA()
                return


def p_empty(p):
    '''empty :  '''
    p[0] = None


def p_error(p):
    print("Macro Syntax error")
    # sys.exit("Syntax error in input")


def getparser():
    return yacc.yacc()
