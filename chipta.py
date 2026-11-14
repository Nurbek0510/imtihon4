def chipta_tekshir(kod):
    kod = kod.strip()

    if len(kod) != 14:
        return False

    if kod[0:3] != "UZ-" or kod[7] != "-":
        return False

    for belgi in kod[3:7]:
       if belgi < "0" or belgi > "9":
            return False

    for belgi in kod[8:10]:
        if belgi < "A" or belgi > "Z":
            return False

    for belgi in kod[10:14]:
        if belgi < "0" or belgi > "9":
            return False

    return True

kodlar = [" UZ-2026-AB1234 ", " UZ-26-AB1234 ", " UZ-2026-aB1234"]

for kod in kodlar:
    tozalangan = kod.strip()

    if chipta_tekshir(tozalangan):
        yil = tozalangan[3:7]
        seriya = tozalangan[8:14]
        print(f"{tozalangan}: yaroqli | yil: {yil} | seriya: {seriya}")
    else:
        print(f"{tozalangan}: yaroqsiz")