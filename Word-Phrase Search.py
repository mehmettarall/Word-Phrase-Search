import random


def tabloOlustur(boyut):
    tablo = list()
    for eleman in range(0,pow(boyut,2)):
        harf = chr(random.randrange(65,65+26))
        tablo.append(harf)



    matris(tablo, boyut)
    tahminSirasi(tablo, boyut)

def matris(matris,oyun_boyutu):
    sayac = 0
    sayac1 = 1
    while sayac <oyun_boyutu*oyun_boyutu:
        if sayac1 == oyun_boyutu:
            sayac1=0
            print(matris[sayac],end=" \t")
            print("\n")
        else:
            print(matris[sayac],end=" \t")
        sayac=sayac+1
        sayac1=sayac1+1
    print("\n")
def tahminSirasi(tablo,boyut):
    ara = input("Aranilacak kelimeyi giriniz: ")
    bul(tablo,ara,boyut)



def bul(tablo,ara,boyut):
    ku = uzunluk(ara)

    buldum = ""

    adet = 0
    for i in range(0,boyut-1):
        d = 0
        if(tablo[i] == ara[d]):
            sayac = 1
            buldum = tablo[i] + buldum
            d += 1
            indis = i
            if(indis+1  < boyut-1):
                indis = i+1
            while(tablo[indis] == ara[d]):
                if(ku == sayac):
                    adet += 1
                buldum += buldum + tablo[indis]
                if(d+1 < ku):
                    d +=1
                if(indis +1 < boyut-1):
                    indis +=1

    buldum2 = ""
    for i in range(0,boyut-1):
        d2 = 0
        indis = i
        if(tablo[i] == ara[d2]):

            sayac = 1
            buldum2 = tablo[i] + buldum2
            d2 += 1
            if(indis+boyut  < boyut-1):
                indis = i+boyut
            while(tablo[indis] == ara[d2]):

                if(ku == sayac):
                    adet += 1
                buldum2 += buldum2 + tablo[indis]
                if(d2+1 < ku):
                    d2 +=1
                if(indis+boyut  < boyut-1):
                    indis += boyut
    # adet = str(adet)
    print("Kelime:" + ara)
    print("Adet: " , adet)
def uzunluk(k):
    uzunluk = 0
    for i in k:
        uzunluk += 1
    return uzunluk





def menu ():
    while(True):
        print("[1]Basla")
        print("[2]Cikis")
        secim = int(input("islem: "))
        if(secim == 1):
            boyut = int(input("Oyun boyutu"))
            tabloOlustur(boyut)
        elif(secim == 2):
            return 0
        else:
            menu()


menu()
