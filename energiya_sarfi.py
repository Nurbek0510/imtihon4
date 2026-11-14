import matplotlib.pyplot as grafik

kunlar = ["Du", "Se", "Cho", "Pa", "Ju", "Sha", "Ya"]
sarf = [42, 38, 51, 47, 62, 70, 45]

ortacha = sum(sarf) / len(sarf)

yuqori_kunlar = []
yuqori_sarf = []

for i in range(len(sarf)):
    if sarf[i] > ortacha:
        yuqori_kunlar.append(kunlar[i])
        yuqori_sarf.append(sarf[i])

print(f"O‘rtacha sarf: {ortacha:.2f} kWh")
print("O‘rtachadan yuqori kunlar:", ", ".join(yuqori_kunlar))

grafik.plot(kunlar, sarf, marker="o", label="Kunlik sarf")
grafik.axhline(ortacha, color="red", linestyle="--", label="O‘rtacha sarf")
grafik.scatter(yuqori_kunlar, yuqori_sarf, color="orange",
               marker="*", s=150, label="O‘rtachadan yuqori")

grafik.title("7 kunlik elektr sarfi")
grafik.xlabel("Hafta kunlari")
grafik.ylabel("Elektr sarfi (kWh)")
grafik.legend()
grafik.grid(True)

grafik.savefig("energiya_tahlili.png")
grafik.show()