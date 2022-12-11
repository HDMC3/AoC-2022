# __--- Día 4: Limpieza del Campamento ---__

> https://adventofcode.com/2022/day/4

Es necesario despejar el espacio antes de que se puedan descargar los últimos suministros de los barcos, por lo que se ha asignado a varios Elfos el trabajo de limpiar secciones del campamento. Cada sección tiene un número de ID único y a cada Elfo se le asigna un rango de ID de sección.

Sin embargo, a medida que algunos Elfos comparan sus asignaciones de sección entre sí, han notado que muchas de las asignaciones se superponen. Para tratar de encontrar superposiciones rápidamente y reducir el esfuerzo duplicado, los Elfos se emparejan y hacen una gran lista de asignaciones de secciones para cada par (su entrada de rompecabezas).

Por ejemplo, considere la siguiente lista de pares de asignación de secciones:

```
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
```

Para los primeros pares, esta lista significa:

- Dentro del primer par de Elfos, al primer Elfo se le asignaron las secciones 2-4 (secciones 2, 3 y 4), mientras que al segundo Elfo se le asignaron las secciones 6-8 (secciones 6, 7, 8).
- A los Elfos del segundo par se les asignaron dos secciones cada uno.
- A los Elfos del tercer par se les asignaron tres secciones cada uno: uno obtuvo las secciones 5, 6 y 7, mientras que el otro también obtuvo 7, más 8 y 9.

Esta lista de ejemplo utiliza ID de sección de un solo dígito para que sea más fácil de dibujar; su lista real puede contener números más grandes. Visualmente, estos pares de asignaciones de secciones se ven así:

```
.234..... 2-4
.....678. 6-8

.23...... 2-3
...45.... 4-5

....567.. 5-7
......789 7-9

.2345678. 2-8
..34567.. 3-7

.....6... 6-6
...456... 4-6

.23456... 2-6
...45678. 4-8
```

Algunas de las parejas han notado que una de sus asignaciones contiene completamente a la otra. Por ejemplo, 2-8 contiene completamente 3-7 y 6-6 está completamente contenido en 4-6. En parejas en las que una tarea contiene completamente a la otra, un Elfo de la pareja estaría limpiando exclusivamente las secciones que su compañero ya estará limpiando, por lo que estas parecen ser las más necesitadas de reconsideración. En este ejemplo, hay 2 de esos pares.

__¿En cuántos pares de asignaciones un rango contiene completamente al otro?__


## __---Segunda parte---__

Parece que todavía hay bastante trabajo duplicado planeado. En cambio, a los Elfos les gustaría saber el número de pares que se superponen.

En el ejemplo anterior, los dos primeros pares (`2-4,6-8` y `2-3,4-5`) no se superponen, mientras que los cuatro pares restantes (`5-7,7-9`, `2-8,3-7`, `6-6,4-6` y `2-6,4-8`) se superponen:

- `5-7,7-9` superposiciones en un solo tramo, `7`.
- `2-8,3-7` se superpone a todas las secciones `3` a `7`.
- `6-6,4-6` superposiciones en un solo tramo, `6`.
- `2-6,4-8` se superpone en las secciones `4`, `5` y `6`.

Entonces, en este ejemplo, el número de pares de asignaciones superpuestas es __`4`__.

__¿En cuántos pares de asignaciones se superponen los rangos?__