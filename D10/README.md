# __--- Día 10: Tubo de rayos catódicos ---__

> https://adventofcode.com/2022/day/10

Evitas las cuerdas, te sumerges en el río y nadas hasta la orilla.

Los Elfos gritan algo acerca de reunirse con ellos río arriba, pero el río es demasiado ruidoso para decir exactamente lo que están diciendo. Terminan de cruzar el puente y desaparecen de la vista.

Situaciones como esta deben ser la razón por la cual los Elfos priorizaron hacer funcionar el sistema de comunicación en su dispositivo portátil. Lo sacas de tu mochila, pero la cantidad de agua que se drena lentamente de una gran grieta en su pantalla te dice que probablemente no será de mucha utilidad inmediata.

¡A menos que pueda diseñar un reemplazo para el sistema de video del dispositivo! Parece ser una especie de pantalla de tubo de rayos catódicos y una CPU simple que son impulsadas por un circuito de reloj preciso. El circuito del reloj marca a un ritmo constante; cada tic se llama un ciclo.

Comience por averiguar la señal que envía la CPU. La CPU tiene un solo registro, `X`, que comienza con el valor `1`. Solo admite dos instrucciones:

- `addx V` tarda __dos ciclos__ en completarse. __Después de dos ciclos__, el registro `X` aumenta en el valor `V`. (`V` puede ser negativo).
- `noop` tarda __un ciclo__ en completarse. No tiene otro efecto.

La CPU usa estas instrucciones en un programa (su entrada de rompecabezas) para, de alguna manera, decirle a la pantalla qué dibujar.

Considere el siguiente pequeño programa:

```
noop
addx 3
addx -5
```

La ejecución de este programa se desarrolla de la siguiente manera:

- Al comienzo del primer ciclo, la instrucción `noop` comienza a ejecutarse. Durante el primer ciclo, `X` es `1`. Después del primer ciclo, la instrucción `noop` termina de ejecutarse, sin hacer nada.
- Al comienzo del segundo ciclo, la instrucción `addx 3` comienza a ejecutarse. Durante el segundo ciclo, `X` sigue siendo `1`.
- Durante el tercer ciclo, `X` sigue siendo `1`. Después del tercer ciclo, la instrucción `addx 3` termina de ejecutarse y establece `X` en `4`.
- Al comienzo del cuarto ciclo, la instrucción `addx -5` comienza a ejecutarse. Durante el cuarto ciclo, `X` sigue siendo `4`.
- Durante el quinto ciclo, `X` sigue siendo `4`. Después del quinto ciclo, la instrucción `addx -5` termina de ejecutarse y establece `X` en `-1`.

Tal vez pueda aprender algo observando el valor del registro `X` durante la ejecución. Por ahora, considere la __intensidad de la señal__ (el número de ciclo multiplicado por el valor del registro `X`) __durante__ el ciclo 20 y cada 40 ciclos posteriores (es decir, durante los ciclos 20, 60, 100, 140, 180 y 220) .

Por ejemplo, considere este programa más grande:

```
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
```

Las intensidades de señal interesantes se pueden determinar de la siguiente manera:

- Durante el ciclo 20, el registro `X` tiene el valor `21`, por lo que la intensidad de la señal es 20 * 21 = __420__. (El ciclo 20 ocurre en medio del segundo `addx -1`, por lo que el valor del registro `X` es el valor inicial, `1` , más todos los demás valores `addx` hasta ese punto: 1 + 15 - 11 + 6 - 3 + 5 - 1 - 8 + 13 + 4 = 21).
- Durante el ciclo 60, el registro `X` tiene el valor `19`, por lo que la intensidad de la señal es 60 * 19 = __1140__.
- Durante el ciclo 100, el registro `X` tiene el valor `18`, por lo que la intensidad de la señal es 100 * 18 = __1800__.
- Durante el ciclo 140, el registro `X` tiene el valor `21`, por lo que la intensidad de la señal es 140 * 21 = __2940__.
- Durante el ciclo 180, el registro `X` tiene el valor `16`, por lo que la intensidad de la señal es 180 * 16 = __2880__.
- Durante el ciclo 220, el registro `X` tiene el valor `18`, por lo que la intensidad de la señal es 220 * 18 = __3960__.

La suma de estas intensidades de señal es __`13140`__.

__Encuentre la intensidad de la señal durante los ciclos 20, 60, 100, 140, 180 y 220. ¿Cuál es la suma de estas seis intensidades de señal?__


## __--- Segunda parte ---__

Parece que el registro `X` controla la posición horizontal de un sprite. Específicamente, el sprite tiene 3 píxeles de ancho y el registro `X` establece la posición horizontal del __medio__ de ese sprite. (En este sistema, no existe la "posición vertical": si la posición horizontal del sprite coloca sus píxeles donde el CRT está dibujando actualmente, esos píxeles se dibujarán).

