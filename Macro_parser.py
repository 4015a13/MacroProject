import ply.yacc as yacc
import Macrolex as macrolex


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
    # print('SIP Statement: {0}'.format(p[0]))

def p_assignment(p):
    '''assignment : stu_assignment
                  | method_assignment
                    '''
    p[0] = p[1]
    # print('Assignment: {0}'.format(p[0]))

def p_method(p):
    '''method : method_moveup
                | method_inq'''

    p[0] = p[1]
    # print('Method: {0}'.format(p[0]))


def p_method_moveup(p):
    '''method_moveup : ID DOT METHOD_MoveUp LP RP '''
    p[0] = (p[3], p[1])
    global student

    if student.get(p[1]) is None:
        print("ID Error")
        return p

    if p[3] == 'register':
        student.register()

    elif p[3] == "evaluate":
        student.evaluate()

    elif p[3] == "force":
        student.force()


def p_method_inq(p):
    '''method_inq : ID DOT METHOD_INQ LP RP '''

    global student

    if student.get(p[1]) is None:
        print("ID Error")
        return p

    if p[3] == 'status':
        student.status()

    elif p[3] == 'expel':
        student.expel()


def p_stu_assignment(p):
    '''stu_assignment : ID EQUALS ID'''
    p[0] = (p[2], p[1], p[3])
    global student

    if student.get(p[3]) is not None:
        student[p[1]] = None
        student.update({p[1]: student[p[3]]})
    else:
        print('ID Error')


def p_method_assignment(p):
    '''method_assignment : ID EQUALS method_inq'''
    p[0] = (p[2], p[1], p[3])
    global student


def p_empty(p):
    '''empty :  '''
    p[0] = None


def p_error(p):
    print("Macro Syntax error")
    # sys.exit("Syntax error in input")


def getparser():
    return yacc.yacc()