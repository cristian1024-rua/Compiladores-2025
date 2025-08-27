grammar Calculadora;

prog: expresion EOF;

expresion
    : funcion                              # CallFunction
    | '-' expresion                       # Negativo
    | expresion '^' expresion             # Potencia
    | expresion ('*'|'/') expresion       # MultDiv
    | expresion ('+'|'-') expresion       # AddSub
    | '(' expresion ')'                   # Parentesis
    | NUMBER                              # Numero
    ;

funcion
    : ID '(' expresion ')'
    ;

ID: [a-zA-Z]+;
NUMBER: [0-9]+ ('.' [0-9]+)?;
WS: [ \t\r\n]+ -> skip;
