import math

def kubus(sisi):
    volume = sisi**3
    lpermukaan = 6*sisi**2
    print(f'Volume kubus {sisi} **3 = {volume}')
    print(f'Luas Permukaan kubus 6x {sisi}**2 = {lpermukaan}')

def balok(p, l, t):
    volume = p*l*t
    lpermukaan = 2*((p*l) + (p*t) + (l*t))
    print(f'Volume balok {p} x {l} x {t} = {volume}')
    print(f'Luas Permukaan balok 2x(({p}x{l}) + ({p}x{t}) + ({l}x{t})) = {lpermukaan}')

def kerucut(s, r, t):
    volume = 1/3*r**2*t
    lpermukaan = 22/7*r*(s+r) 
    print(f'Volume kerucut 1/3 x {r}**2x {t} = {volume}')
    print(f'Luas permukaan kerucut 22/7 x {r}*({s}+{r}) = {lpermukaan}')

def tabung(jari2, tinggi):
    luastabung = 2 * 22/7 * (jari2 +tinggi)
    print(f'Luas tabung adalah {luastabung}')

def prismasegitiga(alas, keliling, tinggi):
    luasprima = (2 * alas) + (keliling * tinggi)
    print(f'Luas prisma adalah {luasprima}')


