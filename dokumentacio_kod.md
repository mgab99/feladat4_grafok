A kód minden alkalmazott esetén kiszámolja, hogy mennyi alkalmazottja van.

Az első input az, hogy mennyi alkalmazott van, a második, pedig, hogy az alkalmazottaknak mennyi főnökük van.

A megvalósírás során inicializálok egy listát, amiben a mindenkire vonatkozó beosztottak el vannak tárolva.

Ezt követően gráfos megközelítéssel megszámolom az alkalmazottakat.

Ezzel a megoldással az elejére 0 érték kerül, így egy list comprehensionben a 0. indexen lévő 0-át kitörlöm úgymond, legalábbis nem adom vissza.
