from engine import Rulet_Table
from random import randint
from engine import paros_paratlan


def Rulet_test() -> bool:
    val = Rulet_Table()
    kimenet = False
    if type(val) == int and 0<=val<=36:
        kimenet = True
    else:
        kimenet = False
    return kimenet
def paros_paratlan_test() -> bool:
    val = randint(0, 36)
    kiment = []
    kiment.append(val)
    if val % 2 == 0 and paros_paratlan(val):
        kiment.append(paros_paratlan(val))
    else:
        kiment.append=(paros_paratlan(val))
    return kiment


if __name__ == "__main__":
    Tests = ["A rulet_Table"]
    results = [ "✅" if Rulet_Table else "💔"]

for i in range(len(Tests)):
    print(Tests[i], results[i])

print(paros_paratlan_test())