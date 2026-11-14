import csv

jami_yolovchilar = {}

with open("qatnov.csv", "r", encoding="utf-8", newline="") as fayl:
    oqish = csv.DictReader(fayl)

    for qator in oqish:
        yonalish = qator["yonalish"]
        yolovchilar = int(qator["yolovchi"])

        if yonalish not in jami_yolovchilar:
            jami_yolovchilar[yonalish] = 0

        jami_yolovchilar[yonalish] += yolovchilar


for yonalish, jami in jami_yolovchilar.items():
    print(f"{yonalish}-yo‘nalish: {jami} nafar")


with open("yonalish_jami.csv", "w", encoding="utf-8", newline="") as fayl:
    ustunlar = ["yonalish", "jami_yolovchi"]
    yozish = csv.DictWriter(fayl, fieldnames=ustunlar)

    yozish.writeheader()

    for yonalish, jami in jami_yolovchilar.items():
        yozish.writerow({
            "yonalish": yonalish,
            "jami_yolovchi": jami
        })