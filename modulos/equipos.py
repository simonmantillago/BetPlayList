def registrar_equipo(equipos, nombre_equipo):
    nuevo_equipo = [nombre_equipo, 0, 0, 0, 0, 0, 0, 0]  
    equipos.append(nuevo_equipo)

def verificar_equipo(equipos, nombre_equipo):
    for equipo in equipos:
        if equipo[0] == nombre_equipo:
            return True
    return False
