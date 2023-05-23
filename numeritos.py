# numeros = []
# for vez in range(6):
#    numero = float(input("Ingrese un numero: "))
#    numeros.append(numero)
# numeros_sumados = sum(numeros)
# numero_max = max(numeros)
# numero_menor = min(numeros)
# print("Los numeros son: ", numeros)
# print("la suma de estos numeros es :", numeros_sumados)
# print("El mayor es: ", numero_max)
# print("El menor es: ", numero_menor)

numeros = []
ordinales = ['primer', 'segundo', 'tercer', 'cuarto', 'quinto', 'sexto']

for iterador in range(6):
    leyenda = 'Ingrese el ' + ordinales [iterador] + ' numero: '
    numero = input(leyenda)

    try:
        numeros.append(float(numero))
    except:
        print('Solo se aceptan numeros, por lo tanto su ingreso sera tomado como 0')
        numeros.append(0)

suma = 0 #tenes que iniciar la variable porque sino salta error 
producto = 1
for valor in numeros:
    suma = suma + valor
    producto = producto * valor

print('-' * 80)
print('El numero mayor es: ', max(numeros))
print('El numero menos es: ', min(numeros))
print('La suma de todos los numeros es: ', suma)
print('El producto de todos los numeros es: ', producto)
print('-' * 80)