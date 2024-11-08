grammar python;

start: line* EOF;


line: TERM assignment expression tws?;

assignment: operator?'=';

expression: (value (operator (TERM|value|expression))?);

value: TERM | number | string | bool | array;

tws:  ('\n' | '\r')+;
array: '[' ((value',')*? value)']';
string: ('"' ~'"'*? '"') | ('\'' ~'\''*? '\'');
operator: '+' | '-' | '/' | '%' | '*';
bool: 'True' | 'False';
number : FLOAT | DIGIT;

TERM: [a-zA-Z] [a-zA-Z0-9_\-]*;
FLOAT: [0-9]+ '.' [0-9]+;
DIGIT: [0-9]+;
NTWS: ('\t'|' ')-> skip;
// WS: ('\t'|' ' | '\r' | '\n')-> skip;
