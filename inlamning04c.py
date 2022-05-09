#medans sant så skriver den variabler sör sidorna och dess funktion
while True:
    s1 = int(input('Ange den första sidan: '))
    s2 = int(input('Ange den andra sidan: '))
    area = s1*s2
    info = [s1, s2, area]
    volym = ""
    print(f"Rektangelns sidor är {s1} och {s2}, vilket betyder att area är {area}")
#Om sidorna inte stämmer och inte bildar en rektangel och istället en kvadrat skrivs detta
    if s1 == s2:
        print("Detta är en kvadrat ange gärna olika mått.")
        info.append("kvadrat")
    while type(volym) != int:
        try:
            volym = int(
                input("Ange höjden för rektangeln: "))
            if volym <= 0:
                volym = 1
            if volym >= 10:
                volym = 10
        except Exception as e:
            print(" ")
#-||-
    tal = []
    print("Höjd | Volym")
    print(" ")
    for i in range(1, volym+1):
        tal.append(str(i)+", "+str(i*area))
        print(f"{i} | {i*area}")
    info.insert(3, tal)

    fortsätt = input("Vill du fortsätta programmet? (Y/N)?")
    if fortsätt == "N" or fortsätt == "n":

        break
