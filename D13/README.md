# __--- Día 13: Señal de socorro ---__

> https://adventofcode.com/2022/day/13

Subes la colina y vuelves a intentar contactar con los Elfos. Sin embargo, recibes una señal que no esperabas: **una señal de socorro**.

Tu dispositivo portátil aún no debe funcionar correctamente; los paquetes de la señal de socorro se descodificaron **fuera de orden**. Tendrás que reordenar la lista de paquetes recibidos (la entrada de tu rompecabezas) para descodificar el mensaje.

Tu lista consta de pares de paquetes; los pares están separados por una línea en blanco. Tienes que identificar **cuántos pares de paquetes están en el orden correcto**.

Por ejemplo:

```
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
```

Los paquetes de datos están formados por listas y números enteros. Cada lista empieza por `[`, termina por `]` y contiene cero o más valores separados por comas (enteros u otras listas). Cada paquete es siempre una lista y aparece en su propia línea.

Cuando se comparan dos valores, el primero se llama **izquierdo** y el segundo **derecho**. Entonces:

- Si **ambos valores son enteros**, el **entero inferior** debe ir primero. Si el entero de la izquierda es menor que el entero de la derecha, las entradas están en el orden correcto. Si el entero de la izquierda es mayor que el entero de la derecha, las entradas no están en el orden correcto. De lo contrario, las entradas son el mismo número entero; continúe comprobando la siguiente parte de la entrada.

- Si **ambos valores son listas**, compare el primer valor de cada lista, luego el segundo valor, y así sucesivamente. Si la lista de la izquierda se queda sin elementos primero, las entradas están en el orden correcto. Si la lista de la derecha se queda sin elementos primero, las entradas no están en el orden correcto. Si las listas tienen la misma longitud y ninguna comparación toma una decisión sobre el orden, continúa comprobando la siguiente parte de la entrada.

- Si **exactamente un valor es un entero**, convierta el entero en una lista que contenga ese entero como único valor y vuelva a intentar la comparación. Por ejemplo, si se comparan `[0,0,0]` y `2`, convierta el valor derecho a `[2]` (una lista que contenga `2`); el resultado se encuentra entonces comparando en su lugar `[0,0,0]` y `[2]`.

Utilizando estas reglas, puede determinar cuáles de los pares del ejemplo están en el orden correcto:

```
== Par 1 ==
- Compara [1,1,3,1,1] vs [1,1,5,1,1]
  - Compara 1 vs 1
  - Compara 1 vs 1
  - Compara 3 vs 5
    - El lado izquierdo es más pequeño, por lo que las entradas están en el orden correcto


== Par 2 ==
- Compara [[1],[2,3,4]] vs [[1],4]
  - Compara [1] vs [1]
    - Compara 1 vs 1
  - Compara [2,3,4] vs 4
    - Tipos mixtos; convertir a la derecha a [4] y reintentar la comparación
    - Compara [2,3,4] vs [4]
      - Compara 2 vs 4
        - El lado izquierdo es más pequeño, por lo que las entradas están en el orden correcto

== Par 3 ==
- Compara [9] vs [[8,7,6]]
  - Compara 9 vs [8,7,6]
    - Tipos mixtos; convertir a la izquierda a [9] y reintentar la comparación
    - Compara [9] vs [8,7,6]
      - Compara 9 vs 8
        - El lado derecho es más pequeño, por lo que las entradas no están en el orden correcto

== Par 4 ==
- Compara [[4,4],4,4] vs [[4,4],4,4,4]
  - Compara [4,4] vs [4,4]
    - Compara 4 vs 4
    - Compara 4 vs 4
  - Compara 4 vs 4
  - Compara 4 vs 4
  - El lado izquierdo se quedó sin elementos, por lo que las entradas están en el orden correcto

== Par 5 ==
- Compara [7,7,7,7] vs [7,7,7]
  - Compara 7 vs 7
  - Compara 7 vs 7
  - Compara 7 vs 7
  - El lado derecho se quedó sin elementos, por lo que las entradas no están en el orden correcto

== Par 6 ==
- Compara [] vs [3]
  - El lado izquierdo se quedó sin elementos, por lo que las entradas están en el orden correcto

== Par 7 ==
- Compara [[[]]] vs [[]]
  - Compara [[]] vs []
    - El lado derecho se quedó sin elementos, por lo que las entradas no están en el orden correcto

== Par 8 ==
- Compara [1,[2,[3,[4,[5,6,7]]]],8,9] vs [1,[2,[3,[4,[5,6,0]]]],8,9]
  - Compara 1 vs 1
  - Compara [2,[3,[4,[5,6,7]]]] vs [2,[3,[4,[5,6,0]]]]
    - Compara 2 vs 2
    - Compara [3,[4,[5,6,7]]] vs [3,[4,[5,6,0]]]
      - Compara 3 vs 3
      - Compara [4,[5,6,7]] vs [4,[5,6,0]]
        - Compara 4 vs 4
        - Compara [5,6,7] vs [5,6,0]
          - Compara 5 vs 5
          - Compara 6 vs 6
          - Compara 7 vs 0
            - El lado derecho es más pequeño, por lo que las entradas no están en el orden correcto
```

¿Cuáles son los índices de los pares que ya están **en el orden correcto**? (El primer par tiene índice 1, el segundo par tiene índice 2, y así sucesivamente.) En el ejemplo anterior, los pares en el orden correcto son 1, 2, 4 y 6; la suma de estos índices es `13`.

Determina qué pares de paquetes están ya en el orden correcto. **¿Cuál es la suma de los índices de esos pares?**


## __--- Segunda parte ---__

Ahora, sólo necesitas poner **todos los paquetes** en el orden correcto. Ignora las líneas en blanco en tu lista de paquetes recibidos.

El protocolo de señal de socorro también requiere que incluyas dos **paquetes divisores** adicionales:

```
[[2]]
[[6]]
```

Utilizando las mismas reglas que antes, organice todos los paquetes -los de su lista de paquetes recibidos así como los dos paquetes divisores- en el orden correcto.

Para el ejemplo anterior, el resultado de poner los paquetes en el orden correcto es:

```
[]
[[]]
[[[]]]
[1,1,3,1,1]
[1,1,5,1,1]
[[1],[2,3,4]]
[1,[2,[3,[4,[5,6,0]]]],8,9]
[1,[2,[3,[4,[5,6,7]]]],8,9]
[[1],4]
[[2]]
[3]
[[4,4],4,4]
[[4,4],4,4,4]
[[6]]
[7,7,7]
[7,7,7,7]
[[8,7,6]]
[9]
```

Después, localice los paquetes divisores. Para encontrar la **clave de descodificación** de esta señal de socorro, tienes que determinar los índices de los dos paquetes divisores y multiplicarlos. (El primer paquete está en el índice 1, el segundo en el índice 2, etc.) En este ejemplo, los paquetes divisores son el **10º** y el **14º**, por lo que la clave de descodificación es **`140`**.

Organiza todos los paquetes en el orden correcto. **¿Cuál es la clave de descodificación de la señal de socorro?**