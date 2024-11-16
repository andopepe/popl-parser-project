grammar python;

start: line* EOF;

ifStatement: 'if' expression+ ':''\t'?tws'\t' nifline+ elif*  else?;

elif: ('elif' expression+ ':'(tws'\t'nifline)+);

else: ('else:'(tws'\t'nifline)+);

nifline: (term assignment expression tws?);

line: (term assignment expression tws?) | ifStatement;

assignment: operator?'=';

expression: (('(' expression ')') | ex);

ex: expHP exp;

exp: (operatorLP expHP exp) 
    | (conditionals expHP exp) 
    | (and expHP exp) 
    | (or expHP exp) 
    | ;

expHP: ('('expression')' | term | value) expHPP;

expHPP: (operatorHP ('('expression')' | term | value) expHPP) | ;


//exp: ((expression ( ('+'|'-'|conditionals|and|or) (term|value))?) | expHP)*;
//expHP: (value ( (operatorHP|conditionals|and|or) (term|value))?);

value: ('('val')') | val;
val: not? (term | number | string | bool | array);

tws:  ('\n')+;
array: '[' ((value',')*? value)']';
string: ('"' ~'"'*? '"') | ('\'' ~'\''*? '\'');
operator: operatorLP | operatorHP;
operatorHP: '/' | '%' | '*';
operatorLP: '+' | '-';
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
