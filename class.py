#class Matematik: --> classları adlandırırken ilk harf büyük
#class Matematik:
#    def __init__(self):
#        print("Matematik Başladı")#-->Class ı çağırdığın zaman hangi fonskyionu seçersen seç çalışan fonksiyondur init
#    def topla(self,sayi1,sayi2):
#        return sayi1 + sayi2
#    def cikar(self,sayi1,sayi2):
#        return sayi1 - sayi2
#    def bol(self,sayi1,sayi2):
#        return sayi1 / sayi2
#    def carp(self,sayi1,sayi2):
#        return sayi1 * sayi2
    

#matematik = Matematik()
#sonuc = matematik.topla(2,8)
#print(f"Sonuc:{sonuc}")

#<--ÇOK GÜZEL VERSİYONU-->

class Matematik:
    def __init__(self,sayi1,sayi2):#-->init ile fonskiyonlarda yapacağın işlemler için hepsinde sayi1 ve sayi2 kullanmanı sağlar
        self.s1 = sayi1#-->bunu yapmamızın sebebi sadece matematik class ında kullanabileceğimiz değerleri atayabilmek için onun dışına çıkmaması için self yapıyoruz
        self.s2 = sayi2
        print("matematik başladı")
    def topla(self):
        return self.s1 + self.s2
    def cikar(self):
        return self.s1 - self.s2
    def bol(self):
        return self.s1 / self.s2
    def carp(self):
        return self.s1 * self.s2
    

matematik = Matematik(8,2)
sonuc = matematik.topla()
print(f"Sonuc:{sonuc}")
