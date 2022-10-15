import math


def v_szescian():
    a = float(input("podaj a: "))
    return a**3
    
def v_ostroslup_czworokatny():
    a = float(input("podaj a: "))
    h = float(input("podaj h: "))
    return (a**2) * (1/3) * h

def  v_graniastoslup_trojkatny():
    a = float(input("podaj a: "))
    h = float(input("podaj h: "))
    H = float(input("podaj H: "))
    return (1/3) * a * h * H
    
    
    
def v_walec(r:float, h:float):
    return math.pi * r **2 * h

def v_kuli(r:float):
    return (4/3) * math.pi * r**3

def v_stozek(r:float, h:float):
    return (1/3) * math.pi * r**2 * h
    
    
    
def v_piramidy(a:float, h:float):
    return a**2 * h / 3

def v_torus(r:float, R:float):
    return 2* math.pi ** 2 * r ** 2 * R

def v_kuli_odjac_v_torusa(r:float, R:float):
    return v_kuli(r) - v_torus(r, R)




def v_szescian_odjac_v_kuli(r:float):
    return v_szescian() - v_kuli(r)
    
def v_kuli_dodac_v_walca(r:float, h:float):
    print(v_kuli(r) + v_walec(r, h))
    
def v_szesciana_dodac_v_kuli(r:float, R:float):
    print(v_szescian() + v_kuli(r, R))
    
    
    
def v_szescian_dodac_v_stozek(r:float, h:float):
    print(v_szescian() + v_stozek(r, h))
    
def dwa_razy_v_szesciana_dodac_v_graniastoslupa_trojkatnego():
    print ((2 * v_szescian()) + v_graniastoslup_trojkatny())
    
def v_walec_dodac_v_stozka_odjac_v_kuli():
    r = float(input("podaj r: "))
    h = float(input("podaj h: "))
    print(v_walec(r, h) + v_stozek(r, h) - v_kuli(r))



def v_piramidy_odjac_v_szescianu():
    a = float(input("podaj a: "))
    h = float(input("podaj h: "))
    return v_piramidy(a, h) - v_szescian()
    
def  cztery_razy_v_stozka():
    r = float(input("podaj r: "))
    h = float(input("podaj h: "))
    return 4 * (v_stozek(r, h))
    
def v_walec_odjac_v_kuli(r:float, h:float):
    print(v_walec(r, h) - v_kuli(r))
    



    
    
    
    