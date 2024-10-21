"""1. Páros és páratlan számok szétválogatása (1-től 20-ig)
Feladat: Írd ki külön a páros és a páratlan számokat 1-től 20-ig.
Páros számok: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
Páratlan számok: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19"""



"""
2. Számok faktoriálisa
Feladat: Számold ki egy adott szám faktoriálisát!

Ha az adott szám 5, a faktoriálisa: 5! = 5 × 4 × 3 × 2 × 1 = 120
"""

def masodik():
    szam = 6
    faktorialis = 1

    for i in range(1, szam + 1):
        faktorialis *= i
    print(faktorialis)


"""
3. Számok összegének és átlagának kiszámolása
Feladat: Számold ki az 1-től egy adott számig lévő számok összegét és átlagát!

Ha az adott szám 10:
Összeg: 1 + 2 + 3 + ... + 10 = 55
Átlag: 55 ÷ 10 = 5.5
"""

def harmadik():
    n_szam = 10
    osszeg = 0
    for i in range(1, n_szam + 1):
        osszeg = osszeg + 1

    atlag = osszeg / n_szam
    print(f"{n_szam} szám átlaga:{atlag}")

"""
4. Egymásba ágyazott for ciklusok: szorzótábla megjelenítése
Feladat: Készítsd el az 1-től 10-ig tartó szorzótáblát!

Szorzótábla 1-től 10-ig:
1 × 1 = 1, 1 × 2 = 2, ..., 1 × 10 = 10
2 × 1 = 2, 2 × 2 = 4, ..., 2 × 10 = 20
...
10 × 1 = 10, 10 × 2 = 20, ..., 10 × 10 = 100
"""

def negyedik():
    szam1 = 1
    for i in range(1, 11):
        print(f"{szam1} x {i} = {szam1 * i}")

"""
5. Fibonacci-sorozat generálása
Feladat: Írd ki a Fibonacci-sorozat első 10 számát!

Fibonacci-sorozat első 10 száma: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
"""

# masodik()
# harmadik()
negyedik()
