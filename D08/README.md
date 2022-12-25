# __--- Día 8: Casa del árbol de árboles ---__

> https://adventofcode.com/2022/day/8

La expedición se encuentra con un parche peculiar de árboles altos, todos plantados cuidadosamente en una cuadrícula. Los elfos explican que una expedición anterior plantó estos árboles como un esfuerzo de reforestación. Ahora, tienen curiosidad si esta sería una buena ubicación para una casa en el árbol.

Primero, determine si hay suficiente cubierta de árbol aquí para mantener __oculta__ una casa de árbol. Para hacer esto, debe contar la cantidad de árboles que son __visibles desde fuera de la cuadrícula__ al mirar directamente a lo largo de una fila o columna.

Los elfos ya han lanzado un quadcopter para generar un mapa con la altura de cada árbol (su entrada de rompecabezas). Por ejemplo:

```
30373
25512
65332
33549
35390
```

Cada árbol se representa como un solo dígito cuyo valor es su altura, donde `0` es el más corto y `9` es el más alto.

Un árbol es __visible__ si todos los otros árboles entre él y un borde de la cuadrícula son más __cortos__ que él. Solo considere árboles en la misma fila o columna; Es decir, solo mira hacia arriba, hacia abajo, la izquierda o la derecha desde cualquier árbol dado.

Todos los árboles alrededor del borde de la cuadrícula son __visibles__, dado que ya están en el borde, no hay árboles para bloquear la vista. En este ejemplo, eso solo deja el __interior nueve árboles__ para considerar:

- El `5` superior izquierda es __visible__ desde la izquierda y la parte superior. (No es visible desde la derecha o el fondo ya que otros árboles de altura `5` están en el camino).
- El medio superior `5` es __visible__ de arriba y hacia la derecha.
- El superior derecho `1` no es visible desde ninguna dirección; Para que sea visible, solo necesitaría árboles de altura __0__ entre él y un borde.
- El `5` medio izquierdo es visible, pero solo desde la derecha.
- El centro `3` no es visible desde ninguna dirección; Para que sea visible, necesitaría haber solo árboles de la máxima altura __2__ entre él y un borde.
- El medio derecho `3` es __visible__ desde la derecha.
- En la fila inferior, el medio `5` es __visible__, pero los `3` y `4` no lo son.

Con 16 árboles visibles en el borde y otros 5 visibles en el interior, un total de __`21`__ árboles son visibles en este acuerdo.

__Considere su mapa; ¿Cuántos árboles son visibles desde fuera de la red?__


## __--- Segunda parte ---__

Contentos con la cantidad de árboles disponibles, los Elfos solo necesitan saber cuál es el mejor lugar para construir su casa en el árbol: les gustaría poder ver muchos árboles.

Para medir la distancia de visualización desde un árbol dado, mire hacia arriba, abajo, izquierda y derecha desde ese árbol; deténgase si llega a un borde o al primer árbol que tenga la misma altura o más que el árbol en cuestión. (Si un árbol está justo en el borde, al menos una de sus distancias de visualización será cero).

A los Elfos no les importan los árboles distantes más altos que los encontrados por las reglas anteriores; la casa del árbol propuesta tiene grandes aleros para mantenerla seca, por lo que de todos modos no podrían ver más alto que la casa del árbol.

En el ejemplo anterior, considere el __`5`__ del medio en la segunda fila:

```
30373
25512
65332
33549
35390
```

- Mirando hacia arriba, su vista no está bloqueada; puede ver 1 árbol (de altura 3).
- Mirando a la izquierda, su vista se bloquea inmediatamente; solo puede ver 1 árbol (de altura 5, justo al lado).
- Mirando a la derecha, su vista no está bloqueada; puede ver 2 árboles.
- Mirando hacia abajo, su vista se bloquea eventualmente; puede ver 2 árboles (uno de altura 3, luego el árbol de altura 5 que bloquea su vista).

La __puntuación escénica__ de un árbol se encuentra multiplicando su distancia de visualización en cada una de las cuatro direcciones. Para este árbol, esto es __`4`__ (se encuentra al multiplicar `1 * 1 * 2 * 2`).

Sin embargo, puedes hacerlo aún mejor: considera el árbol de altura `5` en el medio de la cuarta fila:

```
30373
25512
65332
33549
35390
```

- Mirando hacia arriba, su vista está bloqueada en __`2`__ árboles (por otro árbol con una altura de `5`).
- Mirando a la izquierda, su vista no está bloqueada; puede ver __`2`__ árboles.
- Mirando hacia abajo, su vista tampoco está bloqueada; puede ver __`1`__ árbol.
- Mirando a la derecha, su vista está bloqueada en __`2`__ árboles (por un árbol enorme de altura `9`).

La puntuación escénica de este árbol es __`8`__ (`2 * 2 * 1 * 2`); este es el lugar ideal para la casa del árbol.

__Considere cada árbol en su mapa. ¿Cuál es la puntuación escénica más alta posible para cualquier árbol?__