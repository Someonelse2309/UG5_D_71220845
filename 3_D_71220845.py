import math
loop = True
while loop == True:
    jarak = (input("Silahkan masukan jarak awal (dalam meter)\n>> ")).lower()
    if jarak == "done" or jarak == "berhenti":
        print ("\nTerima Kasih\n")
        break
    else:
        jarak = int(jarak)
        sudutlima = float(input("Silahkan masukan sudut elevasi di menit ke-5\n>> "))
        sudutenam = float(input("Silahkan masukan sudut elevasi di menit ke-6\n>> "))
        tansudutlima = math.tan(math.radians(sudutlima))
        tansudutenam = math.tan(math.radians(sudutenam))
        tinggilima = jarak * tansudutlima
        jarakakhir = jarak * (tansudutenam - tansudutlima)
        selisih = jarakakhir * tansudutenam
        print (f"Ketinggian di menit 5 adalah {tinggilima}\nSelisih ketinggian di menit 5 dan 6 adalah {selisih}")
     