  
def hitung_mobil():
    ulg = True
    jumlahsol = 0
    jumlahjog = 0
    jumlahsur = 0
    jumlahmag = 0  
    while ulg == True:
        print ()
        mobil = str(input("Silahkan masukan asal mobil (ketik done untuk mengakhiri)\n>> ")).lower()
        if mobil == "solo":
            jumlahsol += 1
            ulg = True
        elif mobil == "jogja":
            jumlahjog += 1
            ulg = True
        elif mobil == "magelang":
            jumlahmag += 1
            ulg = True
        elif mobil == "surabaya":
            jumlahsur += 1
            ulg = True
        elif mobil == "done":
            ulg = False
            print (f"\nJumlah Solo \t\t: {jumlahsol}\nJumlah Surabaya \t: {jumlahsur}\nJumlah Jogja \t\t: {jumlahjog}\nJumlah Magelang \t: {jumlahmag}")
        else:
            print ("Maaf Input Anda Salah\n")
            ulg = True

hitung_mobil()