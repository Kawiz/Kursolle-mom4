total = []
#medans sant så skriver den variabler sör sidorna och dess funktion
while True:
    s1 = int(input('Ange den första sidan: '))
    s2 = int(input('Ange den andra sidan: '))
    area = s1*s2
    info = [s1, s2, area]
    volym = ""
    print(f"Rektangelns sidor är {s1} och {s2}, vilket betyder att area är {area}")
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

    total.append(info)
    tal = []
    print("Höjd | Volym")
    print(" ")
    for i in range(1, volym+1):
        tal.append(str(i)+", "+str(i*area))
        print(f"{i} | {i*area}")
    info.insert(3, tal)
    
    fortsätt = input("Vill du fortsätta programmet? (Y/N)?")
    if fortsätt == "N" or fortsätt == "n":
        for t in total:
            if s1 == s2:
                print("Rektangeln har sidorna", t[0], " och ", t[1]," vilket betyder att area är ", t[2], ". Detta är en kvadrat använde gärna olika mått.")
            else:
                print("Rektangeln har sidorna", t[0], " och ", t[1]," vilket betyder att area är ", t[2])
        break
