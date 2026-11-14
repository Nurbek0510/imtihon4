xizmatlar = {
    "diagnostika" : 50000,
    "tozalash" : 80000,
    "sozlash": 40000,
    "almashtirish" : 120000
}

def hisobla(*args, **kwargs):
    jami = 0

    for xizmat in args:
        if xizmat in xizmatlar:
            jami += xizmatlar[xizmat]
        else:
            print(f"Ogohlantirish: {xizmat} xizmati topilmadi.")

    mijoz = kwargs["mijoz"]
    chegirma_foizi = kwargs["chegirma"]

    chegirma_sumasi = jami * chegirma_foizi / 100
    tolov = jami - chegirma_sumasi

    print("Mijoz: ", mijoz)
    print("Xizmatlar jami: ", int(jami), "som")
    print("Chegirma: ", int(chegirma_sumasi), "som")
    print("Tolov: ", int(tolov), "som")

hisobla(
    "diagnostika",
    "tozalash",
    "sozlash",
    mijoz = "Nodira", 
    chegirma = 10
)