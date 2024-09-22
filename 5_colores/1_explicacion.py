""" CÓDIGOS:
Códigos para estilo: 

0: None
1: Bold
4: Underline
7: Negative

Códigos para Texto: 

30: white
31: red
32: green
33: yellow
34: blue
35: purple
36: cyan
37: gray

Códigos para Background: 

40: white
41: red
42: green
43: yellow
44: blue
45: purple
46: cyan
47: gray
"""

print('\nTexto común');

#       Inicia color               lo corta
print('\033[1;30;41m Hola Mundo! \033[m');

# Si no se corta con el color, pasa al siguiente print
x = 10;
y = 20;

print(f'Los valores son: \033[7;40m{x}\033[m y \033[4;46m{y}\033[m');

# Utilizando format:
print(f'{'\033[1;37;42m'} Otra manera! {'\033[m'}');


# Otra manera:
cores = {
    'limpa': '\033[m',
    'azul': '\033[34m',
    'amarillo': '\033[33m',
    'blancoNegro': '\033[7;30m'
}

print(f'{cores['amarillo']} Otra manera! {cores['limpa']}');
