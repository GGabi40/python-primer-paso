from random import randrange;
from time import sleep;

velocidad = randrange(30, 140);
limite = 80
multa = (velocidad - limite) * 7;

sleep(2);
print('\n¡ALTO! Control policial.');
print('\nLeyendo velocidad del vehículo...\n');

for i in range(5):
    print('.', end='', flush=True);
    sleep(0.5);

print('\n');

if (velocidad >= limite):
    print(f'Ibas a {velocidad} km/h. Tenés una multa por exceso de velocidad su costo será de $ {multa:.2f}');
    print('ATRAPADO.');
else:
    print(f'Ibas a {velocidad} km/h. Tu velocidad está bien, siga camino.');
