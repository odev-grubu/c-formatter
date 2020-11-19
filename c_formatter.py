kaynak = open('source.c', 'r')
hedef = open('target.c', 'w')
bosluk = '  '
bosluk_sayisi = 0

for satir in kaynak:
    if '{' in satir:
        satir = bosluk*bosluk_sayisi+satir
        bosluk_sayisi += 1

    elif '}' in satir:
        bosluk_sayisi -= 1
        satir = bosluk*bosluk_sayisi+satir

    else:
        satir = bosluk*bosluk_sayisi+satir

    hedef.write(satir)

kaynak.close()
hedef.close()
