### CONDICIONALES ANIDADOS
colores = {
    'limpia': '\033[m',
    'amarillo': '\033[33m',
    'azul': '\033[34m',
    'negrita': '\033[1m',
    'FondoRojo': '\033[30;41m',
    'FondoAmarillo': '\033[43m',
    'FondoVerde': '\033[1;44m',
    'Invertido': '\033[7;40m'
}


from random import choice
from time import sleep

juegosPosibles = ['piedra', 'papel', 'tijeras']
reglas = {
    'piedra': 'tijeras',
    'papel': 'piedra',
    'tijeras': 'papel'
}
computadoraElige = choice(juegosPosibles)
salir = 0

print('\n')

for i in range(30):
    print(f'{colores["azul"]}-={colores["limpia"]}', end='', flush=True)
    sleep(0.05)
    
print(f'\n{colores["Invertido"]}\n Piedra, Papel o Tijeras{colores["limpia"]} \n')

for i in range(30):
    print(f'{colores["azul"]}-={colores["limpia"]}', end='', flush=True)
    sleep(0.05)

print(f'\n¿Estás Listo?\n')

while(salir == 0):
    jugadorElige = input('¿Qué elegis jugar? PIEDRA, PAPEL O TIJERAS?\n').lower().strip()

    print('\nPROCESANDO...\n')
    sleep(1)

    if jugadorElige not in reglas:
        print(f'{colores["FondoRojo"]}Elija una opción correcta.{colores["limpia"]}')
    else:
        if(computadoraElige == jugadorElige):
            print(f'{colores["azul"]}¡EMPATE!{colores["limpia"]} \nLa computadora eligió {colores["amarillo"]}{computadoraElige}{colores["limpia"]} y el jugador {colores["amarillo"]}{jugadorElige}{colores["limpia"]}\n')
        elif(reglas[jugadorElige] == computadoraElige):
            print(f'{colores["FondoVerde"]}¡GANASTE!{colores["limpia"]} \nLa computadora eligió {colores["amarillo"]}{computadoraElige}{colores["limpia"]} y el jugador {colores["amarillo"]}{jugadorElige}{colores["limpia"]}\n')
        else:
            print(f'{colores["FondoRojo"]}¡PERDISTE!{colores["limpia"]} \nLa computadora eligió {colores["amarillo"]}{computadoraElige}{colores["limpia"]} y el jugador {colores["amarillo"]}{jugadorElige}{colores["limpia"]}\n')
    
    sleep(1)
    salir = int(input('\nDesea salir?\n\t0. Seguir jugando\n\t1. Salir del juego\n'))

print(f'{colores["negrita"]}\nMuchas gracias por jugar.{colores["limpia"]}')
