log = "hall-a, HALL-B, hall-a, hall-c, HALL-B, hall-a"

bolimlar =[]

for i in log.split(","):
    i = i.strip()

    if i != "":
        bolimlar.append(i.upper())

noyob_bolimlar = set(bolimlar)

print("Tozalangan: ", ", ".join(bolimlar))
print("Noyob bolimlar: ", len(noyob_bolimlar))