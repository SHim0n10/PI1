from random import choice

class Generator():
    def __init__(self):
        self.pridavne_meno = ["veľký", "malý", "nízky", "obdivuhodný", "guľatý"]
        self.podstatne_meno = ["chlap", "mäsiar", "manažér", "stavbár"]
        self.prislovka = ["rýchlo", "pomaly", "ladne"]
        self.sloveso = ["spal", "skákal", "upratoval"]
        self.miesto = ["u babky", "pod stolom", "v práci"]
        self.veta = ["", "", "", "", ""]
    def generate(self):
            self.veta[0] = choice(self.pridavne_meno)
            self.veta[1] = choice(self.podstatne_meno)
            self.veta[2] = choice(self.prislovka)
            self.veta[3] = choice(self.sloveso)
            self.veta[4] = choice(self.miesto)
            for i in range(len(self.veta)):
                print(self.veta[i], end=' ')
            print("")


gener = Generator()
gener.generate()
gener.generate()
gener.generate()
gener.generate()
gener.generate()
gener.generate()
gener.generate()
gener.generate()

