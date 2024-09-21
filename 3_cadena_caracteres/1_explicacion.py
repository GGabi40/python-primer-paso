## CORTANDO UNA STRING

frase = 'Una frutilla';
# En mi memoria:

# 0 1 2 3 4 5 6 7 8 9 10 11 -> índice de cada letra
# U N A   F R U T I L L A

# frase[ARRANCA:TERMINA];

frase[9]; # L
frase[9:11]; # L L --> Va de 9 hasta 10, no incluye el 11
frase[9:12]; # L L A

frase[9:12:2]; # Arranco en 9, paro en 11 pero salteo de 2 en 2
# L A

frase[:5]; # arranca desde 0 y va hasta 5
frase[7:]; # arranca en 7 y va hasta el final
frase[4::3]; # Arranca en 4, va hasta el final y saltea de 3 en 3


## ANÁLISIS -> Para adquirir info

frase2 = 'Un perrito';

len(frase2); # me dice cuántos caracteres posee.

frase2.count('o'); # cuenta cuántas veces aparece la letra 'o'
frase2.count('o', 0, 6); # cuenta cuántas veces aparece 
# la letra 'o' desde el índice 0 hasta el 5

frase2.find('perr'); # cuántas veces encontró 'perr'
frase2.find('banana'); # si no encuentra, devuelve -1

'perrito' in frase2; # Devuelve true o false

## TRANSFORMACIÓN -> modifica string
frase2.replace('perrito', 'python'); # busca perrito y sustituye por python

nuevaFrase = frase2.replace('perrito', 'python');

frase2.upper(); # modifica todo a mayuscula
frase2.lower(); # modifica todo a minuscula
frase2.capitalize(); # primera letra en mayuscula
frase2.title(); # todas primeras letras en mayuscula

frase3 = '  aprender a programar  ';

frase3.strip(); # Remueve todos los espacios de adelante y del final
frase3.rstrip(); # Remueve somante espacios de lado derecho
frase3.lstrip(); # Remueve somante espacios de lado izquierdo


## DIVISIÓN -> divide una string
frase2.split(); # Divide los strings por medio de los espacios
# ['UN', 'PERRITO'];


## UNIÓN -> une strings
'-'.join(frase2); # Une a la frase divida por guion
# 'un-perrito'


## Printar una frase muy grande:
print("""ABRIR COMILLAS DOBLES 3 VECES""");