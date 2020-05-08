grammar Skyline;


root : expr EOF ;

expr    : LP expr RP                                # parenthesis

        | MINUS expr                                # mirror

        | expr MULT expr                            # interRepli

        | expr (PLUS|MINUS) expr                    # unionOffset
        
        | ident ASSIGN expr                         # assignment

        | sky                                       # skylineValue
        
        | INTVAL                                    # integerVal

        | ident                                     # exprIdent
        ;

ident   : ID
        ;

sky: LP INTVAL COMMA INTVAL COMMA INTVAL RP;

COMMA     : ',';
ASSIGN    : ':=';
PLUS      : '+';
MULT      : '*';
MINUS     : '-';
LP        : '(';
RP        : ')';
INTVAL    : ('0'..'9')+ ;
ID        : ('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'_'|'0'..'9')* ;