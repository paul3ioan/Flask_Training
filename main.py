class Preturi_uorezculapti():
    def __init__(self, nume, cant):
        self.name=nume
        self.price=(10, 8, 11, 9.5)
        self.quantity=cant
    def __str__(self):
        return "Esti prost nu stii sintaxa"
    def raportcantpret(self):
        return max([self.quantity/i for i in self.price])
    def minpret(self):
        return min([i for i in self.price])

aliment=Preturi_uorezculapti("uorez cu lapti", 500)
print(aliment.raportcantpret())
print(aliment.minpret())