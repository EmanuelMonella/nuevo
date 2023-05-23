estudiantes = []
ingresos_invalidos = 0

while True: 
    estudiante = input('Ingrese apellido y nombre del estudiante: ').strip().upper()
    
    if len(estudiante) == 0:
        break

    estudiante_trozado = estudiante.split()
    
    if len(estudiante_trozado) != 2:
        ingresos_invalidos = ingresos_invalidos + 1
        print('Solo se permiten letras.')
        continue

    apellido = estudiante_trozado[0].strip()
    nombre = estudiante_trozado[1].strip()
    if apellido.isalpha() == False or nombre.isalpha() == False:
        ingresos_invalidos = ingresos_invalidos + 1
        print('Solo se pueden ingresar palabras.')

      
    #elif estudiante.isalpha() == False:
     #   ingresos_invalidos = ingresos_invalidos + 1
      #  print('Solo letras.')
    #elif estudiante in estudiantes:
     #   ingresos_invalidos = ingresos_invalidos + 1
      #  print('Ya esta en la lista.')
    
    else:
        estudiante_validado = apellido + ' ' + nombre
        es_va = nombre + ' ' + apellido
        if estudiante_validado in estudiantes:
            print('Ya esta en la lista')
            ingresos_invalidos = ingresos_invalidos + 1
            continue        
        elif es_va in estudiantes:
            print('Ya esta en la lista')
            ingresos_invalidos = ingresos_invalidos + 1
            continue 
        else:
            estudiantes.append(estudiante_validado)
            print('Ok')


estudiantes.sort()

print('\nFin')
print('\nLos estudiantes son: ')
for elemento in estudiantes:
    print(elemento)
print('\nLos errores son: ', ingresos_invalidos)
print('\nLa cantidad de estudiantes es: ', len(estudiantes))

archivo = open('datos1.txt', 'w')
with open('datos.txt', 'w') as f:
    f.write('\n'.join(estudiantes))
