import math

def l_persegi(sisi):
    luas = sisi*sisi
    keliling = sisi*sisi*sisi*sisi
    print(f'Luas Persegi {sisi} * {sisi} = {luas}')
    print(f'Keliling Persegi adalah {keliling}')

def persegipanjang(p, l):
    luas = p * l 
    keliling = 2*p + 2*l 
    print(f'Luas Persegi Panjang {p} * {l}')
    print(f'Keliling Persegi Panjang {keliling}')

def segitiga(alas, tinggi):
    luas = 1/2 * alas * tinggi
    print(f'luas segitiga 1/2 * {alas} * {tinggi} = {luas}')

def l_belahketupat(d1,d2):
    luasbk = 1/2 * d1 * d2
    print(f'luas belah ketupat {1/2} * {d1} * {d2} = {luasbk}')

def l_layanglayang(d1,d2):
    luasll = 1/2 * d1 * d2
    print(f'luas layang layang {1/2} *{d1} *{d2} = {luasll}')

    

