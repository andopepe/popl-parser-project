from antlr4 import *
from pythonLexer import pythonLexer
from pythonParser import pythonParser

with open('retry/project_deliverable_3.py', 'r') as file:
# with open('retry/tmp.py', 'r') as file:
    content = file.read()
    # print(content)
    input_text = content
    lexer = pythonLexer(InputStream(input_text))
    stream = CommonTokenStream(lexer)
    parser = pythonParser(stream)

    tree = parser.start()


    # print(tree.toStringTree(recog=parser).replace('\n', '').replace('(', ': ').replace(')', ', ').strip()[2:])
    # print(tree.toStringTree(recog=parser).replace('(', '\n\t'))
    opens = 0

    # print(tree.toStringTree(recog=parser).split(' ('))
    # print(tree.toStringTree(recog=parser).split(' (')[0][0])

    # exit()
    result = tree.toStringTree(recog=parser).replace(' (', '(')
    print(result[:100])
    spaceCheck = True
    for index, character in enumerate(result):
        if len(character) == 0:
            continue
        # print('"',i,'"')
        if character == '"':
            if spaceCheck == True:
                spaceCheck = False
            else:
                spaceCheck = True
        if character == '\\' and result[index+1] in ['n', 't']:
            pass
        elif character in ['n', 't'] and result[index-1] == '\\':
            pass
        elif character[0] == '(':
            print('\n' +'     '*opens+'-', end="")
            opens +=1
        elif character == ')':
            opens -=1
        elif character == ' ' and spaceCheck:
            print("\n"+'    '*(opens+1), end="")
        else:
            print(character, end="")
    print()

    # print(visit(tree))