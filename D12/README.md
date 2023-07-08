# **--- Día 12: Algoritmo Hill Climbing ---**

> https://adventofcode.com/2022/day/12

Intentas contactar con los elfos utilizando tu dispositivo portátil, pero el río que estás siguiendo debe estar demasiado bajo para recibir una señal decente.

Le pides al dispositivo un mapa de altura de la zona circundante (la entrada de tu rompecabezas). El mapa de alturas muestra el área local desde arriba dividida en una cuadrícula; la elevación de cada cuadrado de la cuadrícula viene dada por una sola letra minúscula, donde `a` es la elevación más baja, `b` es la siguiente más baja, y así sucesivamente hasta la elevación más alta, `z`.

En el mapa de alturas también se incluyen marcas para tu posición actual (`S`) y la ubicación que debería recibir la mejor señal (`E`). Tu posición actual (`S`) tiene la elevación `a`, y la ubicación que debería obtener la mejor señal (`E`) tiene la elevación `z`.

Te gustaría llegar a `E`, pero para ahorrar energía, debes hacerlo en el **menor número de pasos posible**. En cada paso, puedes moverte exactamente una casilla hacia arriba, hacia abajo, hacia la izquierda o hacia la derecha. Para evitar tener que sacar tu equipo de escalada, la elevación de la casilla de destino puede ser **como máximo uno más alta** que la elevación de tu casilla actual; es decir, si tu elevación actual es `m`, podrías dar un paso hasta la elevación `n`, pero no hasta la elevación `o`. (Esto también significa que la elevación de la casilla de destino puede ser mucho más baja que la elevación de tu casilla actual).

Por ejemplo:

```
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
```

Aquí, empiezas en la esquina superior izquierda; tu objetivo está cerca del centro. Puedes empezar moviéndote hacia abajo o hacia la derecha, pero al final tendrás que dirigirte hacia la `e` de la parte inferior. Desde ahí, puedes girar en espiral hasta la meta:

```
v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^
```

En el diagrama anterior, los símbolos indican si el camino sale de cada casilla moviéndose hacia arriba (`^`), hacia abajo (`v`), a la izquierda (`<`) o a la derecha (`>`). La casilla que debería recibir la mejor señal sigue siendo `E`, y `.` marca las casillas no visitadas.

Este camino llega a la meta en **`31`** pasos, el menor número posible.

**¿Cuál es el menor número de pasos necesarios para desplazarse desde la posición actual hasta el lugar que debería recibir la mejor señal?**


## __--- Segunda parte ---__

Mientras subes la colina, sospechas que los elfos querrán convertir esto en una ruta de senderismo. Sin embargo, el comienzo no es muy pintoresco; tal vez puedas encontrar un punto de partida mejor.

Para maximizar el ejercicio durante la caminata, el sendero debe comenzar lo más bajo posible: elevación `a`. La meta sigue siendo la plaza marcada con una `E`. Sin embargo, el sendero debe seguir siendo directo, dando el menor número de pasos para llegar a su meta. Por lo tanto, tendrás que encontrar el camino más corto desde **cualquier cuadrado en la elevación a** hasta el cuadrado marcado con `E`.

Considera de nuevo el ejemplo anterior:

```
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
```

Ahora, hay seis opciones para la posición inicial (cinco marcadas con la letra `a`, más la casilla marcada con la letra `S` que cuenta como situada en la elevación `a`). Si empiezas en el cuadrado de abajo a la izquierda, podrás alcanzar la meta más rápidamente:

```
...v<<<<
...vv<<^
...v>E^^
.>v>>>^^
>^>>>>>^
```

Este camino alcanza la meta en sólo **`29`** pasos, el menor número posible.

**¿Cuál es el menor número de pasos necesarios para desplazarse partiendo de cualquier casilla con elevación `a` hasta el lugar que debe recibir la mejor señal?**