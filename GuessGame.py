# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 00:13:28 2024

@author: eamir
"""

from random import randint


t_s=0
tahmin=randint(1,100)
dogrutahmin=False
while (dogrutahmin==False): # for ile yapınız.
    girilensayi=int(input("Bir tahmin yapın(1-100): (çıkmak için sıfıra basın) "))
    t_s+=1
    if  t_s== 5 :
       print(f"{t_s}.hakkınız ile tahmin hakkınız bitti")
       break
    if (girilensayi==0):
        print("oyundan çıktınız..")
        break
    elif (girilensayi<tahmin):
        print("Küçük sayı girdiniz. daha yüksek giriniz..")
        continue #░altındaki satırı çalıştırmaz.
    elif girilensayi>tahmin:
        print("Büyük sayı girdiniz. Daha küçük giriniz:")
        continue
    else:
        dogrutahmin=True
        print(f"{t_s} denemede Doğru tahmin ettiniz. Rastgele üretilen sayı: {tahmin}")