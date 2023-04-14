# -*- coding: utf-8 -*-
"""Hesap eklemede yardım aldım"""
from Person import Person
kullanici1=Person("Bora","Avcı","borabora2")
kullanici2=Person("Güncel","Sarıman","Guncel1234")
kullanici_listesi=[]
kullanici_listesi.append(kullanici1)
kullanici_listesi.append(kullanici2)
iscorrect=False
SMS=1234 #aslında random olmalı
while(True):
    print("Sisteme Hoşgeldiniz.\nGiriş Yap-1\nŞifremi Unuttum-2\n")
    islem=int(input("İşlem:"))
    if(islem==1):
        ad=str(input("Adınız:"))
        soyad=str(input("Soyadınız:"))
        sifre=str(input("Şifreniz:"))
        for i in kullanici_listesi:
            if i.ad==ad and i.soyad==soyad and i.sifre==sifre:
                iscorrect=True
        if iscorrect:
            print("Giriş başarılı.")
            break
        else:
            print("Giriş başarısız.")
   
    elif(islem==2):        
        ad=str(input("Adınız:"))
        soyad=str(input("Soyadınız:"))
        print("SMS Kodu gönderildi.")
        while(True):
            kod=int(input("Kodu giriniz:"))
            if(kod==SMS):
                while(True):
                    yeni=input("Yeni şifrenizi girin:")
                    if yeni == sifre:
                        print("Yeni şifreniz eskisiyle aynı olamaz.")
                        continue
                    else:
                        print("Yeni şifre kullanıma girmiştir.")
                        sifre=yeni
                        break
                break    
            else:
                print("Hatalı kod girildi. Tekrar deneyin.\n")
                continue
    else:
        print("Hatalı işlem.")               
        
        
    
        
        

