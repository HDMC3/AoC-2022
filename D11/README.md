# **--- Día 11: Monkey in the Middle ---**

> https://adventofcode.com/2022/day/11

Cuando finalmente empiezas a subir río arriba, te das cuenta de que tu mochila es mucho más liviana de lo que recuerdas. Justo en ese momento, uno de los artículos de tu mochila sale volando por encima de tu cabeza. ¡Los monos están jugando Keep Away con tus cosas perdidas!

Para recuperar tus cosas, debes poder predecir dónde arrojarán los monos tus artículos. Después de una cuidadosa observación, te das cuenta de que los monos operan en función de **lo preocupado que estés por cada elemento**.

Tomas algunas notas (tu entrada de rompecabezas) sobre los elementos que cada mono tiene actualmente, qué tan preocupado estás por esos elementos y cómo el mono toma decisiones en función de tu nivel de preocupación. Por ejemplo:

```
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
```

Cada mono tiene varios atributos:

-   `Starting items`: enumeran tu **nivel de preocupación** para cada artículo que el mono tiene actualmente en el orden en que serán inspeccionados.
-   `Operation`: muestra cómo cambia tu nivel de preocupación cuando ese mono inspecciona un artículo. (Una operación como `nuevo = viejo * 5` significa que tu nivel de preocupación después de que el mono inspeccionó el artículo es cinco veces mayor que tu nivel de preocupación antes de la inspección).
-   `Test` muestra cómo el mono usa tu nivel de preocupación para decidir dónde arrojar un objeto a continuación.
    -   `If true`: muestra lo que sucede con un elemento si la `Prueba` es verdadera.
    -   `If false`: muestra lo que sucede con un elemento si la `Prueba` es falsa.

Después de que cada mono inspeccione un artículo pero antes de que pruebe tu nivel de preocupación, tu alivio de que la inspección del mono no dañó el artículo hace que tu nivel de preocupación se **divida por tres** y se redondee al número entero más cercano.

Los monos se turnan para inspeccionar y tirar objetos. En el **turno** de un solo mono, inspecciona y arroja todos los artículos que tiene en sus manos, uno a la vez y en el orden indicado. El mono `0` va primero, luego el mono `1`, y así sucesivamente hasta que cada mono haya tenido un turno. El proceso en el que cada mono da un solo turno se llama **ronda**.

Cuando un mono arroja un artículo a otro mono, el artículo va al **final** de la lista del mono receptor. Un mono que comienza una ronda sin artículos podría terminar inspeccionando y arrojando muchos artículos cuando llegue su turno. Si un mono no tiene objetos al comienzo de su turno, su turno termina.

En el ejemplo anterior, la primera ronda procede de la siguiente manera:

```
Monkey 0:
  Monkey inspects an item with a worry level of 79.
    Worry level is multiplied by 19 to 1501.
    Monkey gets bored with item. Worry level is divided by 3 to 500.
    Current worry level is not divisible by 23.
    Item with worry level 500 is thrown to monkey 3.
  Monkey inspects an item with a worry level of 98.
    Worry level is multiplied by 19 to 1862.
    Monkey gets bored with item. Worry level is divided by 3 to 620.
    Current worry level is not divisible by 23.
    Item with worry level 620 is thrown to monkey 3.
Monkey 1:
  Monkey inspects an item with a worry level of 54.
    Worry level increases by 6 to 60.
    Monkey gets bored with item. Worry level is divided by 3 to 20.
    Current worry level is not divisible by 19.
    Item with worry level 20 is thrown to monkey 0.
  Monkey inspects an item with a worry level of 65.
    Worry level increases by 6 to 71.
    Monkey gets bored with item. Worry level is divided by 3 to 23.
    Current worry level is not divisible by 19.
    Item with worry level 23 is thrown to monkey 0.
  Monkey inspects an item with a worry level of 75.
    Worry level increases by 6 to 81.
    Monkey gets bored with item. Worry level is divided by 3 to 27.
    Current worry level is not divisible by 19.
    Item with worry level 27 is thrown to monkey 0.
  Monkey inspects an item with a worry level of 74.
    Worry level increases by 6 to 80.
    Monkey gets bored with item. Worry level is divided by 3 to 26.
    Current worry level is not divisible by 19.
    Item with worry level 26 is thrown to monkey 0.
Monkey 2:
  Monkey inspects an item with a worry level of 79.
    Worry level is multiplied by itself to 6241.
    Monkey gets bored with item. Worry level is divided by 3 to 2080.
    Current worry level is divisible by 13.
    Item with worry level 2080 is thrown to monkey 1.
  Monkey inspects an item with a worry level of 60.
    Worry level is multiplied by itself to 3600.
    Monkey gets bored with item. Worry level is divided by 3 to 1200.
    Current worry level is not divisible by 13.
    Item with worry level 1200 is thrown to monkey 3.
  Monkey inspects an item with a worry level of 97.
    Worry level is multiplied by itself to 9409.
    Monkey gets bored with item. Worry level is divided by 3 to 3136.
    Current worry level is not divisible by 13.
    Item with worry level 3136 is thrown to monkey 3.
Monkey 3:
  Monkey inspects an item with a worry level of 74.
    Worry level increases by 3 to 77.
    Monkey gets bored with item. Worry level is divided by 3 to 25.
    Current worry level is not divisible by 17.
    Item with worry level 25 is thrown to monkey 1.
  Monkey inspects an item with a worry level of 500.
    Worry level increases by 3 to 503.
    Monkey gets bored with item. Worry level is divided by 3 to 167.
    Current worry level is not divisible by 17.
    Item with worry level 167 is thrown to monkey 1.
  Monkey inspects an item with a worry level of 620.
    Worry level increases by 3 to 623.
    Monkey gets bored with item. Worry level is divided by 3 to 207.
    Current worry level is not divisible by 17.
    Item with worry level 207 is thrown to monkey 1.
  Monkey inspects an item with a worry level of 1200.
    Worry level increases by 3 to 1203.
    Monkey gets bored with item. Worry level is divided by 3 to 401.
    Current worry level is not divisible by 17.
    Item with worry level 401 is thrown to monkey 1.
  Monkey inspects an item with a worry level of 3136.
    Worry level increases by 3 to 3139.
    Monkey gets bored with item. Worry level is divided by 3 to 1046.
    Current worry level is not divisible by 17.
    Item with worry level 1046 is thrown to monkey 1.
```

