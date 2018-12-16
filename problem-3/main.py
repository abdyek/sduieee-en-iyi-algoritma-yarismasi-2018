
def zitIsaretIceriyor(liste):
    pozIceriyor = False
    negIceriyor = False
    for sayi in liste:
        if abs(sayi) == sayi:
            pozIceriyor = True
        else:
            negIceriyor = True
    if negIceriyor and pozIceriyor:
        return True
    else:
        return False

def sifirIceriyor(liste):
    for sayi in liste:
        if sayi==0:
            return True
    return False

def pozNegAyir(liste):
    negListe = []
    pozListe = []
    for sayi in liste:
        if abs(sayi) == sayi:
            pozListe.append(sayi)
        else:
            negListe.append(sayi)
    return pozListe, negListe

def ikiliAltKumeVer(liste):
    altKumeleri = [] 
    for j in range(len(liste)-1):
        n = liste[j]
        for i in range(len(liste)-1-j):
            i += j
            altKumeleri.append([n, liste[i+1]])
    return altKumeleri

# ikili alt kümeden 3,4 ve daha fazlasını türeten fonksiyon
def uretici(liste, listeParcali):  # burada parçalı liste, ikili, üçlü, dörtlü ... alt küme
    yeni = []
    tmp = []
    for l in listeParcali:
        kalan = liste[liste.index(l[-1]) + 1:]
        for j in kalan:
            tmp.append(j)
            yeni.append(l + tmp)
            tmp.clear()
    return yeni

def altKumeVer(liste, sayi):
    ikiliAltKume = ikiliAltKumeVer(liste)
    for i in range(sayi-2):
        ikiliAltKume = uretici(liste, ikiliAltKume)
    return ikiliAltKume  # artık dönen şey ikili alt küme değil ondan ürettiğim diğer alt kümeler

def listeyiTopla(liste):
    toplam = 0
    for i in liste:
        toplam += i
    return toplam

# toplamları 0 yapan alt kümeleri listeyen fonksiyon
def goal(liste):
    if not zitIsaretIceriyor(liste) and not sifirIceriyor(liste):
        # boş küme olmak zorunda
        print("{}")
    elif sifirIceriyor(liste):
        print("{0}")
    pozListe, negListe = pozNegAyir(liste)

    pozListeAltKumeGrubu = []
    negListeAltKumeGrubu = []

    for i in range(len(pozListe)-1):
        pozListeAltKume = altKumeVer(pozListe, len(pozListe)-i)
        pozListeAltKumeGrubu.append(pozListeAltKume)

    for i in range(len(negListe)-1):
        negListeAltKume = altKumeVer(negListe, len(negListe)-i)
        negListeAltKumeGrubu.append(negListeAltKume)

    goalList = [];  # toplamları 0 olan alt kümeler

    for pozSayi in pozListe:  # sayıların kendilerinin zıt işaretlisinin olma durumu
        for negSayi in negListe:
            if pozSayi + negSayi == 0:
                goalList.append([pozSayi, negSayi])
    
    for i in pozListeAltKumeGrubu: # en küçük 2 li alt kümeleri toplama işi
        for j in negListeAltKumeGrubu:
            for k in i:
                for l in j:
                    if listeyiTopla(k) + listeyiTopla(l) == 0:
                        goalList.append(k + l)

    # bir sayı ile bu sayıya zıt işaretli bir alt grubun toplamlarının 0 olma durumlarını yakalayabilmek için, örn [-7, -5] , 12 gibi
    for i in pozListe:
        for j in negListeAltKumeGrubu:
            for l in j:
                if listeyiTopla(l) + i == 0:
                    goalList.append(l + [i])
    for i in negListe:
        for j in pozListeAltKumeGrubu:
            for l in j:
                if listeyiTopla(l) + i == 0:
                    goalList.append(l + [i])
            
    print("toplamları 0 olan alt kümeler")
    for li in goalList:
        print(li)

# örnek bir sayı listesi
sayiListesi = [-5, 0, -7, -10, 11, +9, 10, 12, 5] 
goal(sayiListesi)



