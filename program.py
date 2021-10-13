from models.ecole import Ecole
from models.eleve import Eleve
from models.prof import Prof

p = Prof("Duck", "Donald", "70.01.01-001.01")

ecole = Ecole("TechnoBel", p)

ecole.ajouter_eleve(Eleve("Vanderquack", "Zaza", "99.01.01-042.01", "Peche à la mouche"))
ecole.ajouter_eleve(Eleve("Duck", "Riri", "97.01.01-013.20", "Aimer les avions"))
ecole.ajouter_eleve(Eleve("Duck", "Fifi", "97.10.01-013.20", "Aimer les trains"))

ecole.ouverture()
print()

ecole.debuter_cours("Python")
print()
ecole.faire_pause()
print()
ecole.debuter_cours("Python")
print()


ecole.fermeture()







