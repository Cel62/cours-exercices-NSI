import doctest

class Pile:
    def __init__(self, contenu):
        self.__contenu = contenu
    
    def pile_vide(self):
        """
        Permet de savoir si la pile est vide ou non
        :return: Renvoie la valeur "True" si la pile est vide sinon renvoie "False"
        :rtype: bool
        """
        return self.__contenu == []

    def empiler(self, element):
        """
        Permet d'empiler un élément
        :param element: L'élément à empiler
        """
        self.__contenu.append(element)
    
    def depiler(self):
        """
        Permet de dépiler le sommet
        """
        if not self.pile_vide():
            return self.__contenu.pop()
        return "Problème avec la méthode depiler"
    
    def sommet(self):
        """
        Permet d'obtenir le sommet
        :return: Renvoie un message si le sommet de la pile ne peut pas être récupérer
        :rtype: str
        """
        if not self.pile_vide():
            return self.__contenu[-1]
        return "Problème avec la méthode sommet"

    def taille(self):
        """
        Permet d'obtenir la taille de la pile
        :return: Renvoie la taille de la liste
        :rtype: int
        """
        return len(self.__contenu)
    
    def showContenu(self):
        """
        Permet d'afficher le contenu de la pile
        """
        print(self.__contenu)

doctest.testmod(verbose=False)