grammar python;

// lexer member sourced from chatGPT
@lexer::members
{
indent_stack = [0]

pending_tokens = []

def nextToken(self):
    token = super().nextToken()

    if token.type == self.NL:
    
        new_indent = 0
        while self._input.LA(1) == ord('\t'):
            new_indent += 1
            self._input.consume()
            
        space_count = 0
        while self._input.LA(1) == ord(' '):
            space_count += 1
            self._input.consume()

        new_indent += space_count // 4

        if space_count % 4 != 0:
            raise ValueError("Indentation error: spaces not multiple of 4")

        current_indent = self.indent_stack[-1] if self.indent_stack else 0
        
        if new_indent > current_indent:
            # Create indent for each tab
            for i in range(0, new_indent - current_indent):
                indent_token = self._factory.create(
                    self._tokenFactorySourcePair, 
                    self.INDENT, 
                    ' ' * new_indent, 
                    self._channel, 
                    token.start, 
                    token.stop, 
                    token.line, 
                    token.column
                )
                self.indent_stack.append(new_indent)
                self.pending_tokens.append(indent_token)
        
        elif new_indent < current_indent:
            # Create dedent tokens for each previous indent that is greater than the new indent
            while self.indent_stack and self.indent_stack[-1] > new_indent:
                self.indent_stack.pop()

                dedent_token = self._factory.create(
                    self._tokenFactorySourcePair, 
                    self.DEDENT, 
                    '', 
                    self._channel, 
                    token.start, 
                    token.stop, 
                    token.line, 
                    token.column
                )
                
                self.pending_tokens.append(dedent_token)
    
    if token.type == Token.EOF:
        while self.indent_stack and self.indent_stack[-1] > 0:
            self.indent_stack.pop()
            dedent_token = self._factory.create(
                self._tokenFactorySourcePair,
                self.DEDENT,
                '',
                self._channel,
                token.start,
                token.stop,
                token.line,
                token.column
            )
            self.pending_tokens.append(dedent_token)
    
    self.pending_tokens.append(token)

    return self.pending_tokens.pop(0)
}

NL: '\r'? '\n';

start: (NL | line)* EOF;

line: assignment NL*| expression NL* | conditional NL* | NL | if | for | while;

assignment: TERM operator?'=' expression;

expression: expression operator val | val;

if: 'if' conditional ':' INDENT line+ DEDENT NL* (elif)* (else)?;
elif: 'elif' conditional ':' INDENT line+ DEDENT NL*;
else: 'else:' INDENT line+ DEDENT NL*;

while: 'while' conditional ':' INDENT line+ DEDENT NL*;

for: 'for ' TERM ' in '( TERM | 'range' '(' number ',' number')') ':' INDENT line+ DEDENT NL*;

val: number | TERM | STRING | bool | array | ('('val')');

array: '[' ((val',')*? val)']';
operator: operatorLP | operatorHP;
operatorHP: '/' | '%' | '*';
operatorLP: '+' | '-';
conditionals: '<' | '<=' | '==' | '>=' | '>' | '!=';
conditional: comparison (AND | OR) comparison | comparison;
comparison: comparable conditionals comparable | NOT? '(' comparison ')' | comparable; 
comparable: NOT? (val | bool);

AND: ' and ';
OR: ' or ';
NOT: 'not ';

bool: TRUE | FALSE;
TRUE: 'True';
FALSE: 'False';

number : FLOAT | DIGIT;
STRING: ('"' ~'"'*? '"') | ('\'' ~'\''*? '\'');

TERM: [a-zA-Z_] [a-zA-Z0-9_]*;

FLOAT: '-'?[0-9]+ '.' [0-9]+;
DIGIT: '-'?[0-9]+;
WS: [ ] ->skip;
BLOCKCOMMENT : '\'\'\'' ( BLOCKCOMMENT | . )*? '\'\'\'' -> skip ;
BLOCKCOMMENT2 : '"""' ( BLOCKCOMMENT2 | . )*? '"""' -> skip ;
LINECOMMENT : '#' ~[\r\n]* -> skip;

INDENT: '\t';
DEDENT: '<DEDENT>';