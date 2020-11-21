class lifo():
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, veri):
        self.stack.append(veri)

    def pop(self):
        return self.stack.pop()


ana_lifomuz = lifo()
kaynak = open('source.c', 'r')
hedef = open('target.c', 'w')
bosluk = '  '
bosluk_sayisi = 0

for satir in kaynak:
    if '{' in satir:
        satir = bosluk*bosluk_sayisi+satir
        bosluk_sayisi += 1
        ana_lifomuz.push(satir)

    elif '}' in satir:
        bosluk_sayisi -= 1
        satir = bosluk*bosluk_sayisi+satir
        ana_lifomuz.push(satir)

    else:
        satir = bosluk*bosluk_sayisi+satir
        ana_lifomuz.push(satir)


buffer_lifomuz = lifo()


def cevir(lifo):
    while not ana_lifomuz.isEmpty():
        buffer_lifomuz.push(ana_lifomuz.pop())
    return buffer_lifomuz


dondurulmus_lifomuz = cevir(ana_lifomuz)

while not dondurulmus_lifomuz.isEmpty():
    hedef.write(dondurulmus_lifomuz.pop())
