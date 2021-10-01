class Ayam:
    def _init_(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    def bersuara(self):
        print("Kukuruyuk")

class Sapi:
    def _init_(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    def bersuara(self):
        print("Mooooo")

ayam1 = Ayam("Rembo", 2)
Sapi1 = Sapi("Cowy", 3)

for hewan in (ayam1, Sapi1):
    hewan.bersuara()

class Burung:
    def intro(self):
        print("Di dunia ini terdapat beberapa jenis berbeda dari spesies burung")

    def terbang(self):
        print("Hampir semua jenis burung dapat terbang. Namun ada beberapa yang tidak dapat terbang")

class Gagak(Burung):
    def terbang(self):
        print("Burung gagak dapat terbang")

class Penguin(Burung):
    def terbang(self):
        print("Penguin tidak dapat terbang")

obj_burung = Burung()
obj_Gagak = Gagak()
obj_penguin = Penguin()

obj_burung.intro()
obj_burung.terbang()

obj_Gagak.intro()
obj_Gagak.terbang()

obj_penguin.intro()
obj_penguin.terbang()