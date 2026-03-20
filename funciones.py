def salud(n):
    mostrar_ico = ""
    corazones="❤️"
    for i in range(0,n,1):
        mostrar_ico = mostrar_ico + corazones
    return mostrar_ico


rango=5
print(salud(rango))