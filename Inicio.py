from Registro import estudiante
EstRegist = [estudiante('Juan', 'Tercero Básico', 90), estudiante('Roberto', 'Quinto Bachillerato', 70)]
#Registrar un estudiante
def registroEst(nombre, grado, promedio):
    EstRegist.append(estudiante(nombre, grado, promedio))
    print('Estudiante registrado exitósamente.')
#Eliminar un registro de Estudiante
def eliminarEst(nombre):
    if len(EstRegist) == 0:
        print('La lista está vacia.')
    else:
        nombre = (input('Ingrese el nombre del estudiante: '))
        encontrado = None
        posicion = 0
        for i in range(len(EstRegist)):
            if EstRegist[i].verEst() == nombre:
                posición = i
                encontrado = True
                break
            else:
                encontrado = False
        if encontrado == True:
                Confirmar = int(input('¿Desea eliminar al estudiante? \n (1. Sí) (2. No) \n'))
                if Confirmar == 1:
                    EstRegist.pop(i)
                    print('Registro eliminado con éxito.')
                elif Confirmar == 2:
                    print('Acción cancelada.')
                else:
                    print('Opción Incorrecta.')
#Mostrar todos los estudiantes
def mostrarEst():
    if len(EstRegist) == 0:
        print('No hay estudiantes para mostrar.')
    else:
        print('----------------------------------')
        for i in range (len(EstRegist)):
            print(' Nombre: ',EstRegist[i].verEst(),'\n',
            'Grado: ',EstRegist[i].verGrado(),'\n',
            'Promedio: ',EstRegist[i].verPromedio())
            print('----------------------------------')
#Crear un reporte
def crearReporte():
    if len(EstRegist) == 0:
        print('No hay estudiantes para crear un reporte.')
    else:
        documento = open('Reporte de estudiantes.html','w')
        documento.write('<!DOCTYPE html>\n')
        documento.write('<html lang="es">\n')
        documento.write('<head>\n')
        documento.write('\t<title>Registro de estudiantes</title>\n')
        documento.write('</head>\n')
        documento.write('<body>\n')
        documento.write('\t<center>\n')
        documento.write('\t\t<h1>Registro de Estudiantes</h1>\n')
        documento.write('\t\t<table border="1">\n')
        documento.write('\t\t\t<tr>\n')
        documento.write('\t\t\t\t<td>Nombre</td><td>Grado</td><td>Promedio</td>\n')
        documento.write('\t\t\t</tr>\n')
        for i in range(len(EstRegist)):
            documento.write('\t\t\t<tr>\n')
            documento.write('\t\t\t\t<td>'+EstRegist[i].verEst()+
            '</td><td>'+EstRegist[i].verGrado()+'</td><td>'+str(EstRegist[i].verPromedio())+'</td>')
            documento.write('\t\t\t<tr>\n')
        documento.write('</center>\n')
        documento.write('</body>\n')
def main():
    op = 0
    print('-------------------------Registro de Estudiantes-----------------------------')
    while op != 5:
        print('______________________________________________________________________')
        print('Seleccione una opción:')
        op = int(input('1. Registrar Estudiante \n2. Eliminar Registro\n3. Mostrar Estudiantes \n4. Crear Reporte \n5.Finalizar Programa\n'))
        if op == 1:
            nombre = input('Ingrese el nombre del estudiante: ')
            edad = int(input('Ingrese la edad del estudiante: '))
            grado = input('Ingrese el grado del estudiante: ')
            registroEst(nombre, edad, grado)
        elif op == 2:
            nombre = ''
            eliminarEst(nombre)
        elif op == 3:
            mostrarEst()
        elif op == 4:
            crearReporte()
            print('Reporte creado.')
        elif op == 5:
            print('Programa finalizado.')
        else:
            print('Opción incorrecta.')
        input('Presione ENTER para continuar...')
main()