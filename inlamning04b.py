#medans sant så skriver den variabler sör sidorna och dess funktion
while True:
    s1 = int(input("Ange den första sidan: "))
    s2 = int(input("Ange den andra sidan: "))
    area = s1*s2
    info = [s1, s2, area]
    print(f"Rektangelns sidor är {s1} och {s2}, vilket betyder att area är {area}")
#Om sidorna inte stämmer och inte bildar en rektangel och istället en kvadrat skrivs detta
    if s1 == s2:
        print("Båda sidorna är lika vilket innebär att det är en kvadrat. Använd gärna olika mått.")
        info.append("kvadrat")
    print("Höjd | Volym")
    print(" ")
    for i in range(1,11):
        print(f"{i} | {i*area}")
#Variabel för att loopa koden igen annars so break vilket ger den ett stopp
    fortsätt = input("Vill du göra en ny uträkning? (Y/N)? ")

    if fortsätt == "N" or fortsätt == "n":
        break
