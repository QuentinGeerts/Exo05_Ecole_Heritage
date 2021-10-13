from models.personne import Personne
import random


class Prof(Personne):

    def __init__(self, nom, prenom, reg_nat):
        super().__init__(nom, prenom, reg_nat)

    @property
    def nom(self):
        return super().nom.upper()

    def donner_cours(self, cours):
        print(self, "donne cours de", cours)

    def repondre(self, personne):

        rng = random.randrange(0, 10)
        if rng < 7:
            print(self, "donne une réponse à", personne)
        elif rng < 9:
            print(self, "se renseigne")
        else:
            super().repondre(personne)


