# __--- Día 3: Reorganización de Mochilas ---__

> https://adventofcode.com/2022/day/3

Un elfo tiene el importante trabajo de cargar todas las mochilas con suministros para el viaje a la jungla. Desafortunadamente, ese duende no siguió del todo las instrucciones de empaque, por lo que ahora es necesario reorganizar algunos artículos.

Cada mochila tiene dos grandes compartimentos. Todos los artículos de un tipo determinado deben ir exactamente en uno de los dos compartimentos. El duende que hizo el equipaje no siguió esta regla para exactamente un tipo de artículo por mochila.

Los Elfos han hecho una lista de todos los elementos que se encuentran actualmente en cada mochila (su entrada de rompecabezas), pero necesitan su ayuda para encontrar los errores. Cada tipo de elemento se identifica con una sola letra minúscula o mayúscula (es decir, a y A se refieren a diferentes tipos de elementos).

La lista de artículos para cada mochila se da como caracteres en una sola línea. Una mochila determinada siempre tiene el mismo número de artículos en cada uno de sus dos compartimentos, por lo que la primera mitad de los caracteres representan artículos en el primer compartimento, mientras que la segunda mitad de los caracteres representan artículos en el segundo compartimento.

Por ejemplo, suponga que tiene la siguiente lista de contenidos de seis mochilas:

```
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
```

- La primera mochila contiene los elementos vJrwpWtwJgWrhcsFMMfFFhFp, lo que significa que su primer compartimento contiene los elementos vJrwpWtwJgWr, mientras que el segundo compartimento contiene los elementos hcsFMMfFFhFp. El único tipo de artículo que aparece en ambos compartimentos es minúscula `p`.
- Los compartimentos de la segunda mochila contienen jqHRNqRjqzjGDLGL y rsFMfFZSrLrFZsSL. El único tipo de artículo que aparece en ambos compartimentos es `L` mayúscula.
- Los compartimentos de la tercera mochila contienen PmmdzqPrV y vPwwTWBwg; el único tipo de elemento común es la `P` mayúscula.
- Los compartimentos de la cuarta mochila solo comparten el tipo de artículo `v`.
- Los compartimentos de la quinta mochila solo comparten el tipo de artículo `t`.
- Los compartimentos de la sexta mochila solo comparten artículos tipo `s`.

Para ayudar a priorizar la reorganización de elementos, cada tipo de elemento se puede convertir en una prioridad:

- Los tipos de elementos en minúsculas de la `a` a la `z` tienen prioridades del __1__ al __26__.
- Los tipos de elementos en mayúsculas de la `A` a la `Z` tienen prioridades de __27__ a __52__.

En el ejemplo anterior, la prioridad del tipo de artículo que aparece en ambos compartimentos de cada mochila es __16 (`p`)__, __38 (`L`)__, __42 (`P`)__, __22 (`v`)__, __20 (`t`)__ y __19 (`s`)__ ; la suma de estos es __157__.

__Encuentra el tipo de artículo que aparece en ambos compartimentos de cada mochila. ¿Cuál es la suma de las prioridades de esos tipos de elementos?__


## __--- Segunda parte ---__
Cuando termine de identificar los elementos extraviados, los Elfos se acercarán a usted con otro problema.

Por seguridad, los Elfos se dividen en grupos de tres. Cada Elfo lleva una insignia que identifica a su grupo. Para mayor eficiencia, dentro de cada grupo de tres Elfos, la insignia es el único tipo de elemento que llevan los tres Elfos. Es decir, si la insignia de un grupo es un artículo de tipo B, entonces los tres Elfos tendrán un artículo de tipo B en algún lugar de su mochila y, como máximo, dos de los Elfos llevarán cualquier otro tipo de artículo.

El problema es que alguien se olvidó de poner la etiqueta de autenticidad actualizada de este año en las insignias. Es necesario sacar todas las insignias de las mochilas para poder colocar las nuevas pegatinas de autenticidad.

Además, nadie anotó qué tipo de elemento corresponde a las insignias de cada grupo. La única forma de saber qué tipo de elemento es el correcto es encontrar el tipo de elemento que es común entre los tres Elfos en cada grupo.

Cada conjunto de tres líneas en su lista corresponde a un solo grupo, pero cada grupo puede tener un tipo de elemento de insignia diferente. Entonces, en el ejemplo anterior, las mochilas del primer grupo son las primeras tres líneas:

```
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
```

Y las mochilas del segundo grupo son las siguientes tres líneas:

```
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
```

En el primer grupo, el único tipo de artículo que aparece en las tres mochilas es la `r` minúscula; estas deben ser sus insignias. En el segundo grupo, su tipo de elemento de insignia debe ser `Z`.

Todavía se deben encontrar prioridades para estos artículos para organizar los esfuerzos de colocación de calcomanías: aquí, son __18 (`r`)__ para el primer grupo y __52 (`Z`)__ para el segundo grupo. La suma de estos es __70__.

__Encuentra el tipo de elemento que corresponde a las insignias de cada grupo de tres Elfos. ¿Cuál es la suma de las prioridades de esos tipos de elementos?__