Después de la ronda 1, los monos tienen objetos con estos niveles de preocupación:

```
Monkey 0: 20, 23, 27, 26
Monkey 1: 2080, 25, 167, 207, 401, 1046
Monkey 2:
Monkey 3:
```

Los monos 2 y 3 no tienen ningún objeto al final de la ronda; ambos inspeccionaron artículos durante la ronda y los arrojaron todos antes de que terminara la ronda.

Este proceso continúa durante algunas rondas más:

```
After round 2, the monkeys are holding items with these worry levels:
Monkey 0: 695, 10, 71, 135, 350
Monkey 1: 43, 49, 58, 55, 362
Monkey 2:
Monkey 3:

After round 3, the monkeys are holding items with these worry levels:
Monkey 0: 16, 18, 21, 20, 122
Monkey 1: 1468, 22, 150, 286, 739
Monkey 2:
Monkey 3:

After round 4, the monkeys are holding items with these worry levels:
Monkey 0: 491, 9, 52, 97, 248, 34
Monkey 1: 39, 45, 43, 258
Monkey 2:
Monkey 3:

After round 5, the monkeys are holding items with these worry levels:
Monkey 0: 15, 17, 16, 88, 1037
Monkey 1: 20, 110, 205, 524, 72
Monkey 2:
Monkey 3:

After round 6, the monkeys are holding items with these worry levels:
Monkey 0: 8, 70, 176, 26, 34
Monkey 1: 481, 32, 36, 186, 2190
Monkey 2:
Monkey 3:

After round 7, the monkeys are holding items with these worry levels:
Monkey 0: 162, 12, 14, 64, 732, 17
Monkey 1: 148, 372, 55, 72
Monkey 2:
Monkey 3:

After round 8, the monkeys are holding items with these worry levels:
Monkey 0: 51, 126, 20, 26, 136
Monkey 1: 343, 26, 30, 1546, 36
Monkey 2:
Monkey 3:

After round 9, the monkeys are holding items with these worry levels:
Monkey 0: 116, 10, 12, 517, 14
Monkey 1: 108, 267, 43, 55, 288
Monkey 2:
Monkey 3:

After round 10, the monkeys are holding items with these worry levels:
Monkey 0: 91, 16, 20, 98
Monkey 1: 481, 245, 22, 26, 1092, 30
Monkey 2:
Monkey 3:

...

After round 15, the monkeys are holding items with these worry levels:
Monkey 0: 83, 44, 8, 184, 9, 20, 26, 102
Monkey 1: 110, 36
Monkey 2:
Monkey 3:

...

After round 20, the monkeys are holding items with these worry levels:
Monkey 0: 10, 12, 14, 26, 34
Monkey 1: 245, 93, 53, 199, 115
Monkey 2:
Monkey 3:
```

