#coding: latin1
from time import sleep
import requests

from api.personas.personas import personasBP


def main():
    print('Bienvenido a la API de Personas y sus m�viles')
    op = int(input('�A qu� fichero quiere entrar?\n1. Personas\n2. M�viles\n3. Salir\n'))

    while op > 3 or op < 1:
        print('No es una opci�n v�lida')
        op = int(input('�A qu� fichero quiere entrar?\n1. Personas\n2. M�viles\n3. Salir\n'))

    if op == 1:
        print('Entrando a personas...')
        sleep(1)
        personas()
    elif op == 2:
        print('Entrando a m�viles...')
        sleep(1)
        moviles()
    elif op == 3:
        print('Un saludo...')

def personas():
    api_url = "http://127.0.0.1:5050/personas"
    print('PERSONAS')
    op = int(input('�Qu� quire hacer?\n1. Obtener todas las personas\n2. Obtener una peresona\n3. Obtener los m�viles de una persona\n4. Actualizar una persona\n5. Eliminar una persona\n6. Crear una persona\n 7.Salir'))

    while op != 7:
        if op == 1:
            response = requests.get(api_url)
            print(response.json())
        elif op == 2:
            print('\n')
            iD = int(input('Cual iD deseas obtener?'))
            response = requests.get(api_url + '/' + str(iD))
            print(response.json())
        elif op == 3:
            print('\n')
            iD = int(input('Cual es el ID de la persona de la que deseas obtener sus m�viles?'))
            response = requests.get(api_url + '/' + str(iD) + '/moviles')
            print(response.json())
        elif op == 4:
            print('\n')

            opA = int(input('�Qu� deseas hacer?\n1. Actualizar todos los campos\n2. Actualizar solo un campo\n3. Salir'))

            while opA != 3:
                if opA == 1:
                    idMod = int(input('Cual id quieres modificar'))
                    dni = input('Cual es el dni de la persona')
                    nombre = input('Cual es el nombre')
                    apellidos = input('Cuales son los apellidos')
                    telefono = int(input('Cual es el telefono'))
                    correo = input('Cual es el correo')

                    todo = {'Id': idMod, 'DNI': dni, 'Nombre': nombre, 'Apellidos': apellidos, 'Tel�fono': telefono,
                            'Correo': correo}

                    response = requests.put(api_url + '/' +  str(idMod), json=todo)
                    print(response.status_code)
                    print(response.json())
                elif opA == 2:
                    idMod = int(input('Cual id quieres modificar'))

                    modo = int(input(
                        '�Qu� quieres modificar? (1: Dni, 2: Nombre, 3: Apellidos, 4: Telefono,  5: Correo, 0: Salir)'))

                    while modo != 0:

                        if modo == 1:
                            dni = input('Cual es el dni de la persona: ')
                            todo = {'DNI': dni}
                        elif modo == 2:
                            nombre = input('Cual es el nombre: ')
                            todo = {'Nombre': nombre}
                        elif modo == 3:
                            apellidos = input('Cuales son los apellidos: ')
                            todo = {'Apellidos': apellidos}
                        elif modo == 4:
                            telefono = int(input('Cual es el telefono: '))
                            todo = {'Tel�fono': telefono}
                        elif modo == 5:
                            correo = input('Cual es el correo: ')
                            todo = {'Correo': correo}
                        else:
                            print('Esa opci�n no es v�lida. Por favor, intenta de nuevo.')

                        response = requests.put(api_url + "/" + str(idMod), json=todo)
                        print(response.status_code)
                        print(response.json())

                        print('\n')
                        modo = int(input(
                            '�Qu� quieres modificar? (1: Dni, 2: Nombre, 3: Apellidos, 4: Telefono,  5: Correo, 0: Salir)'))

                    print('\n')
                    personas()

                else:
                    print('No es una opci�n v�lida')

                print('\n')
                opA = int(
                    input('�Qu� deseas hacer?\n1. Actualizar todos los campos\n2. Actualizar solo un campo\n3. Salir'))

            print('\n')
            personas()

        elif op == 5:
            iD = int(input('Cual ID deseas eliminar'))
            response = requests.delete(api_url + '/' + str(iD))
            print(response.status_code)
            print(response.json())

        elif op == 6:
            dni = input('Cual es el dni de la persona')
            nombre = input('Cual es el nombre')
            apellidos = input('Cuales son los apellidos')
            telefono = int(input('Cual es el telefono'))
            correo = input('Cual es el correo')

            todo = {'DNI': dni, 'Nombre': nombre, 'Apellidos': apellidos, 'Tel�fono': telefono,
                    'Correo': correo}
            response = requests.post(api_url, json=todo)
            print(response.status_code)
            print(response.json())
        
        else:
            print('No es una opci�n v�lida')


        print("\n")
        op = int(input(
            '�Qu� deseas hacer?\n1. Obtener todas las personas\n2. Obtener una persona\n3. Obtener los m�viles de una persona\n4. Actualizar una persona\n5. Eliminar una persona\n6. Crear una persona'))
            
    
    print('\n')
    print("Volviendo al menú principal...")
    sleep(1)
    main()


