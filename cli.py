from engine import *

'''user declare'''
user = ["Bela", 5000]

def tate_engine(user:list, tet:int) -> list:
    debit = user[1]
    if tet >=0:
        if debit < tet:
            kimenet = ["Nincs eleg penzed!", 404]
        else:
            user[1] = user[1]-tet
            kimenet = ["Tet megrakva", 200, tet]
    else:   
        kimenet = ["nem rakhatsz meg nagyobb tetet", 404]
        return kimenet

'''Menu'''
def menu()-> int:
    print('''
        Hogy szeretnel jatszani?:
          Konkret szam emegadasa [1]
          Exit [0]
    ''')
    x = int(input(">"))
    if x != 0:
        return x
    else:
        print("Koszonjuk a jatekot")
        exit()

'''Tabel mukodese'''
def table_management(user:list, ertek:int):
    porgetes = Rulet_Table()

    '''Tet konkret szam'''
    if ertek == 1:
        print(porgetes)
        megrakott = int(input("Megrakott ertek ( 0-36 ):"))
        tet = int(input("Megrakando tet:"))
        middle = tate_engine(user=user, tet=tet)
        if 0 <= megrakott <= 36:
            if porgetes == megrakott:
                if middle[1] == 404:
                    print(middle[0])
                else:
                    print(f"{user[0]}: a te nyeremenyed {tet*32}")
                    user[1] == user[1]+(tet*32)

            else:
                if middle[1] == 404:
                    print(middle[0])
                else:
                    print("Ez nem jott ossze ")
                        
table_management(user=user, ertek=menu())