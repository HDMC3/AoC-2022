# --- Día 1: Conteo de calorías ---

> https://adventofcode.com/2022/day/1

Los renos de Papá Noel suelen comer comida normal para renos, pero necesitan mucha energía mágica para entregar regalos en Navidad. Por eso, su bocadillo favorito es un tipo especial de carambola que solo crece en lo profundo de la jungla. Los Elfos te han traído en su expedición anual al bosque donde crece la fruta.

Para suministrar suficiente energía mágica, la expedición debe recuperar un mínimo de cincuenta estrellas antes del 25 de diciembre. Aunque los Elfos te aseguran que la arboleda tiene mucha fruta, decides agarrar cualquier fruta que veas por el camino, por si acaso.

Recoge estrellas resolviendo acertijos. Habrá dos rompecabezas disponibles cada día en el calendario de Adviento; el segundo rompecabezas se desbloquea cuando completas el primero. Cada rompecabezas otorga una estrella. ¡Buena suerte!

La jungla debe estar demasiado cubierta de maleza y ser difícil de transitar en vehículos o acceder desde el aire; La expedición de los Elfos tradicionalmente va a pie. A medida que sus barcos se acercan a tierra, los Elfos comienzan a hacer un inventario de sus suministros. Una consideración importante es la comida, en particular, la cantidad de calorías que lleva cada Elfo (su entrada de rompecabezas).

Los Elfos se turnan para anotar el número de Calorías que contienen las distintas comidas, meriendas, raciones, etc. que han traído consigo, un elemento por línea. Cada Elfo separa su propio inventario del inventario del Elfo anterior (si lo hay) con una línea en blanco.

Por ejemplo, supongamos que los Elfos terminan de escribir las Calorías de sus artículos y terminan con la siguiente lista:

```
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
```

Esta lista representa las Calorías de la comida que llevan cinco Elfos:

- El primer Elfo lleva comida con 1000, 2000 y 3000 Calorías, un total de 6000 Calorías.
- El segundo elfo lleva un alimento con 4000 calorías.
- El tercer Elfo lleva comida con 5000 y 6000 Calorías, un total de 11000 Calorías.
- El cuarto Elfo lleva comida con 7000, 8000 y 9000 Calorías, un total de 24000 Calorías.
- El quinto Elfo lleva un alimento con 10000 Calorías.

En caso de que los Elfos tengan hambre y necesiten refrigerios adicionales, necesitan saber a qué Elfo preguntar: les gustaría saber cuántas Calorías lleva el Elfo que lleva la mayor cantidad de Calorías. En el ejemplo anterior, esto es 24000 (llevado por el cuarto Elfo).

__Encuentra al duende que lleva más calorías. ¿Cuántas calorías totales lleva ese elfo?__

## __--- Segunda Parte ---__

Para cuando calculas la respuesta a la pregunta de los Elfos, ya se han dado cuenta de que el Elfo que lleva la mayor cantidad de calorías de comida podría quedarse sin bocadillos.

Para evitar esta situación inaceptable, a los Elfos les gustaría saber el total de Calorías que llevan los tres Elfos que llevan la mayor cantidad de Calorías. De esa manera, incluso si uno de esos Elfos se queda sin bocadillos, todavía tienen dos copias de seguridad.

En el ejemplo anterior, los tres primeros Elfos son el cuarto Elfo (con 24000 Calorías), luego el tercer Elfo (con 11000 Calorías), luego el quinto Elfo (con 10000 Calorías). La suma de las Calorías que llevan estos tres duendes es 45000.

__Encuentra los tres Elfos principales que llevan la mayor cantidad de calorías. ¿Cuántas calorías llevan esos duendes en total?__