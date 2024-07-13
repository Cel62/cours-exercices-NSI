class Pile:
    """
    Implémentation de la structure de données linéaire "Pile" sous forme de classe,
    à l'aide d'une liste Python (tableau dynamique)
    """
    def __init__(self):
        """
        Constructeur de la classe Pile : crée une instance vide de la classe Pile,
        ici : une liste vide []
        retour_type : <Pile object>
        Exemple:
        >>> p=Pile()
        """
        self.__contenu = []
    
    def est_vide(self):
        """
        Prédicat qui renvoie True si l'objet de type Pile auquel on
        applique le prédicat ne contient pas d'élément, et False sinon
        param : 
        param_type : <Pile object>
        retour : True or False
        retour_type : <class 'bool'>
        Exemple:
        >>> p=Pile()
        >>> p.est_vide()
        True
        >>>
        """
        return self.__contenu == []
    
    def empiler(self, element):
        """
        Méthode qui permet d'ajouter l'élément passé en argument au
        sommet de l'objet de type Pile auquel on applique la méthode
        param1 : 
        param1_type : <Pile object>
        param2 : un "élément"
        param2_type : type associé à l'élément empilé
        retour : 
        retour_type : <Pile object>
        effet de bord : oui (objet modifié)
        Exemple:
        >>> p=Pile()
        >>> p.empiler(5)
        >>> p.est_vide()
        False
        >>>
        """
        self.__contenu.append(element)
    
    def depiler(self):
        """
        Méthode qui permet de récupérer l'élément situé au sommet
        de l'objet de type Pile auquel on applique la méthode
        en le supprimant de l'objet
        param1 : 
        param1_type : <Pile object>
        retour : un "élément"
        retour_type : type associé à l'élément dépilé
        effet de bord : oui (objet modifié)
        Exemple:
        >>> p=Pile()
        >>> p.empiler(5)
        >>> p.est_vide()
        False
        >>> p.depiler()
        5
        >>> p.est_vide()
        True
        >>> 
        """
        if not self.est_vide():
            return self.__contenu.pop()
    
    def sommet(self):
        """
        Méthode qui permet de récupérer l'élément situé au sommet
        de l'objet de type Pile auquel on applique la méthode
        SANS le supprimer de l'objet
        param1 : 
        param1_type : <Pile object>
        retour : un "élément"
        retour_type : type associé à l'élément dépilé
        effet de bord : non
        Exemple:
        >>> p=Pile()
        >>> p.est_vide()
        True
        >>> p.empiler(5)
        >>> p.empiler(3)
        >>> p.sommet()
        3
        """
        if not self.est_vide():
            return self.__contenu[-1]
    
    def taille(self):
        """
        Méthode qui permet d'obtenir le nombre d'éléments contenus
        dans l'objet de type Pile auquel on applique la méthode
        param1 : 
        param1_type : <Pile object>
        retour : un nombre
        retour_type : <class 'int'>
        effet de bord : non
        Exemple:
        >>> p=Pile()
        >>> p.est_vide()
        True
        >>> p.taille()
        0
        >>> p.empiler(5)
        >>> p.empiler(3)
        >>> p.est_vide()
        False
        >>> p.taille()
        2
        """
        if not self.est_vide():
            return len(self.__contenu)
        else:
            return 0
    
    def affiche(self):
        """
        Méthode qui permet d'afficher les éléments contenus
        dans l'objet de type Pile auquel on applique la méthode
        sous la forme d'une liste Python
        Cette méthode n'est pas censée exister puisqu'elle fait
        apparaître la structure utilisée pour réaliser la classe Pile
        param1 : 
        param1_type : <Pile object>
        retour : la liste des éléments de la pile
        retour_type : <class 'list'>
        effet de bord : non
        Exemple:
        >>> p=Pile()
        >>> p.est_vide()
        True
        >>> p.affiche()
        []
        >>> p.empiler(5)
        >>> p.empiler(3)
        >>> p.affiche()
        [5, 3]
        >>> p.depiler()
        3
        >>> p.affiche()
        [5]
        """
        return self.__contenu

