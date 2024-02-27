from modulos import equipos
from modulos import partidos
from modulos import reportes
import os
if __name__ == '__main__':
    def main():
        os.system('cls')
        equipos_list = []
        while True:
            os.system('cls')
            titulo = """
            ++++++++++++++++++++++++++++++
            + LIGA BETPLAY COLOMBIA 2024 +
            ++++++++++++++++++++++++++++++
            """
            print(titulo)
            print("\n1. Registrar equipo")
            print("2. Registrar partido")
            print("3. Reportes")
            print("4. Salir")

            opcion = solicitar_opcion()

            if opcion == 1:
                os.system('cls')
                nombre_equipo = input("Ingrese el nombre del equipo: ")
                equipos.registrar_equipo(equipos_list, nombre_equipo)    
            elif opcion == 2:
                os.system('cls')
                while True:
                    local = input("Ingrese el nombre del equipo local: ")
                    visitante = input("Ingrese el nombre del equipo visitante: ")
                    if not (equipos.verificar_equipo(equipos_list, local) and equipos.verificar_equipo(equipos_list, visitante)):
                        print("Error: Uno o ambos equipos no están registrados.")
                        continue
                    goles_local = solicitar_gol(local)
                    goles_visitante = solicitar_gol(visitante)
                    partidos.registrar_partido(equipos_list, local, visitante, goles_local, goles_visitante)
                    break
            elif opcion == 3:
                os.system('cls')
                submenu_reportes(equipos_list)
            elif opcion == 4:
                os.system('cls')
                break
            else:
                os.system('cls')
                print("Opción inválida. Por favor, seleccione una opción válida.")

    def submenu_reportes(equipos):
        while True:
            os.system('cls')
            titulo = """
            ++++++++++++++++++++++++++++++
            + LIGA BETPLAY COLOMBIA 2024 +
            ++++++++++++++++++++++++++++++
            """
            print(titulo)
            print("1. Equipo con más goles anotados")
            print("2. Equipo con más puntos")
            print("3. Equipo con más partidos ganados")
            print("4. Total de goles anotados por todos los equipos")
            print("5. Promedio de goles anotados en el torneo")
            print("6. Ver estadísticas de todos los equipos")
            print("7. Volver al menú principal")

            opcion = solicitar_opcion()

            if opcion == 1:
                reportes.reporte_max_goles(equipos)
                os.system('pause')
                
            elif opcion == 2:
                reportes.reporte_max_puntos(equipos)
                os.system('pause')
                
            elif opcion == 3:
                reportes.reporte_max_partidos_ganados(equipos)
                os.system('pause')
                
            elif opcion == 4:
                reportes.total_goles_anotados(equipos)
                os.system('pause')
                
            elif opcion == 5:
                reportes.promedio_goles_anotados(equipos)
                os.system('pause')
                
            elif opcion == 6:
                reportes.mostrar_estadisticas_equipos(equipos)
                os.system('pause')
                
            elif opcion == 7:
                break
            
    def solicitar_opcion():
        while True:
            try:
                opcion = int(input("Seleccione una opción: "))
                return opcion
            except ValueError:
                print("Opcion invalida")
    
    def solicitar_gol(name):
            while True:
                    try:
                        opcion = int(input(f'Cuantos goles metio el equipo {name}: '))
                        return opcion
                    except ValueError:
                        print('Dato invalido')

    main()





        