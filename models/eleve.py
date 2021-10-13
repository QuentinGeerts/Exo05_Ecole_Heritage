from models.personne import Personne
import random


class Eleve(Personne):

    def __init__(self, nom, prenom, reg_nat, hobby):
        super().__init__(nom, prenom, reg_nat)
        self.__hobby = hobby

    @property
    def hobby(self):
        return self.__hobby

    @hobby.setter
    def hobby(self, value):
        self.__hobby = value

    def suivre_cours(self, cours):
        print(self, "suit le cours de", cours)

    def poser_question(self, cible, question):
        print(self, "demande à", cible, ":", question)

        if isinstance(cible, Personne):
            cible.repondre(self)
        else:
            print("...")

    def repondre(self, personne):

        if random.randrange(0, 2) == 0:
            print(self, "explique à", personne)
        else:
            super().repondre(personne)