class File:
    """
    Implémentation de la structure de données linéaire "File" sous forme de classe,
    à l'aide d'une liste Python (tableau dynamique)
    """
    def __init__(self):
        """
        Constructeur de la classe File : crée une instance vide de la classe File,
        ici : une liste vide []
        retour_type : <File object>
        Exemple:
        >>> f=File()
        """
        self.__contenu = []
    
    def est_vide(self):
        """
        Prédicat qui renvoie True si l'objet de type File auquel on
        applique le prédicat ne contient pas d'élément, et False sinon
        param : 
        param_type : <File object>
        retour : True or False
        retour_type : <class 'bool'>
        Exemple:
        >>> f=File()
        >>> f.est_vide()
        True
        >>>
        """
        return self.__contenu == []
    
    def enfiler(self, element):
        """
        Méthode qui permet d'ajouter l'élément passé en argument au
        bout de l'objet de type File auquel on applique la méthode
        param1 : 
        param1_type : <File object>
        param2 : un "élément"
        param2_type : type associé à l'élément enfilé
        retour : 
        retour_type : <File object>
        effet de bord : oui (objet modifié)
        Exemple:
        >>> f=File()
        >>> f.enfiler(5)
        >>> f.est_vide()
        False
        >>>
        """
        self.__contenu.append(element)
    
    def defiler(self):
        """
        Méthode qui permet de récupérer l'élément situé au sommet
        de l'objet de type File auquel on applique la méthode
        en le supprimant de l'objet
        param1 : 
        param1_type : <File object>
        retour : un "élément"
        retour_type : type associé à l'élément défilé
        effet de bord : oui (objet modifié)
        Exemple:
        >>> f=File()
        >>> f.enfiler(5)
        >>> f.est_vide()
        False
        >>> f.defiler()
        5
        >>> f.est_vide()
        True
        >>> 
        """
        if not self.est_vide():
            return self.__contenu.pop(0)
    
    def sommet(self):
        """
        Méthode qui permet de récupérer l'élément situé au sommet
        de l'objet de type File auquel on applique la méthode
        SANS le supprimer de l'objet
        param1 : 
        param1_type : <File object>
        retour : un "élément"
        retour_type : type associé à l'élément défilé
        effet de bord : non
        Exemple:
        >>> f=File()
        >>> f.est_vide()
        True
        >>> f.enfiler(5)
        >>> f.enfiler(3)
        >>> f.sommet()
        5
        """
        if not self.est_vide():
            return self.__contenu[0]
    
    def taille(self):
        """
        Méthode qui permet d'obtenir le nombre d'éléments contenus
        dans l'objet de type File auquel on applique la méthode
        param1 : 
        param1_type : <File object>
        retour : un nombre
        retour_type : <class 'int'>
        effet de bord : non
        Exemple:
        >>> f=File()
        >>> f.est_vide()
        True
        >>> f.taille()
        0
        >>> f.enfiler(5)
        >>> f.enfiler(3)
        >>> f.est_vide()
        False
        >>> f.taille()
        2
        """
        if not self.est_vide():
            return len(self.__contenu)
        else:
            return 0
    
    def affiche(self):
        """
        Méthode qui permet d'afficher les éléments contenus
        dans l'objet de type File auquel on applique la méthode
        sous la forme d'une liste Python
        Cette méthode n'est pas censée exister puisqu'elle fait
        apparaître la structure utilisée pour réaliser la classe File
        param1 : 
        param1_type : <File object>
        retour : la liste des éléments de la pile
        retour_type : <class 'list'>
        effet de bord : non
        Exemple:
        >>> f=File()
        >>> f.est_vide()
        True
        >>> f.affiche()
        []
        >>> f.enfiler(5)
        >>> f.enfiler(3)
        >>> f.affiche()
        [5, 3]
        >>> f.defiler()
        5
        >>> f.affiche()
        [3]
        """
        return self.__contenu


