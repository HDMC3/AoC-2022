# __--- Día 5: Pilas de suministros ---__

> https://adventofcode.com/2022/day/5

La expedición puede partir tan pronto como se hayan descargado los suministros finales de los barcos. Los suministros se almacenan en pilas de cajas marcadas, pero debido a que los suministros necesarios están enterrados debajo de muchas otras cajas, es necesario reorganizar las cajas.

El barco tiene una grúa de carga gigante capaz de mover cajas entre pilas. Para asegurarse de que ninguna de las cajas se aplaste o se caiga, el operador de la grúa las reacomodará en una serie de pasos cuidadosamente planificados. Después de reorganizar las cajas, las cajas deseadas estarán en la parte superior de cada pila.

Los Elfos no quieren interrumpir a la operadora de la grúa durante este delicado procedimiento, pero se olvidaron de preguntarle qué caja terminará dónde, y quieren estar listos para descargarlas lo antes posible para poder embarcar.

Sin embargo, tienen un dibujo de las pilas iniciales de cajas y el procedimiento de reorganización (su entrada de rompecabezas). Por ejemplo:

```
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

mover 1 de 2 a 1
mover 3 de 1 a 3
mover 2 de 2 a 1
mover 1 de 1 a 2
```

En este ejemplo, hay tres pilas de cajas. La pila 1 contiene dos cajas: la caja `Z` está en la parte inferior y la caja `N` está en la parte superior. La pila 2 contiene tres cajas; de abajo hacia arriba, son las cajas `M`, `C` y `D`. Finalmente, la pila 3 contiene una sola caja, `P`.

Luego, se da el procedimiento de reordenamiento. En cada paso del procedimiento, se mueve una cantidad de cajas de una pila a otra pila diferente. En el primer paso del procedimiento de reorganización anterior, se mueve una caja de la pila 2 a la pila 1, lo que da como resultado esta configuración:

```
[D]
[N] [C]
[Z] [M] [P]
 1   2   3
```
  
En el segundo paso, se mueven tres cajas de la pila 1 a la pila 3. Las cajas se mueven __de una en una__, de modo que la primera caja que se mueve (`D`) termina debajo de la segunda y la tercera caja:

```
        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3

```
Luego, ambas cajas se mueven de la pila 2 a la pila 1. Nuevamente, debido a que las cajas se mueven __una a la vez__, la caja `C` termina debajo de la caja `M`:

```
        [Z]
        [N]
[M]     [D]
[C]     [P] 
 1   2   3
```

Finalmente, se mueve una caja de la pila 1 a la pila 2:

```
        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3
```

Los Elfos solo necesitan saber qué caja terminará en la parte superior de cada pila; en este ejemplo, las cajas superiores son `C` en la pila 1, `M` en la pila 2 y `Z` en la pila 3, por lo que debe combinarlas y dar a los Elfos el mensaje __`CMZ`__.

__Después de que se completa el procedimiento de reordenamiento, ¿qué caja termina en la parte superior de cada pila?__


## __--- Segunda parte ---__
Mientras observa al operador de la grúa reorganizar hábilmente las cajas, nota que el proceso no sigue su predicción.

Un poco de lodo estaba cubriendo la escritura en el costado de la grúa, y rápidamente lo limpiaste. La grúa no es una CrateMover 9000, es una CrateMover 9001.

El CrateMover 9001 se destaca por muchas características nuevas y emocionantes: aire acondicionado, asientos de cuero, un portavasos adicional y la capacidad de levantar y mover varias cajas a la vez.

Nuevamente, considerando el ejemplo anterior, las cajas comienzan con la misma configuración:

```
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3
```

Mover una sola caja de la pila 2 a la pila 1 se comporta igual que antes:

```
[D]
[N] [C]
[Z] [M] [P]
 1   2   3
```

Sin embargo, la acción de mover tres cajas de la pila 1 a la pila 3 significa que esas tres cajas movidas permanecen en el mismo orden, lo que da como resultado esta nueva configuración:

```
        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3
```

Luego, cuando ambas cajas se mueven de la pila 2 a la pila 1, también conservan su orden:

```
        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3
```

Finalmente, una sola caja todavía se mueve de la pila 1 a la pila 2, pero ahora es la caja `C` la que se mueve:

```
        [D]
        [N]
        [Z]
[M] [C] [V]
 1   2   3
```

En este ejemplo, el CrateMover 9001 ha colocado las cajas en un orden totalmente diferente: `MCD`.

__Antes de que finalice el proceso de reorganización, actualice su simulación para que los Elfos sepan dónde deben pararse para estar listos para descargar los suministros finales. Después de que se completa el procedimiento de reordenamiento, ¿qué caja termina en la parte superior de cada pila?__