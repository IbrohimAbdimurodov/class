class Kompaniya:
    def __init__(self, nomi, yili, ishchilari):
        self.nomi = nomi
        self.yili = yili
        self.ishchilari = ishchilari
    
    def shifr(self):
        print(self.ismi, self.familiya, self.yoshi)

class Google(Kompaniya):
    def __init__(self, nomi, yili, ishchilari, foydasi, zarari):
        super().__init__( nomi, yili, ishchilari)
        self.foydasi = foydasi
        self.zarari = zarari

    def shifr(self):
        print("Nomi:", self.nomi,"Yili:", self.yili,"Ishchilari:", self.ishchilari,"Foydasi:", self.foydasi,"Zarari:", self.zarari)

o1 = Google("Google", "1996", "140.000", "557mlrd", "32ml")


class GM(Kompaniya):
    def __init__(self, nomi, yili, ishchilari, foydasi, zarari):
        super().__init__( nomi, yili, ishchilari)
        self.foydasi = foydasi
        self.zarari = zarari

    def shifr(self):
       print("Nomi:", self.nomi,"Yili:", self.yili,"Ishchilari:", self.ishchilari,"Foydasi:", self.foydasi,"Zarari:", self.zarari)


g1 = GM("GM", "1997", "10.000", "902mlrd", "850mln")



class Yandex(Kompaniya):
    def __init__(self, nomi, yili, ishchilari, foydasi, zarari):
        super().__init__( nomi, yili, ishchilari)
        self.foydasi = foydasi
        self.zarari = zarari

    def shifr(self):
       print("Nomi:", self.nomi,"Yili:", self.yili,"Ishchilari:", self.ishchilari,"Foydasi:", self.foydasi,"Zarari:", self.zarari)

y1= Yandex("Yandex", "1997","20.000","356mlrd","903mln")


g1.shifr()
y1.shifr()
o1.shifr()