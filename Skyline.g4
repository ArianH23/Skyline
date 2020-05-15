grammar Skyline;


root : statement EOF ;

statement:  ident ASSIGN expr                       # assignment

           | expr                                   # exprVal
           ;


expr    : LP expr RP                                # parenthesis

        | MINUS expr                                # mirror

        | expr MULT expr                            # interRepli

        | expr (PLUS|MINUS) expr                    # unionOffset

        | skyCreation                               # skylineValue
        
        | INTVAL                                    # integerVal

        | ident                                     # exprIdent
        ;

ident   : ID
        ;

skyCreation : (sky | LC sky (',' sky)* RC | LB INTVAL COMMA INTVAL COMMA INTVAL COMMA INTVAL COMMA INTVAL RB);                       //Simple, compost, random

sky: (LP INTVAL COMMA INTVAL COMMA INTVAL RP);


LB        : '{';      
RB        : '}';
COMMA     : ',';
ASSIGN    : ':=';
PLUS      : '+';
MULT      : '*';
MINUS     : '-';
LP        : '(';
RP        : ')';
LC        : '[';
RC        : ']';
INTVAL    : ('0'..'9')+ ;
ID        : ('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'_'|'0'..'9')* ;