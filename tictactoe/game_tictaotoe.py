import random


opcionesGanadoras = [["A1", "B1", "C1"], ["A2", "B2", "C2"], ["A3", "B3", "C3"],
                     ["A1", "A2", "A3"], ["B1", "B2", "B3"], ["C1", "C2", "C3"],
                     ["A1", "B2", "C3"], ["C1", "B2", "A3"]]

def tablero(dictCasillas):
    print(f"-|A|B|C|")
    print(f"1|{dictCasillas['A1']}|{dictCasillas['B1']}|{dictCasillas['C1']}|")
    print(f"2|{dictCasillas['A2']}|{dictCasillas['B2']}|{dictCasillas['C2']}|")
    print(f"3|{dictCasillas['A3']}|{dictCasillas['B3']}|{dictCasillas['C3']}|")

def verificacion_col(columna):
    if columna.upper() in ["A","B","C"]:
        return True
    return False

def verificacion_fila(fila):
    try:
        if int(fila) in [1,2,3]:
            return True

        return False
    except:
        print("El valor debe ser un número")
        return False

def pedir_casilla():
    while True:
        columna = input("\nSelecciona la Columna (A, B, C): ")
        if not verificacion_col(columna):
            print("Columna Inválida")
        else:
            break

    while True:
        fila = input("\nSelecciona la Fila(1,2,3): ")
        if not verificacion_fila(fila):
            print("Fila inválida")
        else:
            break
    return columna.upper()+fila

def primer_turno():
    opciones = ["X", "0"]
    turno = random.choice(opciones)
    return turno

def verificar_ganador(dictCasillas):
    for opcion in opcionesGanadoras:
        if dictCasillas[opcion[0]] == dictCasillas[opcion[1]] == dictCasillas[opcion[2]] != " ":
            return True
    return False

def juego(dictCasillas):
    turno = primer_turno()
    while True:
        if ' ' in dictCasillas.values():
            print(f'\nEl turno es para: {turno}')

            tablero(dictCasillas)

            while True:
                casilla = pedir_casilla()
                if dictCasillas[casilla] == " ":
                    dictCasillas[casilla] = turno
                    break
                print(f"Esa casilla ya está ocupada por {dictCasillas[casilla]}")

            juego_ganado = verificar_ganador(dictCasillas)
            if juego_ganado:
                tablero(dictCasillas)
                print(f'\nFlicidades {turno} eres el Gandor!')
                break

            turno = "X" if turno == "0" else "0"
        else:
            print("Empate, nadie gana")
            break


def main():
    print("""
    ╔══════════════════════════════════════════╗
    ║  🎮  ¡BIENVENIDO AL RETO SUPREMO!  🎮    ║
    ╠══════════════════════════════════════════╣
    ║  Prepárate para la batalla definitiva de ║
    ║           🧠 INGENIO Y ESTRATEGIA 🧠     ║
    ║                                          ║
    ║                                          ║
    ║                                          ║
    ║          🎯 TRES EN RAYA  🎯             ║
    ╚══════════════════════════════════════════╝
    """)
    while True:
        dictCasillas = {"A1": " ", "B1": " ", "C1": " ",
                        "A2": " ", "B2": " ", "C2": " ",
                        "A3": " ", "B3": " ", "C3": " "}

        juego(dictCasillas)

        while True:
            seguir = input("¿Otra Ronda? (S\\N): ")
            if seguir.upper() == "S" or seguir.upper() == "N":
                break
            print("Opción inválida")

        if seguir.upper() == "N":
            break



main()