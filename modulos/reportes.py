def obtener_goles_anotados(equipo):
    return equipo[5] 

def obtener_puntos(equipo):
    return equipo[7]  

def obtener_partidos_ganados(equipo):
    return equipo[2]  


def reporte_max_goles(equipos):
    if equipos:
        equipo_mas_goles = max(equipos, key=obtener_goles_anotados)  
        print("El equipo que más goles anotó es:", equipo_mas_goles[0])
    else:
        print("No hay información disponible. Registre equipos y partidos primero.")

def reporte_max_puntos(equipos):
    if equipos:
        equipo_mas_puntos = max(equipos, key=obtener_puntos)  
        print("El equipo que más puntos tiene es:", equipo_mas_puntos[0])
    else:
        print("No hay información disponible. Registre equipos y partidos primero.")

def reporte_max_partidos_ganados(equipos):
    if equipos:
        equipo_mas_ganados = max(equipos, key=obtener_partidos_ganados)  
        print("El equipo que más partidos ganó es:", equipo_mas_ganados[0])
    else:
        print("No hay información disponible. Registre equipos y partidos primero.")

def total_goles_anotados(equipos):
    if equipos:
        total_goles = sum(equipo[5] for equipo in equipos)  
        print("El total de goles anotados por todos los equipos es:", total_goles)
    else:
        print("No hay información disponible. Registre equipos y partidos primero.")

def promedio_goles_anotados(equipos):
    if equipos:
        total_partidos = sum(equipo[1] for equipo in equipos) 
        total_goles = sum(equipo[5] for equipo in equipos) 
        promedio = total_goles / total_partidos 
        print("El promedio de goles anotados en el torneo es:", promedio)
    else:
        print("No hay información disponible. Registre equipos y partidos primero.")

def mostrar_estadisticas_equipos(equipos):
    if equipos:
        print("Estadísticas de todos los equipos:")
        for equipo in equipos:
            print(f"\nEquipo: {equipo[0]}")  
            print(f"PJ: {equipo[1]}")
            print(f"PG: {equipo[2]}")
            print(f"PP: {equipo[3]}")
            print(f"PE: {equipo[4]}")
            print(f"GF: {equipo[5]}")
            print(f"GC: {equipo[6]}")
            print(f"TP: {equipo[7]}")
    else:
        print("No hay información disponible. Registre equipos y partidos primero.")