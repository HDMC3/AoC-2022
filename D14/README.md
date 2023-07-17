# **--- Día 14: Embalse Regolith ---**

¡La señal de socorro te lleva a una cascada gigante! En realidad, espera - la señal parece venir de la propia cascada, y eso no tiene ningún sentido. Sin embargo, te das cuenta de que hay un pequeño camino **detrás** de la cascada.

Corrección: ¡la señal de socorro te lleva detrás de una cascada gigante! Parece que hay un gran sistema de cuevas aquí, y la señal definitivamente lleva más adentro.

Cuando empiezas a adentrarte en el subsuelo, sientes que el suelo retumba por un momento. La arena empieza a entrar en la cueva. Si no descubres rápidamente adónde va la arena, ¡podrías quedar atrapado!

Afortunadamente, tu familiaridad con el análisis de la trayectoria del material que cae te resultará muy útil. Escaneas un corte vertical bidimensional de la cueva por encima de ti (la entrada de tu puzzle) y descubres que en su mayor parte es **aire** con estructuras hechas de **roca**.

Tu escáner traza la trayectoria de cada estructura de roca sólida e informa de las coordenadas `x,y` que forman la trayectoria, donde `x` representa la distancia a la derecha e `y` representa la distancia hacia abajo. Cada trayectoria aparece como una única línea de texto en la exploración. Después del primer punto de cada trayectoria, cada punto indica el final de una línea recta horizontal o vertical que debe trazarse desde el punto anterior. Por ejemplo:

```
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
```

Este escaneo significa que hay dos caminos de roca; el primer camino consiste en dos líneas rectas, y el segundo camino consiste en tres líneas rectas. (Concretamente, el primer camino consiste en una línea de roca desde `498,4` hasta `498,6` y otra línea de roca desde `498,6` hasta `496,6`).

La arena entra en la cueva desde el punto `500,0`.

Dibujando la roca como `#`, el aire como `.`, y la fuente de la arena como `+`, esto se convierte en:

```
  4     5  5
  9     0  0
  4     0  3
0 ......+...
1 ..........
2 ..........
3 ..........
4 ....#...##
5 ....#...#.
6 ..###...#.
7 ........#.
8 ........#.
9 #########.
```

La arena se produce **una unidad a la vez**, y la siguiente unidad de arena no se produce hasta que la unidad de arena anterior se detiene. Una unidad de arena es lo suficientemente grande como para llenar una baldosa de aire en su exploración.

Una unidad de arena siempre cae **un escalón hacia abajo** si es posible. Si la casilla inmediatamente inferior está bloqueada (por roca o arena), la unidad de arena intenta moverse en diagonal **un paso hacia abajo y a la izquierda**. Si la baldosa está bloqueada, la unidad de arena intenta moverse en diagonal **un paso hacia abajo y a la derecha**. La arena sigue moviéndose mientras pueda hacerlo, a cada paso intenta moverse hacia abajo, luego hacia abajo-izquierda, luego hacia abajo-derecha. Si se bloquean los tres destinos posibles, la unidad de arena **se detiene** y deja de moverse, momento en el que se crea la siguiente unidad de arena en el origen.

Por lo tanto, si dibujamos la arena que se ha detenido como `o`, la primera unidad de arena simplemente cae hacia abajo y se detiene:

```
......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
........#.
......o.#.
#########.
```

La segunda unidad de arena cae hacia abajo, aterriza sobre la primera y se detiene a su izquierda:

```
......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
........#.
.....oo.#.
#########.
```

Después de que un total de cinco unidades de arena se hayan posado, forman este patrón:

```
......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
......o.#.
....oooo#.
#########.
```

Después de un total de 22 unidades de arena:

```
......+...
..........
......o...
.....ooo..
....#ooo##
....#ooo#.
..###ooo#.
....oooo#.
...ooooo#.
#########.
```

Por último, sólo dos unidades más de arena pueden llegar a reposar:

```
......+...
..........
......o...
.....ooo..
....#ooo##
...o#ooo#.
..###ooo#.
....oooo#.
.o.ooooo#.
#########.
```

Una vez que las **`24`** unidades de arena mostradas arriba se han detenido, toda la arena adicional fluye por la parte inferior, cayendo en el vacío infinito. Sólo por diversión, el camino que toma cualquier arena nueva antes de caer para siempre se muestra aquí con `~`:

```
.......+...
.......~...
......~o...
.....~ooo..
....~#ooo##
...~o#ooo#.
..~###ooo#.
..~..oooo#.
.~o.ooooo#.
~#########.
~..........
~..........
~..........
```

Utilizando tu escáner, simula la caída de la arena. **¿Cuántas unidades de arena se detienen antes de que la arena empiece a fluir hacia el abismo?**


## __--- Segunda parte ---__

Te das cuenta de que has leído mal el escáner. No hay un vacío infinito en la parte inferior del escáner - ¡hay suelo, y estás de pie sobre él!

No tienes tiempo de escanear el suelo, así que supones que el suelo es una línea horizontal infinita con una coordenada `y` igual a __dos más la coordenada__ `y` más alta de cualquier punto de tu escaneo.

En el ejemplo anterior, la coordenada `y` más alta de cualquier punto es `9`, por lo que el suelo está en `y=11`. (Esto es como si su escaneo contuviera una línea horizontal infinita). (Esto es como si su exploración contuviera una ruta de roca extra como `-infinito,11 -> infinito,11`.) Con el suelo añadido, el ejemplo anterior ahora se ve así:

```
        ...........+........
        ....................
        ....................
        ....................
        .........#...##.....
        .........#...#......
        .......###...#......
        .............#......
        .............#......
        .....#########......
        ....................
<-- etc #################### etc -->
```

Para encontrar un lugar seguro, tendrás que simular la caída de arena hasta que una unidad de arena se detenga en `500,0`, bloqueando la fuente por completo y deteniendo el flujo de arena hacia la cueva. En el ejemplo anterior, la situación queda así después de que __`93`__ unidades de arena se hayan detenido:

```
............o............
...........ooo...........
..........ooooo..........
.........ooooooo.........
........oo#ooo##o........
.......ooo#ooo#ooo.......
......oo###ooo#oooo......
.....oooo.oooo#ooooo.....
....oooooooooo#oooooo....
...ooo#########ooooooo...
..ooooo.......ooooooooo..
#########################
```

Utilizando tu escáner, simula la caída de arena hasta que la fuente de la arena se bloquee. __¿Cuántas unidades de arena caen?__