class Liste_chainee:
    """
    Implémentation de la structure de données linéaire "Liste chaînée" sous forme de classe,
    à l'aide de tuples
    """
    def __init__(self,tete=None,suivante=None):
        """
        Constructeur de la classe Liste_chainee : crée une instance de la classe Liste_chainee,
        soit un "None" objet si aucun argument n'est passé lors de l'appel du constructeur,
        soit un tuple composé d'un élément de tête et d'un objet du type Liste_chainee (appelé "suivante"),
        passés en paramètres
        retour_type : <Liste_chainee object>
        Exemple:
        >>> lc=Liste_chainee()
        """
        if tete == None:
            self.__cellule = None
        else:
            self.__cellule = (tete,suivante)
    
    def est_vide(self):
        """
        Prédicat qui renvoie True si l'objet de type Liste_chainee auquel on
        applique le prédicat ne contient pas d'élément, et False sinon
        param : 
        param_type : <Liste_chainee object>
        retour : True or False
        retour_type : <class 'bool'>
        Exemple:
        >>> lc=Liste_chainee()
        >>> lc.est_vide()
        True
        >>> lc=Liste_chainee(12,Liste_chainee())
        >>> lc.est_vide()
        False
        >>>
        """
        return self.__cellule is None
    
    def get_tete(self):
        """
        Accesseur : Méthode permettant d'accéder à la valeur de tête de l'objet de type
        Liste_chainee auquel on applique la méthode
        param1 : 
        param1_type : <Liste_chainee object>
        retour : un "élément"
        retour_type : type associé à l'élément de tête
        effet de bord : non
        Exemple:
        >>> lc=Liste_chainee(12,Liste_chainee())
        >>> lc.get_tete()
        12
        """
        if not self.est_vide():
            return self.__cellule[0]
        
    def get_suivante(self):
        """
        Accesseur : Méthode permettant d'accéder à la liste chaînée
        qui constitue la suite de l'objet de type Liste_chainee auquel
        on applique la méthode
        param1 : 
        param1_type : <Liste_chainee object>
        retour : une liste chaînée
        retour_type : <Liste_chainee object>
        effet de bord : non
        Exemple:
        >> lc=Liste_chainee(12,Liste_chainee())
        >> lc.get_suivante()
        <__main__.Liste_chainee object at 0x0363AE50> # exemple d'adresse associée à l'objet liste chaînée pointé
        """
        if not self.est_vide():
            return self.__cellule[1]
    
    def affiche(self,chaine='['):
        """
        Méthode qui permet d'afficher les éléments contenus
        dans l'objet de type Liste_chainee auquel on applique la méthode
        sous la forme d'une liste Python
        param1 : 
        param1_type : <Liste_chainee object>
        param2 : accumulateur contenant l'évolution de la chaîne de caractères
                constituant la représentation de la liste chaînée au fil du traitement
        param2_type : <class 'str'>
        retour : la liste des éléments de la liste chaînée
        retour_type : <class 'str'>
        effet de bord : non
        Exemple:
        >>> lc=Liste_chainee()
        >>> lc.affiche()
        '[]'
        >>> lc=Liste_chainee(12,Liste_chainee())
        >>> lc.affiche()
        '[12]'
        >>> lc=Liste_chainee(12,Liste_chainee(8,lc))
        >>> lc.affiche()
        '[12,8,12]'
        """
        if self.est_vide():
            return '[]'
        chaine += str(self.get_tete())
        if self.get_suivante().est_vide():
            return chaine + "]"
        else:
            return self.get_suivante().affiche(chaine + ',')
    
    def taille(self):
        """
        Méthode qui permet d'obtenir le nombre d'éléments contenus
        dans l'objet de type Liste_chainee auquel on applique la méthode
        param1 : 
        param1_type : <Liste_chainee object>
        retour : un nombre
        retour_type : <class 'int'>
        effet de bord : non
        Exemple:
        >>> lc=Liste_chainee()
        >>> lc.est_vide()
        True
        >>> lc.taille()
        0
        >>> lc=Liste_chainee(12,Liste_chainee(8,Liste_chainee()))
        >>> lc.est_vide()
        False
        >>> lc.affiche()
        '[12,8]'
        >>> lc.taille()
        2
        """
        if self.est_vide():
            return 0
        return 1 + self.get_suivante().taille()
    
    def __len__(self):
        """
        Méthode "spéciale" permettant d'obtenir le nombre d'éléments contenus
        dans l'objet de type Liste_chainee auquel on applique la méthode,
        en utilisant la commande "len" de Python
        param1 : 
        param1_type : <Liste_chainee object>
        retour : un nombre
        retour_type : <class 'int'>
        effet de bord : non
        Exemple:
        >>> lc=Liste_chainee()
        >>> lc.est_vide()
        True
        >>> len(lc)
        0
        >>> lc=Liste_chainee(12,Liste_chainee(8,Liste_chainee()))
        >>> lc.est_vide()
        False
        >>> lc.affiche()
        '[12,8]'
        >>> len(lc)
        2
        """
        return self.taille()
    
    def get_nieme_element(self,n):
        """
        Accesseur : Méthode permettant d'accéder au "nième" élément
        de l'objet de type Liste_chainee auquel on applique la méthode
        param1 : 
        param1_type : <Liste_chainee object>
        param2 : n, "indice" de l'élément recherché
        param2_type : <class 'int'>
        retour : une liste chaînée
        retour_type : <Liste_chainee object>
        effet de bord : non
        Exemple:
        >>> lc=Liste_chainee(12,Liste_chainee(8,Liste_chainee(5,Liste_chainee(3,Liste_chainee()))))
        >>> lc.affiche()
        '[12,8,5,3]'
        >>> lc.get_nieme_element(0).get_tete()
        12
        >>> lc.get_nieme_element(2).get_tete()
        5
        """
        assert not self.est_vide(),"Une liste vide n'a pas de "+str(n)+"ième élément !!!"
        assert n < self.taille(),"Il ne peut y avoir de "+str(n)+"ième élément dans une liste dont les index vont jusque "+str(self.taille()-1)+" !!!"
        if n == 0:
            return self
        else:
            return self.get_suivante().get_nieme_element(n-1)
    
    def get_dernier_element(self):
        """
        Accesseur : Méthode permettant d'accéder au dernier élément
        de l'objet de type Liste_chainee auquel on applique la méthode
        param1 : 
        param1_type : <Liste_chainee object>
        retour : une liste chaînée
        retour_type : <Liste_chainee object>
        effet de bord : non
        Exemple:
        >>> lc=Liste_chainee(12,Liste_chainee(8,Liste_chainee(5,Liste_chainee(3,Liste_chainee()))))
        >>> lc.affiche()
        '[12,8,5,3]'
        >>> lc.get_dernier_element().get_tete()
        3
        """
        if not self.est_vide():
            return self.get_nieme_element(len(self)-1)
    
    def concatenation(self,liste2):
        """
        Méthode permettant de concaténer la liste chaînée "liste2" passée en argument
        à l'objet de type Liste_chainee auquel on applique la méthode
        param1 : 
        param1_type : <Liste_chainee object>
        param2 : 
        param2_type : <Liste_chainee object>
        retour : une liste chaînée
        retour_type : <Liste_chainee object>
        effet de bord : non
        Exemple:
        >>> lc1=Liste_chainee(12,Liste_chainee(8,Liste_chainee(5,Liste_chainee(3,Liste_chainee()))))
        >>> lc2=Liste_chainee(1,Liste_chainee(7,Liste_chainee()))
        >>> lc3=lc1.concatenation(lc2)
        >>> lc3.affiche()
        '[12,8,5,3,1,7]'
        >>> lc4=lc2.concatenation(lc1)
        >>> lc4.affiche()
        '[1,7,12,8,5,3]'
        """
        if self.est_vide():
            return liste2
        return Liste_chainee(self.get_tete(),self.get_suivante().concatenation(liste2))
    
    def ajout_en_dernier(self,element):
        """
        Méthode permettant d'ajouter l'élément "element" passé en argument
        à la fin de l'objet de type Liste_chainee auquel on applique la méthode
        param1 : 
        param1_type : <Liste_chainee object>
        param2 : un "élément"
        param2_type : type associé à l'élément passé en argument
        retour : une liste chaînée
        retour_type : <Liste_chainee object>
        effet de bord : non
        Exemple:
        >>> lc1=Liste_chainee(12,Liste_chainee(8,Liste_chainee(5,Liste_chainee(3,Liste_chainee()))))
        >>> lc2=lc1.ajout_en_dernier(7)
        >>> lc1.affiche()
        '[12,8,5,3]'
        >>> lc2.affiche()
        '[12,8,5,3,7]'
        """
        return self.concatenation(Liste_chainee(element,Liste_chainee()))
    
    def suppression_du_dernier(self):
        """
        Méthode permettant de supprimer le dernier élément
        de l'objet de type Liste_chainee auquel on applique la méthode
        param1 : 
        param1_type : <Liste_chainee object>
        retour : une liste chaînée
        retour_type : <Liste_chainee object>
        effet de bord : non
        Exemple:
        >>> lc1=Liste_chainee(12,Liste_chainee(8,Liste_chainee(5,Liste_chainee(3,Liste_chainee()))))
        >>> lc2=lc1.suppression_du_dernier()
        >>> lc1.affiche()
        '[12,8,5,3]'
        >>> lc2.affiche()
        '[12,8,5]'
        """
        if self == self.get_dernier_element():
            return Liste_chainee()
        return Liste_chainee(self.get_tete(),self.get_suivante().suppression_du_dernier())
    
    def n_premiers_elements(self,n):
        """
        Méthode permettant d'obtenir une liste chaînée contenant les "n" premiers éléments
        de l'objet de type Liste_chainee auquel on applique la méthode
        param1 : 
        param1_type : <Liste_chainee object>
        param2 : n, un nombre
        param2_type : <class 'int'>
        retour : une liste chaînée
        retour_type : <Liste_chainee object>
        effet de bord : non
        Exemple:
        >>> lc1=Liste_chainee(12,Liste_chainee(8,Liste_chainee(5,Liste_chainee(3,Liste_chainee()))))
        >>> lc2=lc1.n_premiers_elements(2)
        >>> lc1.affiche()
        '[12,8,5,3]'
        >>> lc2.affiche()
        '[12,8]'
        """
        assert not self.est_vide()
        assert n>0 and n<=self.taille()
        liste_tampon = self
        for _ in range(self.taille()-n):
            liste_tampon = liste_tampon.suppression_du_dernier()
        return liste_tampon
    
    def insertion_liste_dans_liste(self,liste_inseree,index):
        """
        Méthode permettant d'insérer la liste chaînée "liste_inseree" passée en argument
        dans l'objet de type Liste_chainee auquel on applique la méthode, à l'index passé en argument
        param1 : 
        param1_type : <Liste_chainee object>
        param2 : 
        param2_type : <Liste_chainee object>
        param3 : index
        param3_type : <class 'int'>
        retour : une liste chaînée
        retour_type : <Liste_chainee object>
        effet de bord : non
        Exemple:
        >>> lc1=Liste_chainee(12,Liste_chainee(8,Liste_chainee(5,Liste_chainee(3,Liste_chainee()))))
        >>> lc2=Liste_chainee(1,Liste_chainee(7,Liste_chainee()))
        >>> lc3=lc1.insertion_liste_dans_liste(lc2,1)
        >>> lc1.affiche()
        '[12,8,5,3]'
        >>> lc2.affiche()
        '[1,7]'
        >>> lc3.affiche()
        '[12,1,7,8,5,3]'
        """
        assert not self.est_vide()
        assert index>=0 and index<self.taille()
        liste_fin = liste_inseree.concatenation(self.get_nieme_element(index))
        liste_debut = self.n_premiers_elements(index)
        return liste_debut.concatenation(liste_fin)
    
    def insertion_element_dans_liste(self,element,index):
        """
        Méthode permettant d'insérer l'élément "element" passé en argument
        dans l'objet de type Liste_chainee auquel on applique la méthode, à l'index passé en argument
        param1 : 
        param1_type : <Liste_chainee object>
        param2 : élément
        param2_type : type associé à l'élément à insérer
        param3 : index
        param3_type : <class 'int'>
        retour : une liste chaînée
        retour_type : <Liste_chainee object>
        effet de bord : non
        Exemple:
        >>> lc1=Liste_chainee(12,Liste_chainee(8,Liste_chainee(5,Liste_chainee(3,Liste_chainee()))))
        >>> lc2=lc1.insertion_element_dans_liste(7,2)
        >>> lc1.affiche()
        '[12,8,5,3]'
        >>> lc2.affiche()
        '[12,8,7,5,3]'
        """
        assert not self.est_vide()
        assert index>=0 and index<self.taille()
        return self.insertion_liste_dans_liste(Liste_chainee(element,Liste_chainee()),index)
        
    def inversion_liste(self):
        """
        Méthode permettant d'inverser l'ordre des éléments
        de l'objet de type Liste_chainee auquel on applique la méthode
        param1 : 
        param1_type : <Liste_chainee object>
        retour : une liste chaînée
        retour_type : <Liste_chainee object>
        effet de bord : non
        Exemple:
        >>> lc=Liste_chainee(12,Liste_chainee(8,Liste_chainee(5,Liste_chainee(3,Liste_chainee()))))
        >>> lc.affiche()
        '[12,8,5,3]'
        >>> lc2=lc.inversion_liste()
        >>> lc2.affiche()
        '[3,5,8,12]'
        """
        if self.est_vide():
            return Liste_chainee()
        return Liste_chainee(self.get_dernier_element().get_tete(),self.suppression_du_dernier().inversion_liste())

if __name__ == "__main__":
    import doctest
    doctest.testmod()