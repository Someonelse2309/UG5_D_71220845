import math
loop = True
while loop == True:
    for i in range (0,1):
        jarak = (input("\nSilahkan masukan jarak awal (dalam meter)\n>> ")).lower()
        if jarak == "stop" or jarak == "berhenti":
            print ("\nTerima Kasih\n")
            loop = False
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
            print (f"Ketinggian di menit 5 adalah {round(tinggilima,2)} meter\nSelisih ketinggian di menit 5 dan 6 adalah {round(selisih,2)} meter")
     