Perseguir a todos los monos a la vez es imposible; Vas a tener que concentrarte en los **dos monos más activos** si quieres tener alguna esperanza de recuperar tus cosas. Cuente el **número total de veces que cada mono inspecciona artículos** en 20 rondas:

```
Monkey 0 inspected items 101 times.
Monkey 1 inspected items 95 times.
Monkey 2 inspected items 7 times.
Monkey 3 inspected items 105 times.
```

En este ejemplo, los dos monos más activos inspeccionaron artículos 101 y 105 veces. El nivel de **negocios de monos** en esta situación se puede encontrar al multiplicarlos: **`10605`**.

**Averigua qué monos perseguir contando cuántos artículos inspeccionan en 20 rondas. ¿Cuál es el nivel de negocio de los monos después de 20 rondas de travesuras simiescas?**

## **--- Segunda parte ---**

Le preocupa que nunca pueda recuperar sus artículos. Tan preocupado, de hecho, que su alivio porque la inspección de un mono no dañó un artículo **ya no hace que su nivel de preocupación se divida por tres**.

Desafortunadamente, ese alivio era todo lo que impedía que sus niveles de preocupación alcanzaran **niveles ridículos**. **Deberá encontrar otra manera de mantener sus niveles de preocupación manejables**.

A este ritmo, es posible que aguantes a estos monos durante **mucho tiempo**, ¡posiblemente `10000` **rondas**!

Con estas nuevas reglas, aún puedes resolver el asunto de los monos después de 10000 rondas. Usando el mismo ejemplo anterior:

```
== After round 1 ==
Monkey 0 inspected items 2 times.
Monkey 1 inspected items 4 times.
Monkey 2 inspected items 3 times.
Monkey 3 inspected items 6 times.

== After round 20 ==
Monkey 0 inspected items 99 times.
Monkey 1 inspected items 97 times.
Monkey 2 inspected items 8 times.
Monkey 3 inspected items 103 times.

== After round 1000 ==
Monkey 0 inspected items 5204 times.
Monkey 1 inspected items 4792 times.
Monkey 2 inspected items 199 times.
Monkey 3 inspected items 5192 times.

== After round 2000 ==
Monkey 0 inspected items 10419 times.
Monkey 1 inspected items 9577 times.
Monkey 2 inspected items 392 times.
Monkey 3 inspected items 10391 times.

== After round 3000 ==
Monkey 0 inspected items 15638 times.
Monkey 1 inspected items 14358 times.
Monkey 2 inspected items 587 times.
Monkey 3 inspected items 15593 times.

== After round 4000 ==
Monkey 0 inspected items 20858 times.
Monkey 1 inspected items 19138 times.
Monkey 2 inspected items 780 times.
Monkey 3 inspected items 20797 times.

== After round 5000 ==
Monkey 0 inspected items 26075 times.
Monkey 1 inspected items 23921 times.
Monkey 2 inspected items 974 times.
Monkey 3 inspected items 26000 times.

== After round 6000 ==
Monkey 0 inspected items 31294 times.
Monkey 1 inspected items 28702 times.
Monkey 2 inspected items 1165 times.
Monkey 3 inspected items 31204 times.

== After round 7000 ==
Monkey 0 inspected items 36508 times.
Monkey 1 inspected items 33488 times.
Monkey 2 inspected items 1360 times.
Monkey 3 inspected items 36400 times.

== After round 8000 ==
Monkey 0 inspected items 41728 times.
Monkey 1 inspected items 38268 times.
Monkey 2 inspected items 1553 times.
Monkey 3 inspected items 41606 times.

== After round 9000 ==
Monkey 0 inspected items 46945 times.
Monkey 1 inspected items 43051 times.
Monkey 2 inspected items 1746 times.
Monkey 3 inspected items 46807 times.

== After round 10000 ==
Monkey 0 inspected items 52166 times.
Monkey 1 inspected items 47830 times.
Monkey 2 inspected items 1938 times.
Monkey 3 inspected items 52013 times.
```

Después de 10000 rondas, los dos monos más activos inspeccionaron los artículos 52166 y 52013 veces. Multiplicándolos juntos, el nivel de **negocios de monos** en esta situación ahora es **`2713310158`**.

**Los niveles de preocupación ya no se dividen por tres después de inspeccionar cada elemento; necesitará encontrar otra manera de mantener sus niveles de preocupación manejables. Comenzando nuevamente desde el estado inicial en la entrada de su rompecabezas, ¿cuál es el nivel de negocio de los monos después de 10000 rondas?**