Cuentas los píxeles en el CRT: 40 de ancho y 6 de alto. Esta pantalla CRT dibuja la fila superior de píxeles de izquierda a derecha, luego la fila debajo y así sucesivamente. El píxel más a la izquierda de cada fila está en la posición `0` y el píxel más a la derecha en cada fila está en la posición `39`.

Al igual que la CPU, el CRT está estrechamente ligado al circuito del reloj: el CRT dibuja __un solo píxel durante cada ciclo__. Representando cada píxel de la pantalla como un `#`, estos son los ciclos durante los cuales se dibujan el primer y último píxel de cada fila:

```
Cycle   1 -> ######################################## <- Cycle  40
Cycle  41 -> ######################################## <- Cycle  80
Cycle  81 -> ######################################## <- Cycle 120
Cycle 121 -> ######################################## <- Cycle 160
Cycle 161 -> ######################################## <- Cycle 200
Cycle 201 -> ######################################## <- Cycle 240
```

Por lo tanto, al cronometrar cuidadosamente las instrucciones de la CPU y las operaciones de dibujo de CRT, debería poder determinar si el sprite es visible en el instante en que se dibuja cada píxel. Si el sprite se coloca de tal manera que uno de sus tres píxeles es el píxel que se está dibujando actualmente, la pantalla produce un __píxel iluminado__ (`#`); de lo contrario, la pantalla deja el __píxel oscuro__ (`.`).

Los primeros píxeles del ejemplo más grande anterior se dibujan de la siguiente manera:

```
Sprite position: ###.....................................

Start cycle   1: begin executing addx 15
During cycle  1: CRT draws pixel in position 0
Current CRT row: #

During cycle  2: CRT draws pixel in position 1
Current CRT row: ##
End of cycle  2: finish executing addx 15 (Register X is now 16)
Sprite position: ...............###......................

Start cycle   3: begin executing addx -11
During cycle  3: CRT draws pixel in position 2
Current CRT row: ##.

During cycle  4: CRT draws pixel in position 3
Current CRT row: ##..
End of cycle  4: finish executing addx -11 (Register X is now 5)
Sprite position: ....###.................................

Start cycle   5: begin executing addx 6
During cycle  5: CRT draws pixel in position 4
Current CRT row: ##..#

During cycle  6: CRT draws pixel in position 5
Current CRT row: ##..##
End of cycle  6: finish executing addx 6 (Register X is now 11)
Sprite position: ..........###...........................

Start cycle   7: begin executing addx -3
During cycle  7: CRT draws pixel in position 6
Current CRT row: ##..##.

During cycle  8: CRT draws pixel in position 7
Current CRT row: ##..##..
End of cycle  8: finish executing addx -3 (Register X is now 8)
Sprite position: .......###..............................

Start cycle   9: begin executing addx 5
During cycle  9: CRT draws pixel in position 8
Current CRT row: ##..##..#

During cycle 10: CRT draws pixel in position 9
Current CRT row: ##..##..##
End of cycle 10: finish executing addx 5 (Register X is now 13)
Sprite position: ............###.........................

Start cycle  11: begin executing addx -1
During cycle 11: CRT draws pixel in position 10
Current CRT row: ##..##..##.

During cycle 12: CRT draws pixel in position 11
Current CRT row: ##..##..##..
End of cycle 12: finish executing addx -1 (Register X is now 12)
Sprite position: ...........###..........................

Start cycle  13: begin executing addx -8
During cycle 13: CRT draws pixel in position 12
Current CRT row: ##..##..##..#

During cycle 14: CRT draws pixel in position 13
Current CRT row: ##..##..##..##
End of cycle 14: finish executing addx -8 (Register X is now 4)
Sprite position: ...###..................................

Start cycle  15: begin executing addx 13
During cycle 15: CRT draws pixel in position 14
Current CRT row: ##..##..##..##.

During cycle 16: CRT draws pixel in position 15
Current CRT row: ##..##..##..##..
End of cycle 16: finish executing addx 13 (Register X is now 17)
Sprite position: ................###.....................

Start cycle  17: begin executing addx 4
During cycle 17: CRT draws pixel in position 16
Current CRT row: ##..##..##..##..#

During cycle 18: CRT draws pixel in position 17
Current CRT row: ##..##..##..##..##
End of cycle 18: finish executing addx 4 (Register X is now 21)
Sprite position: ....................###.................

Start cycle  19: begin executing noop
During cycle 19: CRT draws pixel in position 18
Current CRT row: ##..##..##..##..##.
End of cycle 19: finish executing noop

Start cycle  20: begin executing addx -1
During cycle 20: CRT draws pixel in position 19
Current CRT row: ##..##..##..##..##..

During cycle 21: CRT draws pixel in position 20
Current CRT row: ##..##..##..##..##..#
End of cycle 21: finish executing addx -1 (Register X is now 20)
Sprite position: ...................###..................
```

Permitir que el programa se ejecute hasta su finalización hace que el CRT produzca la siguiente imagen:

```
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
```

__Renderiza la imagen dada por tu programa. ¿Qué ocho letras mayúsculas aparecen en su CRT?__