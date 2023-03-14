class Person:
    def __init__(self,fullname):
        self.fullname = fullname

        





musteri = input("Ad Soyad giriniz(boşluk bırakarak):")
kayit = Person(musteri)
print(kayit.fullname)