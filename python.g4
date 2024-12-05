grammar python;


@lexer::header{
from pythonParser import pythonParser
from antlr4.Token import CommonToken
from antlr4.Token import Token
from pythonParser import pythonParser
}
@lexer::members {
class DenterHelper(object):
    def __init__(self, nl_token, indent_token, dedent_token, should_ignore_eof):
        self.dents_buffer = []
        self.indentations = []
        self.nl_token = nl_token
        self.indent_token = indent_token
        self.dedent_token = dedent_token
        self.reached_eof = False
        self.should_ignore_eof = should_ignore_eof

    def next_token(self):
        self.init_if_first_run()
        if not self.dents_buffer:
            t = self.pull_token()
        else:
            t = self.dents_buffer.pop(0)
        if self.reached_eof:
            return t
        if t.type == self.nl_token:
            r = self.handle_newline_token(t)
        elif t.type == Token.EOF:
            r = self.apply(t)
        else:
            r = t
        return r
    
    def pull_token(self):
            """

            :rtype: CommonToken
            """
            pass

    def init_if_first_run(self):
        if not self.indentations:
            self.indentations.insert(0, 0)
            while True:
                first_real_token = self.pull_token()
                if first_real_token.type != self.nl_token:
                    break
            if first_real_token.column > 0:
                self.indentations.insert(0, first_real_token.column)
                self.dents_buffer.append(self.create_token(self.indent_token, first_real_token))
            self.dents_buffer.append(first_real_token)

    def handle_newline_token(self, t: Token):
        next_next = self.pull_token()
        while next_next.type == self.nl_token:
            t = next_next
            next_next = self.pull_token()
        if next_next.type == Token.EOF:
            return self.apply(next_next)
        nl_text = t.text
        indent = len(nl_text) - 1
        if indent > 0 and nl_text[0] == '\r':
            indent -= 1
        prev_indent = self.indentations[0]
        if indent == prev_indent:
            r = t
        elif indent > prev_indent:
            r = self.create_token(self.indent_token, t)
            self.indentations.insert(0, indent)
        else:
            r = self.unwind_to(indent, t)
        self.dents_buffer.append(next_next)
        return r

    def create_token(self, token_type, copy_from: CommonToken):
        if token_type == self.nl_token:
            token_type_str = 'newLine'
        elif token_type == self.indent_token:
            token_type_str = 'indent'
        elif token_type == self.dedent_token:
            token_type_str = 'dedent'
        else:
            token_type_str = None
        r = self.get_injected_token(copy_from, token_type_str)
        r.type = token_type
        return r
    
    def get_injected_token(self, copy_from: CommonToken, token_type_str):
        new_token = copy_from.clone()
        new_token.text = token_type_str
        return new_token

    def unwind_to(self, target_indent, copy_from : CommonToken):
        self.dents_buffer.append(self.create_token(self.nl_token, copy_from))
        while True:
            prev_indent = self.indentations.pop(0)
            if prev_indent == target_indent:
                break
            if target_indent > prev_indent:
                self.indentations.insert(0, prev_indent)
                self.dents_buffer.append(self.create_token(self.indent_token, copy_from))
                break
            self.dents_buffer.append(self.create_token(self.dedent_token, copy_from))
        self.indentations.insert(0, target_indent)
        return self.dents_buffer.pop(0)

    def apply(self, t: CommonToken):
        if self.should_ignore_eof:
            self.reached_eof = True
            return t
        else:
            if not self.indentations:
                r = self.create_token(self.nl_token, t)
                self.dents_buffer.append(t)
            else:
                r = self.unwind_to(0, t)
                self.dents_buffer.append(t)
            self.reached_eof = True
            return r

class MyCoolDenter(DenterHelper):
    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
        self.lexer: pythonLexer = lexer

    def pull_token(self):
        return super(pythonLexer, self.lexer).nextToken()

denter = None

def nextToken(self):
    if not self.denter:
        self.denter = self.MyCoolDenter(self, self.NL, pythonParser.INDENT, pythonParser.DEDENT, False)
    return self.denter.next_token()

}

NL: ('\r'? '\n' '\t'*);


start: (NL | line)*;

line: (term assignment expression NL?) | ifStatement | for | while;

assignment: operator?'=';

expression: expression operator expression | expression conditionals expression | '('expression')' | val;

// ifStatement: IF expression+ ':' (NL INDENT line)+ (ELIF expression+ ':'  (NL INDENT line)+ )* (ELSE':'  (NL INDENT line)+ )?;

// ifStatement: IF expression+ ':' NL INDENT line+ DEDENT;

ifStatement: if elif* else?;
if: IF expression+ ':' INDENT line+ DEDENT;
elif: ELIF expression+ ':'  INDENT line+ DEDENT;
else: ELSE ':'  INDENT line+ DEDENT;

while: WHILE expression+ ':' INDENT line+ DEDENT;

for: FOR expression 'in' expression ':' INDENT line+ DEDENT;

value: ('('val')') | val;
val: NOT? (term | number | STRING | bool | array | function);

array: '[' ((value',')*? value)']';
operator: operatorLP | operatorHP;
operatorHP: '/' | '%' | '*';
operatorLP: '+' | '-';
conditionals: '<' | '<=' | '==' | '>=' | '>' | '!=' | AND | OR | NOT;
function: term'('value(','value)+')';

AND: 'and';
OR: 'or';
NOT: 'not';

IF: 'if'; 

ELSE: 'else';

ELIF: 'elif';

FOR: 'for';

WHILE: 'while';


bool: TRUE | FALSE;
TRUE: 'True';
FALSE: 'False';

number : FLOAT | DIGIT+;
STRING: ('"' ~'"'*? '"') | ('\'' ~'\''*? '\'');

term: TERM;
TERM: TERM_START TERM_FOLLOW*;
fragment TERM_START: [a-zA-Z]; 
fragment TERM_FOLLOW: [a-zA-Z0-9_\-]+;

FLOAT: '-'?[0-9]+ '.' [0-9]+;
DIGIT: '-'?[0-9];
WS: [ ] ->skip; 

BLOCKCOMMENT : '\'\'\'' ( BLOCKCOMMENT | . )*? '\'\'\'' -> skip ;
BLOCKCOMMENT2 : '"""' ( BLOCKCOMMENT2 | . )*? '"""' -> skip ;
LINECOMMENT : '#' ~[\r\n]* -> skip;

INDENT: 'indent';
DEDENT: 'dedent';