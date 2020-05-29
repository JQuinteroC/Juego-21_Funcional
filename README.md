# Juego de 21
## Requerimientos
Se solicita crea un juego de 21 con las cartas del póker, en el paradigma funcional, sin GUI y con las siguientes condiciones:
- El juego se realiza entre la casa y un jugador
- Al iniciar la partida, se le entregan dos cartas a cada participante, la casa muestra solo una de sus cartas
- El jugador podrá pedir una carta o plantarse
     - Si el jugador se planta, se muestra todo el juego
     - En caso de empate ganara la casa
- La casa pedirá cartas hasta sacar 21 o perder

## Desarrollo
Al ser la primera vez que nos afrontamos a este paradigma de programación, el profesor nos ayudo a estructurar los primeros pasos, pero todo se resume en resolver el problema en pequeñas partes que al unirse resuelven el "todo".
Dentro estas partes logramos identificar las siguientes funciones que requería el programa:
- Crear la baraja
- Mezclar la baraja aleatoriamente
- Hallar el valor de una carta
    - En el caso de la carta A, tomar mejor caso (si vale 1 o si vale 11)
- Hallar el valor de todo un mazo
- Asignar un mazo al jugador
- Asignar un mazo al repartidor
- Definir un ganador
Fue a partir de la identificación de estas tareas, que se logro desarrollar el programa, pues cada una termino representando una función a implementar

### Programadores
**[Jose Quintero Cañizalez](https://github.com/JQuinteroC) - *20181020061*** y **[Cristhian Camilo Martinez](https://github.com/Moitas500) - *20181020021***


[![Run on Repl.it](https://repl.it/badge/github/JQuinteroC/Juego-21_Funcional)](https://repl.it/github/JQuinteroC/Juego-21_Funcional)
