# __--- Día 7: No queda espacio en el dispositivo ---__

> https://adventofcode.com/2022/day/7

Puede escuchar el canto de los pájaros y las gotas de lluvia golpeando las hojas a medida que avanza la expedición. De vez en cuando, incluso puedes escuchar sonidos mucho más fuertes en la distancia; ¿Qué tamaño tienen los animales aquí, de todos modos?

El dispositivo que te dieron los Elfos tiene problemas con algo más que su sistema de comunicación. Intenta ejecutar una actualización del sistema:

```
$ system-update --please --pretty-please-with-sugar-on-top
Error: No space left on device
```
¿Quizás pueda eliminar algunos archivos para hacer espacio para la actualización?

Navega por el sistema de archivos para evaluar la situación y guardar la salida de terminal resultante (su entrada de rompecabezas). Por ejemplo:

```
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
```

El sistema de archivos consta de un árbol de archivos (datos sin formato) y directorios (que pueden contener otros directorios o archivos). El directorio más externo se llama `/`. Puede navegar por el sistema de archivos, entrar o salir de los directorios y enumerar el contenido del directorio en el que se encuentra actualmente.

Dentro de la salida de la terminal, las líneas que comienzan con `$` son comandos que ejecutó, muy parecido a algunas computadoras modernas:

- `cd` significa cambiar de directorio. Esto cambia qué directorio es el directorio actual, pero el resultado específico depende del argumento:
    - `cd x` se mueve __dentro__ un nivel: busca en el directorio actual el directorio llamado `x` y lo convierte en el directorio actual.
    - `cd ..` se mueve __fuera__ un nivel: encuentra el directorio que contiene el directorio actual, luego convierte ese directorio en el directorio actual.
    - `cd /` cambia el directorio actual al directorio más externo, `/`.
- `ls` significa __lista__. Imprime todos los archivos y directorios contenidos inmediatamente por el directorio actual:
    - `123 abc` significa que el directorio actual contiene un archivo llamado `abc` con tamaño `123`.
    - `dir xyz` significa que el directorio actual contiene un directorio llamado `xyz`.

Dados los comandos y la salida en el ejemplo anterior, puede determinar que el sistema de archivos se ve visualmente así:

```
- / (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)
```

Aquí hay cuatro directorios: `/` (el directorio más externo), `a` y `d` (que están en `/`) y `e` (que está en `a`). Estos directorios también contienen archivos de varios tamaños.

Dado que el disco está lleno, su primer paso probablemente debería ser encontrar directorios que sean buenos candidatos para la eliminación. Para ello, debe determinar el __tamaño total de cada directorio__. El tamaño total de un directorio es la suma de los tamaños de los archivos que contiene, directa o indirectamente. (Los directorios en sí mismos no cuentan como si tuvieran un tamaño intrínseco).

Los tamaños totales de los directorios anteriores se pueden encontrar de la siguiente manera:

- El tamaño total del directorio `e` es __584__ porque contiene un solo archivo `i` de tamaño __584__ y ningún otro directorio.
- El directorio `a` tiene un tamaño total de __94853__ porque contiene archivos `f` (tamaño __29116__), `g` (tamaño __2557__) y `h.lst` (tamaño __62596__), más el archivo `i` indirectamente (`a` contiene `e` que contiene `i`).
- El directorio `d` tiene un tamaño total de __24933642__.
- Como directorio más externo, `/` contiene todos los archivos. Su tamaño total es __48381165__, la suma del tamaño de cada archivo.

Para comenzar, encuentre todos los directorios con un __tamaño total de 100000 como máximo__, luego calcule la suma de sus tamaños totales. En el ejemplo anterior, estos directorios son `a` y `e`; la suma de sus tamaños totales es __95437__ (94853 + 584). (Como en este ejemplo, ¡este proceso puede contar archivos más de una vez!)

__Encuentre todos los directorios con un tamaño total de 100000 como máximo. ¿Cuál es la suma de los tamaños totales de esos directorios?__


## __--- Segunda parte ---__
Ahora, estás listo para elegir un directorio para eliminar.

El espacio total de disco disponible para el sistema de archivos es __`70000000`__. Para ejecutar la actualización, necesita un espacio no utilizado de al menos __`30000000`__. Debe encontrar un directorio que pueda eliminar que libere suficiente espacio para ejecutar la actualización.

En el ejemplo anterior, el tamaño total del directorio más externo (y, por lo tanto, la cantidad total de espacio usado) es `48381165`; Esto significa que el tamaño del espacio no utilizado debe ser actualmente `21618835`, que no es el `30000000` requerido por la actualización. Por lo tanto, la actualización aún requiere un directorio con un tamaño total de al menos `8381165` para eliminar antes de que pueda ejecutarse.

Para lograr esto, tiene las siguientes opciones:

- Eliminar el Directorio `e`, que aumentaría el espacio no utilizado en `584`.
- Eliminar el Directorio `a`, que aumentaría el espacio no utilizado en `94853`.
- Eliminar el Directorio `d`, que aumentaría el espacio no utilizado en `24933642`.
- Eliminar directorio `/`, que aumentaría el espacio no utilizado en `48381165`.

Los directorios `e` y `a` son demasiado pequeños; Eliminarlos no liberaría suficiente espacio. Sin embargo, los directorios `d` y `/` son lo suficientemente grandes. Entre estos, elija el más pequeño: `d`, aumentando el espacio no utilizado para __`24933642`__.

__Encuentre el directorio más pequeño que, si se elimina, liberaría suficiente espacio en el sistema de archivos para ejecutar la actualización. ¿Cuál es el tamaño total de ese directorio?__