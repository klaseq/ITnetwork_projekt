class Pojistenec:
    def __init__(self, jmeno, prijmeni, vek, cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.cislo = cislo
    
    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}, vek: {self.vek}, tel: {self.cislo}"