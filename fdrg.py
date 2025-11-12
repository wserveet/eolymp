pin=9786
tarife=0
p=0
durum=True
g=3
s=0
say=0
limit=0
siyahi={}
odenis=0
endirim=0
yuklenenpul=0
istifadeci=0
while durum:

    n=int(input())
    if n!=pin:
        g-=1
        if g==0:
            ("program dayandirilir")
            durum=False
    elif n==pin:
        print("lutfen gozleyin")
    menu=int(input("1-balansi goster 2-balans artir 3-gedis et 4-son emeliyyatlara bax 5-gunluk statistika 6-parametrler 0-cixis"))
    if menu==2:
        siyahi.append("balansartir")
        artirma=int(input("mebleg daxil edin"))
        if artirma<0 or artirma==0:
            print("mebleg duzgun daxil edin")
        elif artirma>0:
            if s+artirma>100+limit:
                print("gunluk limiti kecen emeliyyatlar icra olunabilmir")
            elif s+artirma<=100+limit:
                s=s+artirma
                yuklenenpul+=artirma
        breakpoint()
    if menu==3:
        if tarife==0:
            siyahi.append("kecid")
            if s>=0.4:
                if say>1 and say<5:
                    s=s-0.36
                    endirim+=0.04
                    odenis=odenis-0.36
                elif say>=5:
                    s=s-0.3
                    endirim+=0.1
                    odenis=odenis-0.3
                else:
                    s=s-0.4
                    odenis=odenis-0.4
                say=+1
                breakpoint()
        if tarife==1:
            siyahi.append("kecid")
            if s>=0.2:
                if say>1 and say<5:
                    s=s-0.18
                    endirim+=0.02
                    odenis=odenis-0.18
                elif say>=5:
                    s=s-0.15
                    endirim+=0.05
                    odenis=odenis-0.15
                else:
                    s=s-0.2
                    odenis=odenis-0.2
                say=+1
                breakpoint()
        if tarife==2:
            siyahi.append("kecid")
            if s>=0.15:
                if say>1 and say<5:
                    s=s-0.14
                    endirim+=1
                    odenis=odenis-0.14
                elif say>=5:
                    s=s-0.11
                    endirim+=0.4
                    odenis=odenis-0.11
                else:
                    s=s-0.15
                    odenis=odenis-0.15
                say=+1
                breakpoint()
        elif s>=0.3 and s<=0.39:
            teklif=int(input("tecili kecid 0.3+0.1(borc) 1-beli 2-xeyr"))
            if teklif==1:
                s=s-0.4
                say+=1
                breakpoint()
            elif teklif==2:
                breakpoint()
        elif s<0.3:
            print("kartinizda yeterli balans yoxdur")
            breakpoint()

    if menu==5:
        siyahi.append("guluk statistika")
        print("gedis sayi=",say," umumi odenis=",odenis," endirimler cemi=",endirim," artirilan mebleg=",yuklenenpul)
        breakpoint()
    if menu==6:
        siyahi.append("parametrler")
        secenek=int(input("limit artirma-1 tarife secme-2"))
        if secenek==1:
            limit=int(input("limiti artirin"))
        elif secenek==2:
            j=int(input("telebe ucun-1 pensiyaci ucun-2"))
            tarife+=j
        else:
            print("duzgun daxil edin")
            breakpoint()
    if menu==6:
        print("cixis edilir")
        breakpoint()
    if menu==4:
        siyahi.append("tarixce")
        r=int(input())
        r=-r
        print(siyahi[0:r-1])
        breakpoint()