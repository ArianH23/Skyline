grammar Skyline;


root : expr EOF ;

expr    : LP expr RP                                # parenthesis

        | MINUS expr                                # mirror

        | expr MULT expr                            # instersection
        | expr MULT INTVAL                          # replication

        | expr (PLUS|MINUS) expr                    # union
        | expr (PLUS|MINUS) INTVAL                  # offset
        
        | ident ASSIGN expr                         # assignment

        | sky                                       # skylineValue
        
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