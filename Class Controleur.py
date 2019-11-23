#coding: utf-8

class Controleur:
    def __init__(self, soldeCaisse, operation):
        self.soldeCaisse = soldeCaisse
        self.operation = operation
    def verifier(self):
        if self.soldeCaisse == self.operation:
            print("Tout va pour le mieu")
        else :
            print("La somme des opérations journalières ne cadre pas avec le solde en caisse(problème)")


print("Une operation est l'ensemble des transactions journalière éffectuer dans une banque ")

c1 = Controleur(2000000, 2000000)
c1.verifier()

c2 = Controleur(10000000, 500000)
c2.verifier()
print("A reverifier en cas de problème.........")

