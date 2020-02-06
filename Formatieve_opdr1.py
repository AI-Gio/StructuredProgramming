#Opdracht 1
from textwrap import dedent


def pyramide():
    grootte = int(input("Hoe groot?: "))
    for i in range(0, grootte):
        print((i+1) * "*")
    for i in range(1, grootte):
        print((grootte - i) * "*")
pyramide()
def pyramide2():
    grootte = int(input("Hoe groot?: "))
    i = 0
    while i < grootte:
        i += 1
        print(i* "*")
    while i > 0:
        i -= 1
        print(i* "*")

def pyramide_rev():
    grootte = int(input("Hoe groot?: "))
    i = grootte
    while i > 0:
        print(i*"*")
        i -= 1
    i = 1
    while i < grootte:
        print((i+1) * "*")
        i += 1


#Opdracht 2
def ZinCheck():
    z1 = input("Geef een string: ")
    z2 = input("Geef een string: ")
    index = 0
    if len(z1) >= len(z2):
        for i in z1:
            if i != z2[index]:
                print("Het eerste verschil zit op index: " + str(index))
                break
            else:
                index += 1
    elif len(z1) < len(z2):
        for i in z2:
            if i != z1[index]:
                print("Het eerste verschil zit op index: " + str(index))
                break
            else:
                index += 1



#opdracht 3
def count(lijst, X):
    tel = 0
    for i in lijst:
        if i == X:
            tel += 1
    return tel

def BigDiff(lst):
    grootste = 0
    for i in lst:
        try:
            if (lst[lst.index(i) + 1] - i) > grootste:
                grootste = lst[lst.index(i) + 1] - i
        except IndexError:
            break
    print(grootste)

def Zero_One(lijst):
    for i in lijst:
        if i != 0 and i != 1:
            return "Sorry there has to be an input of 1 or 0"
    ManyOne = count(lijst, 1)
    ManyZero = count(lijst, 0)
    if ManyZero >= 12:
        return "Sorry there are too many zero's in this list"
    elif ManyZero > ManyOne:
        return "Sorry there are more zero's then one's in this list"
    else:
        return "This list is verified"
#Opdracht 4
def PalSelf():
    woord = input("Check of het woord een palindroom is: ")
    index = 0
    for i in woord: #l
        for j in range(1+index, (len(woord) + 1)):
            if i == woord[-(j)]:
                break
            else:
                return "Het woord is geen palindroom"
        index += 1
    if index == len(woord):
        return "Het woord is een palindroom"
"""
^niet opgezocht op internet^
check van voor naar achter en van achter naar voren of de letter gelijk zijn en als ze tot het einde van de lengte van het woord gelijk zijn dan is het een palindroom
doe dit met index op tellen
"""
def PalLib():
    woord = input("Check of het woord een palindroom is: ")
    woordRev = woord[::1]
    if woord == woordRev:
        return "Het woord is een palindroom"
    else:
        return "Het woord is geen palindroom"
"""
^opgezocht op het internet^
https://www.w3schools.com/python/python_howto_reverse_string.asp
"""


#Opdracht 5
def SortLst(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst
#Opdracht 6
def Gem(lst):
    count = 0
    for i in lst:
        count += 1
    i = sum(lst) / count
    return i
def GemTwo(lst):  #Deze functie is nog niet helemaal werkend
    count1 = 0
    count2 = 0
    TopLst = []
    for i in lst:
        count1 += 1
        count2 = 0
        for j in lst:
            count2 += 1
        TopLst.append(sum(i) / count2)
    return sum(TopLst) / count1
#print(GemTwo([[2,2,2],[3,3,3],[4,4,4],[5,5,5]]))
#Opdracht 7
def Gokmachine():
    import random
    getal = random.randint(0,10)
    while True:
        gok = int(input("Gok het getal: "))
        if getal == gok:
            return "Concgrats u guessed right!"
        else:
            print("Ah such a shame, try again!")

#Opdracht 8
def Compression():
    f = open("NotCompressed", "rt")
    NotComp = f.readlines()
    for i in NotComp:
        if "\n" in NotComp:
            NotComp.remove("\n")
    for i in NotComp:
        Comp = i.strip(" \n")
        print(Comp)

#Opdracht 9
def Shift():
    ch = "11110000" #input("Put in 8bit binary number: ")
    n = 3 #int(input("Put in shift left(n)/shift right(-n): "))
    #if n > 0:
        #for i in range(0,n):






















