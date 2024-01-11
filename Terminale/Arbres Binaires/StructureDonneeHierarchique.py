from file import File

class AB:
    def __init__(self, etiquette = None, sag = None, sad = None):
        self.etiquette = etiquette
        self.sag = sag
        self.sad = sad
    
    def est_vide(self):
        if self.etiquette is None:
            return True
        return False

    def taille(self):
        if self.est_vide():
            return 0
        return 1 + self.sag.taille() + self.sad.taille()

    def hauteur(self):
        if self.est_vide():
            return -1
        return 1 + max(self.sag.hauteur(), self.sad.hauteur())
    
    def parcours_infixe(self, parcours = None):
        if parcours == None:
            parcours = []
        if not self.est_vide():
            self.sag.parcours_infixe(parcours)
            parcours += [self.etiquette]
            self.sad.parcours_infixe(parcours)
        return parcours
    
    def parcours_prefixe(self, parcours = None):
        if parcours == None:
            parcours = []
        if not self.est_vide():
            parcours += [self.etiquette]
            self.sag.parcours_prefixe(parcours)
            self.sad.parcours_prefixe(parcours)
        return parcours
    
    def parcours_suffixe(self, parcours = None):
        if parcours == None:
            parcours = []
        if not self.est_vide():
            self.sag.parcours_suffixe(parcours)
            self.sad.parcours_suffixe(parcours)
            parcours += [self.etiquette]
        return parcours
        
    def parcours_largeur(self):
        parcours = []
        f = File()
        f.enfiler(self)
        while not f.file_vide():
            x = f.defiler()
            parcours.append(x.etiquette)
             
            if not x.sag.est_vide():
                f.enfiler(x.sag)
            if not x.sad.est_vide():
                f.enfiler(x.sad)
        return parcours
            
a = AB("H", AB(), AB())

a.sag = AB("D", AB(), AB())
a.sag.sag = AB("B", AB(), AB())
a.sag.sag.sag = AB("A", AB(), AB())
a.sag.sag.sad = AB("C", AB(), AB())
a.sag.sad = AB("F", AB(), AB())
a.sag.sad.sag = AB("E", AB(), AB())
a.sag.sad.sad = AB("G", AB(), AB())

a.sad = AB("J", AB(), AB())
a.sad.sag = AB("I", AB(), AB())
a.sad.sad = AB("K", AB(), AB())