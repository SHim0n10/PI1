class Zvieratko:
    def __init__(self, meno):
        self.meno = meno
    def jedz(self,jedlo):
        print(f"{self.meno}: {jedlo} mi chuti!")


class Macka(Zvieratko):
    def urob_zvuk(self):
        print(f"{self.meno}: Mňau!")

    def jedz(self, jedlo):
        super().jedz("Sunka")
        print(f"{self.meno}: {jedlo} mi nechuti.")

class Pes(Zvieratko):
    def urob_zvuk(self):
        print(f"{self.meno}: Haf!")

macka = Macka("Micka")
pes = Pes("Falko")

macka.jedz("šunka")
macka.urob_zvuk()

pes.jedz("šunka")
pes.urob_zvuk()

# POLYMORFIZMUS
zvierata = [Macka("Naginy"), Pes("Azor")]

for zviera in zvierata:
    zviera.jedz("Granulka")
    zviera.urob_zvuk()

# GENERALIZACIA