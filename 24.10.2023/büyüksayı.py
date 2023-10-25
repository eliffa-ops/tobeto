
sayi1=float(input("Birinci sayiyi giriniz:"))
sayi2=float(input("İkinci sayiyi giriniz:"))
sayi3=float(input("Üçüncü sayiyi giriniz:"))

if (sayi1>=sayi2) and (sayi1>=sayi3):
    enBuyuk=sayi1
elif (sayi2>=sayi1) and (sayi2>=sayi3):
    enBuyuk=sayi2
else:
    enBuyuk=sayi3
    print("En buyuk sayi:",enBuyuk)
    