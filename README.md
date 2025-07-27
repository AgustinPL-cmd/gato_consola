# 🎮 Tic Tac Toe en Consola - Python 🐍

¡Bienvenido a este simple pero entretenido juego de Tres en Línea (Tic-Tac-Toe) hecho completamente en Python para ejecutarse desde la terminal!

Este proyecto fue creado como ejercicio de programación básica, con enfoque en estructuras de datos, validaciones y lógica de flujo. Ideal para quienes están comenzando con Python y quieren entender cómo estructurar un juego interactivo paso a paso.

---

## 🧠 ¿Cómo se juega?

Dos jugadores se turnan para colocar sus símbolos (`X` y `O`) en un tablero de 3x3, introduciendo la **columna** (`A`, `B`, `C`) y la **fila** (`1`, `2`, `3`) donde quieren colocar su marca.  
El primero que logre alinear tres símbolos en línea recta (horizontal, vertical o diagonal) gana.

Ejemplo del tablero:

-|A|B|C|
1|X|O| |
2| |X|O|
3| | |X|


---

## 🚀 Características del proyecto

- Lógica de turnos alternados entre jugador X y jugador O.
- Validación de entradas (letras y números).
- Prevención de movimientos en casillas ya ocupadas.
- Detección automática del ganador o empate.
- Interfaz en consola limpia y fácil de usar.

---

## 📁 Estructura del código

- `dictCasillas`: Diccionario que almacena el estado de cada casilla (vacía o con un símbolo).
- `opcionesGanadoras`: Lista de combinaciones ganadoras posibles.
- `tablero()`: Muestra el estado actual del tablero.
- `verificacion_col()` y `verificacion_fila()`: Validan que la entrada del usuario sea correcta.
- `pedir_casilla()`: Solicita la jugada al usuario y valida el input.
- `verificar_ganador()`: Revisa si existe una combinación ganadora.

---

## ⚙️ Cómo ejecutarlo

1. Asegúrate de tener Python 3 instalado.
2. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/tic-tac-toe-python.git
