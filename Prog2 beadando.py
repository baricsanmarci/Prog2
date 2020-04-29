#EX26

from math import gcd

part = input("Írja be a megnézett időtartalmat! (hh:mm:ss):")
total = input("Írja be a teljes időtartalmat! (hh:mm:ss):")
par=part.split(":")
tota=total.split(":")

if part==total:
    print("Megnézted az egész filmet")
elif part== "00:00:00":
    print("Még nem kezdted el a filmet")
elif part>total:
    print("A megadott rész hosszabb mint maga a film, módosítsd a bevitt adatokat")
else:
    part_h=int(par[0])
    total_h=int(tota[0])

    part_m=int(par[1])
    total_m=int(tota[1])

    part_s=int(par[2])
    total_s=int(tota[2])

#most átalakítok mindent másodpercbe
    parth_s=(part_h*60)*60
    totalh_s=(total_h*60)*60

    partm_s=(part_m*60)
    totalm_s=(total_m*60)

    osszpart=parth_s+partm_s+part_s
    ossztotal=totalh_s+totalm_s+total_s

    g=gcd(osszpart,ossztotal)

    megtekintes=[]
    megtekintes.append(int(osszpart/g))
    megtekintes.append(int(ossztotal/g))
    a=megtekintes[0]
    b=megtekintes[1]

    print(megtekintes, "A teljes videó ", int(a), "/", int(b), "részét sikerült már megnézni.", sep='')

#EX2
x=1
teszt=int(input("Adja meg a kívánt tesztesetek számát: "))
if teszt<1 or teszt>5000:
    print("A tesztesetek számának 1 és 5000 közé kell esnie")
else:
    print("A megadott tesztesetek száma megfelel a kritériumnak.")
    while x!=teszt+1:
        n=int(input("Adja meg a tábla sorainak számát(1-50-ig): "))
        m=int(input("Adja meg a tábla oszlopainak számát(1-50-ig): "))
        if (n<1 or m<1 or n>50 or m>50):
            print("A megadott sorok vagy oszlopok száma nem felel meg a megadott kritériumoknak: No")
        else:
            if (n>=1 and m>=1 and n<=50 and m<=50) and (n%2==0 or m%2==0):
                print(f"A {x}. esetben: Yes")
            else:
                print(f"A {x}. esetben: No")
        x=x+1


