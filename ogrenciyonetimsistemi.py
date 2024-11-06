# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 23:14:19 2024

@author: eamir
"""



list={}

while True:
    i=input("bir işlem seçiniz: ")
    if i=="çıkış":
        print("Çıkış yapılıyor...")
    if i=="ekleme":
       ıd=int(input("ID giriniz: ")) 
       if ıd in list:
           print("Bu ID'ye sahip bir öğrenci zaten var!")
       else:
         ad=input("adını soyadını giriniz: ")
         nott=input("notunuzu giriniz: ")
         list[ıd]={"Tam_ad":ad ,"not":nott}
         print(f"{ıd} ID'li öğrenci başarıyla eklendi.")
    elif i=="öğrenci silme" or i=="silme":
        ıd=int(input("silmek istediğiniz öğrencinin ID'sini giriniz: "))
        if ıd in list:
            del list[ıd]
            print(f"{ıd} ID'li öğrenci başarıyla silindi.")       
        else:    
            print("Bu ID'ye sahip bir öğrenci bulunamadı!")
    elif i=="listele":
        if not list:
            print("henüz listede kimse yok!")
        else:
            print("Mevcut Öğrenciler:")
            for ıd, bilgiler in list.items():
                print(f"ID: {ıd}, Ad Soyad: {list[ıd]['Tam_ad']}, Not: {list[ıd]['not']}")
    else:
        print("Geçersiz işlem. Lütfen tekrar deneyin.")
          