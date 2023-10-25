metin=input("Lütfen metni giriniz:")
ters=metin[::-1]

print("Girilen metnin tersi=&s' &(ters)")
if ters ==metin:
    print("Girilen metin palindromdur")
else:
    print("Girilen metin palindrom değildir")
    