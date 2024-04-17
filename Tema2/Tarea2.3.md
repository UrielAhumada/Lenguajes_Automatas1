# Tarea 2.3

## Ejercicio 1
Expresión regular que valide un Password fuerte:
1 minúscula
1 mayúscula
1 numero
1 carácter especial
8 caracteres de longitud

*Expresion*: ^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\da-zA-Z]).{8,}$

Esta compuesta de:
- ^: Indica el comienzo de la cadena.
- (?=.*[a-z]): Este es un "positive lookahead" que asegura que la cadena contenga al menos una letra minúscula de la a-z.
- (?=.*[A-Z]): Similar al anterior, pero asegura que la cadena contenga al menos una letra mayúscula de la A-Z.
. (?=.*\d): Otro "positive lookahead" que asegura que la cadena contenga al menos un dígito (0-9).
- (?=.*[^\da-zA-Z]): Un "positive lookahead" que asegura que la cadena contenga al menos un carácter especial, es decir, un carácter que no sea letra ni número.
- .{8,}: Este componente asegura que la longitud total de la cadena sea de al menos 8 caracteres.
- $: Indica el final de la cadena.

*Demostracion*:
![image](https://github.com/UrielAhumada/Lenguajes_Automatas1/assets/160798678/6952fddc-ccce-46f1-b808-8c55690de002)

## Ejercicio 2
Expresión Regular que valide un Nombre de usuario:
Longitud de 3 a 16 caracteres
Letra o numero o guion medio o bajo

*Expresion*: ^[a-zA-Z0-9_-]{3,16}$

Esta compuesta de:
- ^: Indica el comienzo de la cadena.
- [a-zA-Z0-9_-]: Este es un conjunto de caracteres permitidos. En este caso, incluye letras minúsculas (a-z), letras mayúsculas (A-Z), dígitos (0-9), el guión bajo _ y el guión -.
- {3,16}: Este componente indica que la longitud de la cadena debe estar entre 3 y 16 caracteres.
- $: Indica el final de la cadena.

*Demostracion*:
![image](https://github.com/UrielAhumada/Lenguajes_Automatas1/assets/160798678/ead916e8-2518-4504-838e-8e5593a3f57a)
