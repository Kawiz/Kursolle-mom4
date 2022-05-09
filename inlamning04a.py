#Variabler sör sidorna och dess funktion
s1 = int(input("Ange rektangelns ena sida:"))
s2 = int(input("Ange rektangelns andra sida:"))
#Uträkningar av sidorna
area = s1*s2
#Om sidorna inte stämmer och inte bildar en rektangel och istället en kvadrat skrivs detta
if s1==s2:
    print(" ")
    print(f"Felaktigt input. Ena sidan är {s1} och andra är {s2}. Detta är en kvadrat eftersom bägge sidorna är lika långa. Skriv gärna olika värden.")
#Annars vanliga utskriften som är menad.
else:
    print(" ")
    print(f"Rektangeln har sidorna {s1} och {s2} vilket gör att arean är {area}")
print(" ")
print("Höjden | Volymen")
print(" ")
for i in range(1,11):
    print(i, "|",i*area)
print(" ")