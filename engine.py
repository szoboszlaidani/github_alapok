import random

def Rulet_Table() -> int:
    ertek = random.randint(0, 36)
    return ertek

def paros_paratlan(szam:int) -> bool:
    '''A paros a True, a paratlan a False'''
    kimenet = False
    if szam != 0:
        if szam % 2 == 0:
            kimenet = True
        else:
            kimenet = False
    else:
        return None
    return kimenet

