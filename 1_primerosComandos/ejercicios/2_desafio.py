# DESAFÍO 1

# Hacer un programa que lea algo 
# por teclado y muestre su tipo primitivo 
# y todas las informaciones posibles 
# sobre ella

info = input('Escriba algo: ');

print('Es de tipo: ', type(info));
print('Está TODA en minuscula?', info.islower());
print('Está TODA en mayuscula?', info.isupper());

if(info.isspace()) :
    print('\tEs solo espacio.')
else :
    if(info.isnumeric()) :
        print('\t¡Es numérico!');
    else :
        if(info.islower()) :
            print('\tEn mayuscula: ', info.upper());
        else :
            print('\tEn minuscula: ', info.lower());

print('Está capitalizada? ', info.istitle()); # returns True if the first letter of the string is in uppercase
print('Capitalizada: ', info.capitalize()); # returns the string but with the first letter in uppercase
print('Es alfanumérico?', info.isalpha()); # retorna true si es de a-z
print('Solo es espacio?', info.isspace()); # returns true if the string is just "space"
print('Es numérico?', info.isnumeric());
print('Es printeable?', info.isprintable());
print('Centrada: ', info.center(30)); # returns the string with a space of 30 characters
print('La cantidad de strings: ', info.count('a')); # returns the amount of times the specific value appears in the string
print('Termina con punto? ', info.endswith('.')); # returns True or False if it ends with the specific string

