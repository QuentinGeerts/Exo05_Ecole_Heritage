class Ecole:

    def __init__(self, nom, prof):
        self.__nom = nom
        self.__prof = prof
        self.__eleves = list()


    @property
    def nom(self):
        return self.__nom

    @property
    def prof(self):
        return self.__prof

    def ajouter_eleve(self, eleve):
        if eleve in self.__eleves:
            raise ValueError

        self.__eleves.append(eleve)



    def ouverture(self):
        self.prof.arriver()
        for e in self.__eleves:
            e.arriver()

    def fermeture(self):
        for e in self.__eleves:
            e.quitter()
        self.prof.quitter()

    def debuter_cours(self, cours):
        self.prof.donner_cours(cours)

        for eleve in self.__eleves:
            eleve.suivre_cours(cours)

    def faire_pause(self):
        for eleve in self.__eleves:
            eleve.faire_pause()

        self.prof.faire_pause()