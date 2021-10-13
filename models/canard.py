class Canard:

    def __init__(self, nom):
        self.__nom = nom

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    def __str__(self):
        return "un canard jaune"

if __name__ == '__main__':
    from models.eleve import Eleve

    c = Canard("Donald")
    e1 = Eleve("Vanderquack", "Zaza", "123456789", "Manger des pommes")
    e2 = Eleve("Picsou", "Balthazar", "123456782", "Avoir de l'argent")


    e1.poser_question(e2, "Il fait beau?")
    print()

    e1.poser_question(c, "Pourquoi le code bug?")