# -*- coding: utf-8 -*-

satir = int(raw_input("satır sayısını giriniz:"))
sutun = int(raw_input("sütün sayısını giriniz:"))
i = 0
j = 0
matris = []
matris_satir = []

for i in range(0,satir):
    matris.append(1)
    for j in range(0,sutun):
        matris_satir.append(1)
        matris_satir[j] = int(raw_input("%s. satır ve %s. sütun değerini giriniz :"%((i+1),(j+1))))
        matris[i] = matris_satir
    matris_satir = []    

for i in range(0,satir):
    print matris[i]
    
    
        
