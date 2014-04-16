#-*- coding:utf-8 -*-
#karatsuba

#büyük basamaklı sayıların çarpımı(max. 40 basamak)

def karatsuba(a,b):
    boyut1 = len(str(a))
    boyut2 = len(str(b))
    if boyut1 <= boyut2:
        a2 = a % (10**(boyut1-1))
        a1 = (a - a2) / (10**(boyut1-1))
        b2 = b % (10**(boyut1-1))
        b1 = (b - b2) / (10**(boyut1-1))
        yeni_boyut = boyut1-1
    else:
        b2 = b % (10**(boyut2-1))
        b1 = (b - b2) / (10**(boyut2-1))
        a2 = a % (10**(boyut2-1))
        a1 = (a - a2) / (10**(boyut2-1))
        yeni_boyut = boyut2-1

    if a2 > 1 and b2 > 1:
        Z2 = a1 * b1
        Z0 = karatsuba(a2,b2)
        Z1 = ((a1+a2)*(b1+b2)) - Z2 - Z0
        sonuc = (Z2 * (10**(yeni_boyut*2))) + (Z1*(10**yeni_boyut)) + Z0
        return sonuc
    else:
        return a*b
        

sayi1 = int(raw_input("1. sayıyı giriniz:"))
sayi2 = int(raw_input("2. sayıyı giriniz:"))

print 
print "1. sayının basamak sayısı = " , len(str(sayi1))
print "2. sayının basamak sayısı = " , len(str(sayi2))
print "Sonucun basamak sayısı" , len(str(karatsuba(sayi1,sayi2)))
print "Sonuç = " , karatsuba(sayi1,sayi2)


 
