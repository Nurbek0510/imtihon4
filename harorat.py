haroratlar = [-20, -19, -17, -16, -18, -21, -15, -14, -20]

son = 0
jami_harorat = 0

for harorat in haroratlar:
    jami_harorat += harorat

    if harorat > -18:
        son += 1

ortacha = jami_harorat / len(haroratlar)

print("Xavfli olchovlar:", son, "ta")
print(f"Harorat: {ortacha:.2f}°C")