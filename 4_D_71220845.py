senin = [" ", "Ngasdos PrakAlPro","MuayThai"," "," "," "]
selasa = ["Kelas AI", "Kelas RPLBO", "Kelas ProgWeb", "Ngerjain Tugas ProgWeb","Bikin Soal UG AlPro","Seminar Cyber Security"]
rabu = ["Kelas PrakRPLBO", "Kelas PrakProgWeb","Kelas Pendidikan Pancasila", "Kelas EtProf","Ngasdos PrakAlPro","Ngerjain Tugas Keamanan Komputer"]
kamis = ["Kelas Keamanan Komputer"," ","Ngasdos PrakJarKom"," "," "," "]
jumat = ["Kelas PrakRPLBO"," ","Mengkoreksi UG PrakAlPro","Mengkoreksi Tugas PrakJarKom","MuayThai"," "]
sabtu = [" ","Photoshoot"," ","MuayThai"," "," "," "]
loop = True
while loop == True:
    a = str(input("Silahkan Masukan Hari Yang Dikehendaki\n>> "))
    b = 1
    if a == "senin":
        print (f"\n\nKelas Pada Hari {a.title()}\n")
        for i in range(0,5):
            if senin[i]==" ":
                continue
            else:
                print (f"Sesi ke-{i+1}\t: {senin[i]}")
        break
    elif a == "selasa":
        print (f"\n\nKelas Pada Hari {a.title()}\n")
        for i in range(0,5):
            if selasa[i]==" ":
                continue
            else:
                print (f"Sesi ke-{i+1}\t: {selasa[i]}")
        break
    elif a == "rabu":
        print (f"\n\nKelas Pada Hari {a.title()}\n")
        for i in range(0,5):
            if rabu[i]==" ":
                continue
            else:
                print (f"Sesi ke-{i+1}\t: {rabu[i]}")
        break
    elif a == "kamis":
        print (f"\n\nKelas Pada Hari {a.title()}\n")
        for i in range(0,5):
            if kamis[i]==" ":
                continue
            else:
                print (f"Sesi ke-{i+1}\t: {kamis[i]}")
        break
    elif a == "jumat":
        print (f"\n\nKelas Pada Hari {a.title()}\n")
        for i in range(0,5):
            if jumat[i]==" ":
                continue
            else:
                print (f"Sesi ke-{i+1}\t: {jumat[i]}")
        break
    elif a == "sabtu":
        print (f"\n\nKelas Pada Hari {a.title()}\n")
        for i in range(0,5):
            if sabtu[i]==" ":
                continue
            else:
                print (f"Sesi ke-{i+1}\t: {sabtu[i]}")
        break
    else:
        print ("\nMaaf Input Anda Salah\n")
        continue