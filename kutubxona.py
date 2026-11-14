import json
with open("inventar.json", "r", encoding="utf-8") as f:

    kitoblar = json.load(f)

mavjud_kitoblar = []

for kitob in kitoblar:
    mavjud = kitob["jami"] - kitob["band"]

    mavjud_kitoblar.append({
        "nom": kitob["nom"],
        "mavjud": mavjud
    })

    print(f'{kitob["nom"]}: {mavjud} ta mavjud')

with open("mavjud_kitoblar.json", "w", encoding="utf-8") as f:
    json.dump(mavjud_kitoblar, f, ensure_ascii=False, indent=4)

print(f"{len(mavjud_kitoblar)} ta yozuv saqlandi.")