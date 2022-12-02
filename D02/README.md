# --- Día 2: Piedra, Papel, Tijeras ---

> https://adventofcode.com/2022/day/2

Los Elfos comienzan a establecer un campamento en la playa. Para decidir qué carpa estará más cerca del almacén de refrigerios, ya está en marcha un torneo gigante de Piedra, papel o tijera.

Rock Paper Scissors es un juego entre dos jugadores. Cada juego contiene muchas rondas; en cada ronda, los jugadores eligen simultáneamente uno de piedra, papel o tijera usando una forma de mano. __Luego, se selecciona un ganador para esa ronda: Roca derrota a Tijeras, Tijeras derrota a Papel y Papel derrota a Roca. Si ambos jugadores eligen la misma forma, la ronda termina en empate.__

Agradecido por tu ayuda ayer, un Elfo te da una __guía de estrategia encriptada (tu entrada de rompecabezas)__ que dicen que seguramente te ayudará a ganar. "La primera columna es lo que tu oponente va a jugar: __A para Piedra, B para Papel y C para Tijeras.__ La segunda columna--" De repente, el Elfo es llamado para ayudar con la tienda de alguien.

La segunda columna, razonas, debe ser lo que debe tocar en respuesta: __X para Piedra, Y para Papel y Z para Tijeras.__ Ganar cada vez sería sospechoso, por lo que las respuestas deben haber sido cuidadosamente elegidas.

El ganador de todo el torneo es el jugador con la puntuación más alta. Su puntaje total es la suma de sus puntajes para cada ronda. __El puntaje de una sola ronda es el puntaje de la forma que seleccionó (1 para Piedra, 2 para Papel y 3 para Tijeras) más el puntaje para el resultado de la ronda (0 si perdió, 3 si la ronda fue un empate , y 6 si ganaste).__

Como no puedes estar seguro de si el Elfo está tratando de ayudarte o de engañarte, debes calcular la puntuación que obtendrías si siguieras la guía de estrategia.

Por ejemplo, suponga que le dieron la siguiente guía de estrategia:

```
A Y
B X
C Z
```

Esta guía de estrategia predice y recomienda lo siguiente:

- En la primera ronda, tu oponente elegirá Roca (A) y tú debes elegir Papel (Y). Esto termina en una victoria para ti con una puntuación de 8 (2 porque elegiste Papel + 6 porque ganaste).
- En la segunda ronda, tu oponente elegirá Papel (B) y tú debes elegir Roca (X). Esto termina en una pérdida para ti con una puntuación de 1 (1 + 0).
- La tercera ronda es un empate con ambos jugadores eligiendo Tijeras, lo que le da una puntuación de 3 + 3 = 6.

En este ejemplo, si siguiera la guía de estrategia, obtendría una puntuación total de 15 (8 + 1 + 6).

__¿Cuál sería su puntaje total si todo sale exactamente de acuerdo con su guía de estrategia?__


## __--- Segunda parte ---__

El elfo termina de ayudar con la tienda y vuelve a ti sigilosamente. "De todos modos, la segunda columna dice cómo debe terminar la ronda: __X significa que debes perder, Y significa que debes terminar la ronda en un empate y Z significa que debes ganar. ¡Buena suerte!"__

La puntuación total todavía se calcula de la misma manera, pero ahora debe averiguar qué forma elegir para que la ronda termine como se indica. El ejemplo anterior ahora es así:

- En la primera ronda, tu oponente elegirá Rock (A), y necesitas que la ronda termine en tablas (Y), así que también eliges Rock. Esto le da una puntuación de 1 + 3 = 4.
- En la segunda ronda, tu oponente elegirá Papel (B) y tú eliges Roca, por lo que perderás (X) con una puntuación de 1 + 0 = 1.
- En la tercera ronda, derrotarás a las Tijeras de tu oponente con Rock por una puntuación de 1 + 6 = 7.

Ahora que está descifrando correctamente la guía de estrategia ultrasecreta, obtendrá una puntuación total de 12.

__Siguiendo las instrucciones del duende para la segunda columna, ¿cuál sería tu puntaje total si todo sale exactamente de acuerdo con tu guía de estrategia?__