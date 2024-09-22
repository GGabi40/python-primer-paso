from random import randrange;
from time import sleep;

colores = {
    'limpia': '\033[m',
    'amarillo': '\033[33m',
    'backRojo': '\033[1;41m'
};

velocidad = randrange(30, 140);
limite = 80
multa = (velocidad - limite) * 7;

sleep(2);
print(f'\n{colores["backRojo"]}¡ALTO! Control policial. {colores["limpia"]}');
print('\nLeyendo velocidad del vehículo...\n');

for i in range(5):
    print('.', end='', flush=True);
    sleep(0.5);

print('\n');

if (velocidad >= limite):
    print(f'Ibas a {colores['backRojo']}{velocidad} km/h{colores["limpia"]}. Tenés una multa por exceso de velocidad su costo será de {colores['amarillo']}$ {multa:.2f}{colores['limpia']}');
    print('ATRAPADO.');
else:
    print(f'Ibas a {colores['amarillo']}{velocidad} km/h{colores["limpia"]}. Tu velocidad está bien, siga camino.');
