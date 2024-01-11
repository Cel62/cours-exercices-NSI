import doctest

class File:
    def __init__(self, contenu = []):
        self.__contenu = contenu
    
    def file_vide(self):
        """
        Permet de savoir si la file est vide ou non
        :return: Renvoie la valeur "True" si la file est vide sinon renvoie "False"
        :rtype: bool
        """
        return self.__contenu == []

    def enfiler(self, element):
        """
        Permet d'enfiler un élément
        :param element: L'élément à enfiler
        """
        self.__contenu.insert(0, element)
    
    def defiler(self):
        """
        Permet de défiler le sommet
        """
        if not self.file_vide():
            return self.__contenu.pop(-1)
        return "Problème avec la méthode defiler"
    
    def premier(self):
        """
        Permet d'obtenir le premier
        :return: Renvoie un message si le premier de la file ne peut pas être récupérer
        :rtype: str
        """
        if not self.file_vide():
            return self.__contenu[-1]
        return "Vous ne pouvez pas récupérer le premier de cette file."

    def taille(self):
        """
        Permet d'obtenir la taille de la pile
        :return: Renvoie la taille de la liste
        :rtype: int
        """
        return len(self.__contenu)
    
    def showContenu(self):
        """
        Permet d'afficher le contenu de la file
        """
        print(self.__contenu)

doctest.testmod(verbose=False)