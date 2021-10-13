class Personne:

    # region Initialisateur
    def __init__(self, nom, prenom, reg_nat):
        self.__nom = nom
        self.__prenom = prenom
        self.__reg_nat = reg_nat

    # endregion

    # region Props
    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def prenom(self):
        return self.__prenom

    @prenom.setter
    def prenom(self, value):
        self.__prenom = value

    @property
    def reg_nat(self):
        return self.__reg_nat

    @reg_nat.setter
    def reg_nat(self, value):
        self.__reg_nat = value
    # endregion

    # region Méthodes
    def arriver(self):
        print(self, "arrive")

    def quitter(self):
        print(self, "quitte")

    def faire_pause(self):
        print(self, "fait sa pause")

    def repondre(self, personne):
        print(self, "ne sait pas répondre")

    def __str__(self):
        return "{} {}".format(self.prenom, self.nom)
    # endregion
