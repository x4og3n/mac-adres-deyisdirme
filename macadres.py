#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet MAC Deyisdirme")
print("""
MAC Adres chang by xtogen, xais olunur root istifadecisi olaraq davam edin 

1) MAC Adresi Random Yarat
2) MAC Adresi Elle Yarat
3) MAC Adresi Orijinala Qaytar
""")

islemno = input("İşlem No Girin: ")

if(islemno=="1"):
  os.system("ifconfig eth0 down")
  os.system("macchanger -r eth0")
  os.system("ifconfig eth0 up")
  print("Yeni MAC Adresi Random Yaradildi.")


if(islemno=="2"):
  macadres = input("Yeni MAC Adres Yaz: ")
  os.system("ifconfig eth0 down")
  os.system("macchanger --mac " + macadres + " eth0")
  os.system("ifconfig eth0 up")
  print("Yeni MAC Adresi Elle Yaradildi.")

if(islemno=="3"):
  os.system("ifconfig eth0 down")
  os.system("macchanger -p eth0")
  os.system("ifconfig eth0 up")
  print("MAC Adresi Orijinale Qaytarildi.")

