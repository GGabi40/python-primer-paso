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


import random
from time import sleep

juegosPosibles = ['piedra', 'papel', 'tijeras']
reglas = {
    'piedra': 'tijeras',
    'papel': 'piedra',
    'tijeras': 'papel',
    'salir': '0'
}

salir = 0

print('\n')

for i in range(30):
    print(f'{colores["azul"]}-={colores["limpia"]}', end='', flush=True)
    sleep(0.04)
    
print(f'\n{colores["Invertido"]}\n Piedra, Papel o Tijeras{colores["limpia"]} \n')

for i in range(30):
    print(f'{colores["azul"]}-={colores["limpia"]}', end='', flush=True)
    sleep(0.04)

print(f'\n¿Estás Listo?\n')

jugadorElige = 'a'
while(jugadorElige != '0'):
    computadoraElige = random.choice(juegosPosibles)
    jugadorElige = input('¿Qué elegis jugar? PIEDRA, PAPEL O TIJERAS?\n\tPara salir: presione 0\n').lower().strip()

    if(jugadorElige == '0'):
        print(f'{colores["negrita"]}\nMuchas gracias por jugar.{colores["limpia"]}')
    else:
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
    
    