def moviles():
    api_url = "http://127.0.0.1:5050/moviles"
    print('M�VILES')
    op = int(input('�Qu� deseas hacer?\n1. Obtener todos los m�viles\n2. Obtener un m�vil\n3. Obtener la persona de un m�vil\n4. Actualizar un m�vil\n5. Eliminar un m�vil\n6. Crear un m�vil'))

    while op != 7:
        if op == 1:
            response = requests.get(api_url)
            print(response.json())
        elif op == 2:
            print('\n')
            iD = int(input('Cual iD deseas obtener?'))
            response = requests.get(api_url + '/' + str(iD))
            print(response.json())
        elif op == 3:
            print('\n')
            iD = int(input('Cual es el ID del m�vil de la cual deseas obtener su persona?'))
            response = requests.get(api_url + '/' + str(iD) + '/persona')
            print(response.json())
        elif op == 4:
            print('\n')

            opA = int(input('�Qu� deseas hacer?\n1. Actualizar todos los campos\n2. Actualizar solo un campo\n3. Salir'))

            while opA != 3:
                if opA == 1:
                    idMod = int(input('Cual id quieres modificar'))
                    PrecioCosteMovil = input('Cual es el precio del m�vil')
                    PrecioVentaMovil = input('Cual es el precio venta del m�vil')
                    idPersona = int(input('Cual es el id de la persona'))

                    todo = {'Id': idMod, 'Precio Coste M�vil': PrecioCosteMovil, 'Precio Venta M�vil': PrecioVentaMovil, 'IdPersona': idPersona}

                    response = requests.put(api_url + '/' +  str(idMod), json=todo)
                    print(response.status_code)
                    print(response.json())
                elif opA == 2:
                    idMod = int(input('Cual id quieres modificar'))

                    modo = int(input(
                        '�Qu� quieres modificar? (1: Precio Coste M�vil, 2: Precio Venta M�vil, 3: IdPersona, 0: Salir)'))

                    while modo != 0:

                        if modo == 1:
                            PrecioCosteMovil = input('Cual es el coste del m�vil: ')
                            todo = {'Precio Coste M�vil': PrecioCosteMovil}
                        elif modo == 2:
                            PrecioVentaMovil = input('Cual es el precio venta del m�vil: ')
                            todo = {'Precio Venta M�vil': PrecioVentaMovil}
                        elif modo == 3:
                            idPersona = input('Cual es el id de la persona: ')
                            todo = {'idPersona': idPersona}
                        else:
                            print('Esa opci�n no es v�lida. Por favor, intenta de nuevo.')

                        response = requests.put(api_url + "/" + str(idMod), json=todo)
                        print(response.status_code)
                        print(response.json())

                        print('\n')
                        modo = int(input(
                            '�Qu� quieres modificar? (1: Precio Coste M�vil, 2: Precio Venta M�vil, 3: IdPersona, 0: Salir)'))

                    print('\n')
                    moviles()

                else:
                    print('No es una opci�n v�lida')

                print('\n')
                opA = int(
                    input('�Qu� deseas hacer?\n1. Actualizar todos los campos\n2. Actualizar solo un campo\n3. Salir'))

            print('\n')
            moviles()

        elif op == 5:
            iD = int(input('Cual ID deseas eliminar'))
            response = requests.delete(api_url + '/' + str(iD))
            print(response.status_code)
            print(response.json())

        elif op == 6:
            PrecioCosteMovil = input('Cual es el precio del m�vil')
            PrecioVentaMovil = input('Cual es el precio venta del m�vil')
            idPersona = int(input('Cual es el id de la persona'))

            todo = {'Precio Coste M�vil': PrecioCosteMovil, 'Precio Venta M�vil': PrecioVentaMovil, 'IdPersona': idPersona}
            response = requests.post(api_url, json=todo)
            print(response.status_code)
            print(response.json())
        else:
            print('No es una opci�n v�lida')


        print("\n")
        op = int(input(
            '�Qu� deseas hacer?\n1. Obtener todos los m�viles\n2. Obtener un m�vil\n3. Obtener la persona de un m�vil\n4. Actualizar un m�vil\n5. Eliminar un m�vil\n6. Crear un m�vil'))


if __name__ == '__main__':
    main()