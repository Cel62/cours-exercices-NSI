# Exercice 1
def max_dico(dico):
    valeur_max = 0
    for keys in dico:
        if dico[keys] >= valeur_max:
            valeur_max = dico[keys]
            name = keys
    return (name, valeur_max)

# Exercice 2
class Pile:
    
    """Classe définissant une structure de pile."""
    def __init__(self):
        self.contenu = []
        
    def est_vide(self):
    """Renvoie le booléen True si la pile est vide, False sinon."""
        return self.contenu == []
    
    def empiler(self, v):
        """Place l’élément v au sommet de la pile."""
        self.contenu.append(v)
        
    def depiler(self):
    """Retire et renvoie l’élément placé au sommet de la pile,
    si la pile n’est pas vide."""
    if not self.est_vide():
        return self.contenu.pop()
    
def eval_expression(tab):
    p = Pile()
    for element in tab:
        if element != '+' or element != '*':
            p.empiler(element)
        else:
            if element == '+':
                resultat = p.depiler() + p.depiler()
            else:
                resultat = p.depiler() * p.depiler()
            p.empiler(resultat)
    return p.depiler()