# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 22:31:13 2024

@author: eamir
"""

print("Bankamıza Hoş geldiniz.")
bakiye=1000

while True:
    i=input("Yapmak istediğiniz işlemi seçiniz: ").lower()
    
    if i=="çıkış":
        print("çıkış yapılıyor...")
        break
    elif i=="para çekme":
        cekme=int(input("çekmek istediğiniz tutarı giriniz: "))
        if cekme>bakiye:
            print("bakiyeniz yetersiz")
        elif cekme<0:
            print("negatif tutar girilememektedir.")
        else:
            bakiye-=cekme
            print(f"Yeni bakiye: {bakiye} TL")
    elif i=="para yatırma":
        yatirma=int(input("yatırmak istediğiniz tutarı giriniz: "))
        if yatirma<0:
            print("negatif tutarlı işlem yapılamamaktadır")
        else:
            bakiye+=yatirma
            print(f"Yeni bakiye: {bakiye} TL")
    elif i=="bakiye sorgulama":
        print(f"Mevcut bakiyeniz: {bakiye} TL")
    else:
        print("Geçersiz işlem. Lütfen tekrar deneyin.")