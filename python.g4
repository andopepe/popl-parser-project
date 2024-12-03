grammar python;

tokens { INDENT, DEDENT }

@lexer::members {

	// Initializing `pendingDent` to true means any whitespace at the beginning
	// of the file will trigger an INDENT, which will probably be a syntax error,
	// as it is in Python.
	private boolean pendingDent = true;

	private int indentCount = 0;

	private java.util.LinkedList<Token> tokenQueue = new java.util.LinkedList<>();

	private java.util.Stack<Integer> indentStack = new java.util.Stack<>();

	private Token initialIndentToken = null;

	private int getSavedIndent() { return indentStack.isEmpty() ? 0 : indentStack.peek(); }

	private CommonToken createToken(int type, String text, Token next) {
		CommonToken token = new CommonToken(type, text);
		if (null != initialIndentToken) {
			token.setStartIndex(initialIndentToken.getStartIndex());
			token.setLine(initialIndentToken.getLine());
			token.setCharPositionInLine(initialIndentToken.getCharPositionInLine());
			token.setStopIndex(next.getStartIndex()-1);
		}
		return token;
	}

	@Override
	public Token nextToken() {

		// Return tokens from the queue if it is not empty.
		if (!tokenQueue.isEmpty()) { return tokenQueue.poll(); }

		// Grab the next token and if nothing special is needed, simply return it.
		Token next = super.nextToken();
		//NOTE: This could be an appropriate spot to count whitespace or deal with
		//NEWLINES, but it is already handled with custom actions down in the
		//lexer rules.
		if (pendingDent && null == initialIndentToken && NEWLINE != next.getType()) { initialIndentToken = next; }
		if (null == next || HIDDEN == next.getChannel() || NEWLINE == next.getType()) { return next; }

		// Handle EOF. In particular, handle an abrupt EOF that comes without an
		// immediately preceding NEWLINE.
		if (next.getType() == EOF) {
			indentCount = 0;
			// EOF outside of `pendingDent` state means input did not have a final
			// NEWLINE before end of file.
			if (!pendingDent) {
				initialIndentToken = next;
				tokenQueue.offer(createToken(NEWLINE, "NEWLINE", next));
			}
		}

		// Before exiting `pendingDent` state queue up proper INDENTS and DEDENTS.
		while (indentCount != getSavedIndent()) {
			if (indentCount > getSavedIndent()) {
				indentStack.push(indentCount);
				tokenQueue.offer(createToken(python.INDENT, "INDENT" + indentCount, next));
			} else {
				indentStack.pop();
				tokenQueue.offer(createToken(python.DEDENT, "DEDENT"+getSavedIndent(), next));
			}
		}
		pendingDent = false;
		tokenQueue.offer(next);
		return tokenQueue.poll();
	}

}

start : ( NEWLINE | line )* EOF ;

line: (term assignment expression NEWLINE?) | ifStatement |	for  | while;

assignment: operator?'=';

expression: expression operator expression | expression conditionals expression | '('expression')' | val;

ifStatement: 'if' expression+ ':' (NEWLINE WS line )+ (NEWLINE WS)* ('elif' expression+ ':'  (NEWLINE WS line)+ )* (NEWLINE WS)* ('else:'  (NEWLINE WS line)+ )?;

while: 'while' expression+ ':' NEWLINE  (WS line)+ ;

for: 'for' expression 'in' expression ':'  (NEWLINE WS line)+ ;

value: ('('val')') | val;
val: not? (term | number | STRING | bool | array | function);

array: '[' ((value',')*? value)']';
operator: operatorLP | operatorHP;
operatorHP: '/' | '%' | '*';
operatorLP: '+' | '-';
conditionals: '<' | '<=' | '==' | '>=' | '>' | '!=' | and | or | not;
function: term'('value(','value)+')';

term : TERM;
and: 'and';
or: 'or';
not: 'not';
 
bool: 'True' | 'False';
number : FLOAT | DIGIT;
STRING: ('"' ~'"'*? '"') | ('\'' ~'\''*? '\'');
TERM: [a-zA-Z] [a-zA-Z0-9_\-]*;
FLOAT: '-'?[0-9]+ '.' [0-9]+;
DIGIT: '-'?[0-9]+;
NTWS: ' ' -> skip;

NEWLINE : ( '\r'? '\n' | '\r' ) {
    if (pendingDent) { setChannel(HIDDEN); }
    pendingDent = true;
    indentCount = 0;
    initialIndentToken = null;
};

WS : [\t]+ {
    setChannel(HIDDEN);
    if (pendingDent) { indentCount += getText().length(); }
};

BlockComment : '\'\'\'' ( BlockComment | . )*? '\'\'\'' -> channel(HIDDEN) ;
BlockComment2 : '"""' ( BlockComment2 | . )*? '"""' -> channel(HIDDEN) ;
LineComment : '#' ~[\r\n]* -> channel(HIDDEN);