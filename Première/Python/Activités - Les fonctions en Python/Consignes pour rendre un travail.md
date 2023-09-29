# Consignes pour rendre un travail

##### Pour une **correction efficace**, et donc avoir une bonne note ;-)

* **Respecter le nom de fichier** demandé (en respectant la casse)

* **L'exécution d'un programme ne doit pas provoquer d'erreur** (mettre le code erroné en commentaire dans ce cas)

* **Si une fonction n’a pas été abordée** par manque de temps : la définir avec le nom demandé, définir les paramètres, puis et écrire `pass`
  
  ```python
  def nom_fonction(param1, param2):
          pass
  ```

* **Ne pas oublier les docstrings et les doctests** (s'inspirer des énoncés)

* **La fonction print() peut être utilisée que pour faire des mises au point** et ne doit pas apparaitre dans le code (ou alors sous forme de commentaire). L'usage de cette fonction doit être très exceptionnel !

* **Sur les trois premières lignes de votre programme, faire apparaitre le nom de votre programme, vos nom et prénom** (et éventuellement des lignes supplémentaires pour donner la version ou toute autre information) :
  
  ```python
  # Programme : Projet_ADN
  # Nom : Turing
  # Prénom : Alan
  # version 1.1 créée le 2/12/19 en NSI
  ```

* **Ajouter le code ci-dessous à la fin de votre programme** afin d'utiliser les doctests insérés dans votre code.
  
  ```python
  if __name__ == '__main__':
      import doctest
      doctest.testmod(verbose=True)
  ```
