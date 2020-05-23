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

skyCreation : (sky | LB sky (',' sky)* RB | LC INTVAL COMMA INTVAL COMMA INTVAL COMMA INTVAL COMMA INTVAL RC);                       //Simple, compost, random

sky: (LP INTVAL COMMA INTVAL COMMA INTVAL RP);


LC        : '{';      
RC        : '}';
COMMA     : ',';
ASSIGN    : ':=';
PLUS      : '+';
MULT      : '*';
MINUS     : '-';
LP        : '(';
RP        : ')';
LB        : '[';
RB        : ']';
INTVAL    : '-'? [0-9]+ ;
ID        : [a-z] [a-zA-Z0-9]* ;
WS        : ' ' -> skip ;
