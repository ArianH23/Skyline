grammar Skyline;


root : expr EOF ;

expr    : LP expr RP                                # parenthesis

        | MINUS expr                                # mirror

        | expr MULT expr                            # instersection
        | expr MULT INTVAL                          # replication

        | expr (PLUS|MINUS) expr                    # union
        | expr (PLUS|MINUS) INTVAL                  # offset
        
        | ident ASSIGN expr                         # assignment

        | ident                                     # exprIdent
        ;

ident   : ID
        ;

ASSIGN    : ':=';
PLUS      : '+';
MULT      : '*';
MINUS     : '-';
LP        : '(';
RP        : ')';
INTVAL    : ('0'..'9')+ ;
ID        : ('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'_'|'0'..'9')* ;