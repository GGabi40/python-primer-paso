tempo = int(input('Cuántos años tiene tu auto? '));

if(tempo <= 3):
	print('Auto nuevo');
else:
	print('Auto viejo');
	
print('--Fin--');

print('Auto nuevo' if tempo <= 3 else 'Auto viejo');

print('--Fin--');


### Condicional anidado

if(tempo <= 3):
	print('Auto nuevo');
elif (tempo == 3):
	print('Ya es hora de cambiarlo, eh.');
else:
	print('Auto viejo');

print('--Fin--');