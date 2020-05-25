grammar Skyline;

root: statement EOF;

statement: ident ASSIGN expr                            # assignment 

        | expr                                          # exprValue
        ;

expr:
	LP expr RP					# parenthesis

	| MINUS expr				        # mirror

	| expr MULT expr			        # interRepli

	| expr (PLUS | MINUS) expr	                # unionOffset

	| skyCreation				        # skylineValue

	| integerValue					# newIntegerValue

	| ident						# exprIdent
        ;

ident: ID;

skyCreation: 	sky                                                                                                     //Simple
		| LB sky (COMMA sky)* RB                                                                                //Compost
		| LC integerValue COMMA integerValue COMMA integerValue COMMA integerValue COMMA integerValue RC        //Random
	        ; 

sky: (LP integerValue COMMA integerValue COMMA integerValue RP);

integerValue: MINUS INTVAL                              # negIntegerValue

        | INTVAL                                        # posIntegerValue

        ;

LC: '{';
RC: '}';
COMMA: ',';
ASSIGN: ':=';
PLUS: '+';
MULT: '*';
MINUS: '-';
LP: '(';
RP: ')';
LB: '[';
RB: ']';
INTVAL: [0-9]+;
ID: [a-z] [a-zA-Z0-9]*;
WS: ' ' -> skip;
