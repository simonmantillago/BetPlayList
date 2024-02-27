def actualizar_estadisticas(equipo, goles_a_favor, goles_en_contra, resultado):
    equipo[1] += 1  
    equipo[5] += goles_a_favor  
    equipo[6] += goles_en_contra  

    if resultado == "Ganado":
        equipo[2] += 1  
        equipo[7] += 3  
    elif resultado == "Empatado":
        equipo[4] += 1  
        equipo[7] += 1  
    else:
        equipo[3] += 1  

def registrar_partido(equipos, local, visitante, goles_local, goles_visitante):
    equipo_local = next((equipo for equipo in equipos if equipo[0] == local), None)
    equipo_visitante = next((equipo for equipo in equipos if equipo[0] == visitante), None)

    if goles_local > goles_visitante:
        actualizar_estadisticas(equipo_local, goles_local, goles_visitante, "Ganado")
        actualizar_estadisticas(equipo_visitante, goles_visitante, goles_local, "Perdido")
    elif goles_local < goles_visitante:
        actualizar_estadisticas(equipo_visitante, goles_visitante, goles_local, "Ganado")
        actualizar_estadisticas(equipo_local, goles_local, goles_visitante, "Perdido")
    else:
        actualizar_estadisticas(equipo_local, goles_local, goles_visitante, "Empatado")
        actualizar_estadisticas(equipo_visitante, goles_visitante, goles_local, "Empatado")
