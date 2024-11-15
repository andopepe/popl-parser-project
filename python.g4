grammar python;

start: line* EOF;

ifStatement: 'if' expression+ ':''\t'?tws'\t' line+ elif*  else?;

elif: ('elif' expression+ ':'(tws'\t'line)+);

else: ('else:'(tws'\t'line)+);

line: (term assignment expression tws?) | ifStatement;

assignment: operator?'=';

expression: (('(' expression ')') | exp);
exp: (value ( (operator|conditionals|and|or) (term|value|expression))?);


value: ('('val')') | val;
val: not? (term | number | string | bool | array);

tws:  ('\n')+;
array: '[' ((value',')*? value)']';
string: ('"' ~'"'*? '"') | ('\'' ~'\''*? '\'');
operator: '+' | '-' | '/' | '%' | '*';
conditionals: '<' | '<=' | '==' | '>=' | '>' | '!=';

term : TERM;
and: 'and';
or: 'or';
not: 'not';

bool: 'True' | 'False';
number : FLOAT | DIGIT;
TERM: [a-zA-Z] [a-zA-Z0-9_\-]*;
FLOAT: '-'?[0-9]+ '.' [0-9]+;
DIGIT: '-'?[0-9]+;
NTWS: (' ' | '\r')-> skip;
// WS: ('\t'|' ' | '\r' | '\n')-> skip;
