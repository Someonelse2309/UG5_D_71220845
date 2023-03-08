def ganti_kata(kal,kat1,kat2):
    a = len(kal)
    for i in range (0,a):
        b = kal[i]
        if b == kat1:
            kal[i] = str(kat2)
        else:
            continue
    print (" ".join(kal).title())

kal = str(input("Silahkan masukan kalimat anda\n>> ")).lower().split(' ')
kat1 = str(input("Silahkan masukan kata yang anda mau ganti\n>> ")).lower()
kat2 =  str(input("Silahkan masukan kata pengganti yang mau dipakai\n>> ")).lower()
ganti_kata(kal,kat1,kat2)