# Utilisation d'un système libre

---

**Objectifs :**

* Utiliser les commandes de base en ligne de commande d'un système d'exploitation

* Gérer les droits et permissions d'accès aux fichiers 

**Pré-requis :**

* Avoir des notions de base sur les fichiers, les répertoires et l'arborescence

* Savoir mettre en marche une machine virtuelle fonctionnant sous VirtualBox

**Préparations :**

* Mettre en place une machine virtuelle en utilisant la distribution [Debian Stetch Raspberry Pi Desktop](https://www.raspberrypi.org/downloads/raspberry-pi-desktop/)
* Donner le mot de passe de l'utilisateur pi (s'il a été modifié)

**Séance pratique :**

* Réaliser les activités proposées ci-dessous, et compléter le fichier avec les commandes utilisées et les résultats obtenus.
  
  > Les activités à réaliser sont répérées par un `quote block`, c'est à dire un paragraphe avec une indentation et un trait sur le côté gauche comme ce bloc.

---

## Découverte de l'environnement

Le raspberry est un nano-ordinateur de la taille d'une carte de crédit qui permet l'exécution de plusieurs variantes du système d'exploitation libre GNU/Linux. 

<img src="file:///C:/Users/ducrocq.frederic/Downloads/Les%20OS/raspberry.jpg" title="" alt="raspberry" data-align="center">

Dans le cadre de cette activité nous utiliserons le système d'exploitation `Raspbian` qui est basé sur une distribution `Debian` qui sert de base à d'autres distributions comme Linux Mint ou encore Ubuntu.

La distribution Raspbian fonctionnera ici dans un environnement virtuel appelé VirtualBox qui permettera de disposer d'un système d'exploitation GNU/Linux au sein d'une machine fonctionnant sous un système d'exploitation Microsoft Windows.

### Mise en route

> * Lancer l'application VirtualBox.
> 
> * Démarrer la machine virtuelle intitulée `Raspbian`.
> 
> * Lancer une session de `Terminal` en utilisant le raccourci `LXTerminal` présent sur le bureau.

Vous obtenez :

<img src="file:///C:/Users/ducrocq.frederic/Downloads/Les%20OS/lxterminal.png" title="" alt="" data-align="center">

### Trouver de l'aide

`man` une commande disponible sur les systèmes d'exploitation de type Unix, qui permet de visionner les contenus d'une documentation formatée.

> * Dans la fenêtre du terminal, entrer l'instruction `man ls` pour obtenir le rôle de l'instruction `ls`.
> 
> * Compléter l'espace ci-dessous afin d'indiquer le rôle de l'instruction `ls`.
> 
> ```bash
> # commande à saisir
> man ls
> # expliquer en quelques lignes le rôle de la commande ls
> "La commande ls permet ....."
> ```

### Les répertoires

Commençons par afficher le répertoire courant en utilisant la commande : `pwd` (print name of current/working directory).

> Saisir la commande permettant d'obtenir le répertoire courant et copier-coller le résultat obtenu.
> 
> ```bash
> # commande à saisir
> pwd
> # on obtient : 
> /root
> ```

Le contenu d'un répertoire peut être obtenu au moyen de la commande : `ls`  (list directory contents).

> Afficher le contenu de votre répertoire actuel
> 
> ```bash
> # commande à saisir
> ls
> # on obtient : 
> bench.py hello.c hello.js readme.txt
> ```

La commande `cd` (change directory) permet de changer de répertoire.

> Faire le nécessaire pour se placer dans le répertoire "Documents".
> 
> ```bash
> # commande à saisir
> cd Documents
> # on obtient :
> ```

Nous allons maintenant créer un nouveau répertoire en utilisant la commande `mkdir` (make directory) suivie du nom du répertoire à créer.

> * Créer un répertoire nommé "Rep1" dans le répertoire "Documents".
> 
> * Observez le résultat en utilisant la commande ls.
> 
> * Déplacez-vous ensuite dans le répertoire nouvellement créé.
> 
> * Afficher le répertoire courant
> 
> ```bash
> # création du répertoire "Rep1"
> mkdir Rep1
> # obervation du résultat
> 
> # se placer dans le répertoire créé
> cd Rep1
> # affichage du répertoire courant
> 
> # on obtient :
> ```
> 
> * Créer un nouveau répertoire "tim" dans le répertoire "Rep1".
> 
> * Se placer dans le répertoire "tim".
> 
> * Afficher alors le répertoire courant.
> 
> ```bash
> # création du répertoire "tim"
> mkdir tim
> # se placer dans le répertoire "tim"
> cd tim
> # affichage du répertoire courant
> pwd
> # on obtient :
> /root/Rep1/tim
> ```

### Les fichiers

#### création d'un fichier

La commande `touch` suivi d'un nom de fichier permet de créer un fichier (vide).

> * Créer un fichier vide nommé "oleon" dans le répertoire "tim".
> 
> * Vérifier sa création à l'aide de la commande `ls`.
> 
> ```bash
> # création du fichier vide "oleon" 
> touch oleon
> # vérification de sa création
> ls
> # on obtient :
> oleon
> ```
> 
> * Remonter dans l'arborescence .
> 
> * Vérifier que le répertoire courant a bien été modifié.
> 
> * Créer un répertoire "raymond" dans le répertoire "Rep1"
> 
> * Afficher la liste des fichiers/dossiers du "Rep1"
> 
> ```bash
> # pour remonter dans l'arborescence
> cd ..
> # pour afficher le répertoire courant
> pwd
> # pour créer le répertoire "Raymond"
> mkdir raymond
> # pour lister le contenu du répertoire "Rep1"
> ls
> # on obtient :
> raymond tim
> ```

#### Copier un fichier (ou un répertoire)

La commande `cp` (copy) permet de copier des fichiers ou des répertoires. Pour copier le fichier "oleon" dans le répertoire "Raymond" : 

```bash
# pour copier le fichier "oleon" dans le répertoire "Raymond"
cp tim/oleon raymond/
```

> Réaliser la copie du fichier "oleon" et vérifier la bonne réalisation.
> 
> ```bash
> # pour copier le fichier "oleon" dans le répertoire "Raymond"
> cp tim/oleon raymond/
> # pour vérifier la réalisation de la copie
> cd raymond
> ls
> # on obtient :
> oleon
> ```

#### Suppression d'un répertoire

La commande `rmdir` (remove directory) suivi du nom d'un répertoire permet de le supprimer.

> * Supprimer le répertoire "tim"
> 
> ```bash
> # pour supprimer le répertoire "tim"
> rmdir tim
> # on obtient :
> une erreur
> ```

Vous constatez que la commande produit une erreur car le répertoire n'est pas vide.

Il est possible de supprimer un répertoire non vide, mais pour l'instant allons effacer le fichier "oleon" qui n'est pas d'une grande utilité avec la commande `rm` .

> * Se placer dans le répertoire "tim"
> 
> * Effacer le fichier "oleon"
> 
> * Remonter dans l'arborescence pour se trouver dans le répertoire "Rep1"
> 
> * Effacer le répertoire "tim"
> 
> * Vérifier l'effacement du répertoire
> 
> ```bash
> # se placer dans le répertoire "tim"
> cd tim
> # effacer "oleon"
> rm oleon
> # remonter dans l'arborescence
> cd ..
> # effacer le répertoire "tim"
> rmdir tim
> # vérifier l'effacement
> ls
> # on obtient :
> raymond
> ```

#### Déplacer des fichiers

La commande `mv`(move) permet de déplacer des fichiers.

```bash
# pour déplacer le fichier "oleon" de "raymond" dans le répertoire courant "./"
mv raymond/oleon .
```

La même commande `mv` permet aussi de renommer un fichier.

```bash
# renommer le fichier "oleon" en "arthur"
mv oleon arthur
```

> * Déplacer le fichier "oleon" dans le répertoire courant.
> 
> * Renommer le fichier "oleon" en "arthur".
> 
> * Observer le contenu du répertoire "raymond".
> 
> * Supprimer le répertoire "raymond".
> 
> * Vérifier la bonne suppression.
> 
> ```bash
> # Déplacer le fichier "oleon" dans le répertoire courant
> mv oleon /
> # Renommer le fichier "oleon" en "arthur"
> mv oleon arthur
> # Observer le contenu du répertoire "raymond"
> ls
> # on obtient :
> 
> # Supprimer le répertoire "raymond"
> rmdir raymond
> # Vérification de la suppression
> ls
> # on obtient :
> ```

> * Saisir les commandes ci-dessous, puis commenter le résultat obtenu.
> 
> ```bash
> # commandes à saisir 
> cp arthur Arthur
> ls
> # commenter le résultat obtenu 
> 
> # on remarque que le système de fichier est sensible à la casse
> ```

#### Les fichiers cachés

> Saisir les commandes suivantes, puis noter vos observations
> 
> ```bash
> # commandes à saisir
> cp arthur .arthur
> ls
> # observations
> "Le contenu du ..."
> # commande à saisir
> ls .arthur
> # observations
> "Le fichier .arthur est ..."
> ```

**Remarque :** la convention adoptée et que tous les fichiers dont le nom commence par un point `.` sont traités comme des fichiers cachés. Pour visualiser tous les fichiers d'un répertoire (y compris les cachés), il faut taper les instructions suivantes :

```bash
ls -a
ls -al
```

> * Observez la différence entre les deux commandes ci-dessus.
> 
> * Testez aussi `ls` avec seulement l'option `-l`. 
> 
> ```bash
> # avec l'option -a, on obtient :
> 
> # avec l'option -al, on obtient :
> 
> # avec l'option -l, on obtient :
> ```

Observons que notre répertoire contienne :

* une entrée nommée `.` qui représente le répertoire courant.
* une entrée nommée `..` qui correspond au répertoire supérieur.

On retrouve ces deux entrées dans tous les répertoires.

#### Nettoyage du répertoire

Nettoyons maintenant notre répertoire :

```bash
rm arthur Arthur .arthur
```

* la commande `rm`  accepte plusieurs arguments
  
  ```bash
  cd ..
  ```

* Appeler votre enseignant avant la commande suivante, pour valider la séance !

```bash
rmdir Rep1
```

Tous les fichiers sont identifiables par leur nom et leur emplacement dans la hiérarchie.

On doit pour cela fournir la liste des répertoires qu’il faut traverser avant de parvenir dans le répertoire contenant le fichier.

On appelle cette information le chemin (path en anglais) du fichier.

Chaque répertoire d’un chemin est séparé du répertoire suivant par le caractère «/».

Il existe deux manières de donner un chemin :

- en spécifiant la liste la plus courte des répertoires à traverser *depuis la racine de la hiérarchie*, on dit alors que c’est un **chemin absolu** ;

- en spécifiant une liste des répertoires à traverser à partir d’un répertoire particulier de la hiérarchie, on dit dans ce cas que c’est un **chemin relatif** à ce répertoire de départ.

---

## Les droits d'accès

Les droits d'accès sont les ensembles d'autorisation qui déterminent qui peut avoir accès au fichier en vue de quelle utilisation.

> Placez-vous dans le répertoire `/home/pi` et entrer l'instruction suivante :
> 
> ```bash
> ls -al
> ```

Vous obtenez la liste de tous les fichiers et répertoires contenus dans `/home/pi`avec des informations détailles comme par exemple pour une ligne :

```bash
drwxr-xr-x 2 pi pi 4096 juin 6 16:11 Desktop
```

En lisant les informations de gauche à droite :

- d : directory (en effet Desktop est un répertoire)

- rwxr-xr-x : les différents droits d'accès (r pour lecture, w pour écriture, x pour exécutable et - pour aucun accès)

- 2 : le nombre de liens

- pi : le propriétaire du répertoire

- pi : le groupe d'appartenance du propriétaire (ici le propriétaire est le groupe portent le même nom)

- 4096 : la taille

- juin 6 16:11 : date et heure de création

- Desktop : le nom du fichier ou du répertoire

### Création d'un fichier

> Placez vous dans le répertoire `home/pi/Documents`et créer un document portant le nom `droits.txt`en utilisant l'éditeur de texte `nano`dans lequel vous taperez une ligne de texte.

En cas de difficulté avec `nano`, il existe de nombreux tutoriels sur internet.

### Visualisation des droits

> En utilisant la commande `ls -al`, donnez les informations détaillées concernant le fichier `droits.txt`
> 
> ```bash
> # commande à saisir
> ls -al
> # on obtient :
> ```

On constate que le fichier `droits.txt` est associé aux droits -rw-r--r-- 

### Les droits en fonction des utilisateurs

Les droits sont différents selon les utilisateurs, la première lettre indique le type si l'élément est un dossier (d) ou un lien (l) :

<img src="file:///C:/Users/ducrocq.frederic/Downloads/Les%20OS/droits_unix.png" title="" alt="droits_unix" data-align="center">

Suivent ensuite trois triplets de lettres montrant les droits pour l'utilisateur (le propriétaire), le groupe (les autres membres du groupe) et pour tous les autres utilisateurs de la machine.

Si on revient sur les droits associés au fichier `droits.txt`, on constate que :

- `droits.txt` est un fichier (pas de lettre 'd').

- le propriétaire `pi` peut lire (r) et écrire (w) sur ce fichier (il peut donc le supprimer).

- les membres du groupe `pi` et tous les autres utilisateurs ne pourront que lire (r) ce fichier.

Nous reviendrons sur ces droits et leurs modifications plus tard.

### Création d'un utilisateur

Pour créer un nouvel utilisateur sous Unix, il est nécéssaire d'avoir suffisament de droit sur la machine. Il existe pour cela un "super-utilisateur" appelé "root" qui a tous les droits sur le système.

On peut devenir temporairement "root" en ajoutant `sudo` (Substitute User DO) avant l'instruction que l'on souhaite exécuter.

Pour créer un utilisateur, on utilisera l'instruction `adduser`  suivie du nom du compte à créer.

> Créer un nouvel utilisateur en utilisant par exemple votre prénom
> 
> ```bash
> # commande à saisir
> 
> # on obtient :
> ```

**Remarque :** un compte peut être supprimé avec l'instruction `deluser`.

### Changer d'identité

Afin de tester les droits d'un autre utilisateur sur un fichier (ou répertoire), nous allons ouvrir un nouveau terminal et utiliser l'instruction `su`(substitute user ou switch user).

> Ouvrir un nouveau terminal (en laissant le précédant avec l'utilisateur `pi`ouvert) et prendre l'identité d'un autre utilisateur.
> 
> ```bash
> su utilisateur
> # le shell réclame le mot de passe du compte utilisateur
> ```

On va maintenant vérifier que l'on se trouve dans le répertoire `home/pi/Documents` et s'y déplacer si cela n'est pas le cas.

> Donnez l'instruction permettant de vérifier que l'on est dans le répertoire demandé (et les instructions permettant de s'y placer).
> 
> ```bash
> # pour vérifier le répertoire actuel
> 
> # on obtient :
> 
> # pour s'y rendre
> ```

On va maintenant ouvrir le fichier `droits.txt` avec l'éditeur nano, ajouter une ligne dans ce fichiers et enregistrer les modifications.

> Donnez les instructions nécessaires pour réaliser les actions demandées.
> 
> ```bash
> # pour éditer le fichier droits.txt avec nano
> 
> # que peut-on faire ?
> 
> # que ne peut-on pas faire ?
> ```

### Changement de propriétaire

Le changement de propriétaire se fait à l'aide de l'instruction `chown` (change owner), il faut pour cela en **tant que root**, donner le nom du nouveau propriétaire et le nom du fichier concerné :

```bash
sudo chown utilisateur droits.txt
```

> Modifiez le propriétaire du fichier droits.txt qui est actuellement pi avec le compte utilisateur.
> 
> Affichez les nouveaux droits sur le fichier
> 
> Tentez à nouveau d'ajouter une ligne, et enregistrer les modifications.
> 
> ```bash
> # commande à saisir pour modifier le propriétaire (le faire dans la fenêtre terminal de pi)
> 
> # commande pour vérifier le changement d'utilisateur
> 
> # on obtient :
> 
> # commande pour editer le fichier puis l'enregistrer
> ```

Remarque : dans l'exemple ci-dessus, on peut constater que le compte 'utilisateur' est bien devenu propriétaire du fichier 'droits.txt' mais ce fichier appartient toujours au groupe 'pi'.  De plus, si on veut modifier le propriétaire (et le groupe) de toutes les fichiers et sous-dossier, on utilisera l'option -R.

> ```bash
> # modification propriétaire + groupe
> sudo chown utilisateur:groupe droits.txt
> # modification propriétaire + groupe pour tout un dossier et ce qu'il contient
> sudo chown utilisateur:groupe /home/pi
> ```

### Les groupes

Un groupe est un ensemble d'utilisateurs qui partagent les mêmes fichers et répertoires, chaque utilisateur doit faire partie au moins d'un groupe.

Par défaut, à la création d'un utilisateur, un nouveau groupe portant son nom (groupe primaire) est créé.

>  Obtenir la liste des groupes et des comptes existants en utilisant les instructions `cat /etc/passwd` et `cat /etc/group`en tant que root.
> 
> La commande `cat`  (*concatenate files*) permet différentes fonctions dont la concaténation et l’affichage de contenu de fichiers.
> 
> Se déplacer dans le dossier `/home/` et obtenir la liste détaillée (avec les droits) du contenu de ce dossier.
> 
> Donnez le nom du propriétaire et le nom du groupe propriétaire de chacun des dossiers.
> 
> ```bash
> # commande pour obtenir la liste des utilisateurs, on remarque que chaque utilisateur à un identifiant gid
> 
> # commande pour obtenir la liste des groupes
> 
> # commande pour obtenir le contenu détaillé de /home/
> 
> # on obtient :
> 
> 
> 
> # le propriétaire du dossier pi est l'utilisateur pi, mais aussi le groupe pi même prinicipe pour les autres dossiers
> ```

On pourrait se contenter de ce fonctionnement un utilisateur = un groupe, mais on peut aussi créer d'autres groupes et affecter un utilisateur à plusieurs groupes (groupes secondaires).

Pour obtenir la liste de tous les groupes d'appartenance (groupes primaire et secondaires) d'un utilisateur, on utilise l'instruction `groups` suivie du nom de l'utilisateur.

> Donner la liste des groupes auquelle appartient l'utilisateur ''pi' et 'utilisateur'
> 
> ```bash
> # commande pour afficher les groupes auquels appartient l'utilisateur pi
> 
> # on obtient :
> 
> # commande pour obtenir les groupes du compte utilisateur
> 
> # on obtient :
> ```

Pour créer un nouveau groupe, on utilise l'instruction `addgroup` suivie du nom du groupe à créer.

> Créer un groupe nommé 'eleves'
> 
> ```bash
> # commande pour ajouter le groupe 'eleves', il faut être super utilisateur pour cela
> 
> # on obtient :
> ```

__Remarque__ : on peut supprimer un groupe avec l'instruction `delgroup`.

Pour changer de groupe un utilisateur, on utilise l'instruction `usermod -g` suivie du nom du groupe destinataire et du nom de l'utilisateur.

> Déplacer le compte 'utilisateur' dans le groupe 'eleves', ne pas hésiter à utiliser `man usermod` pour obtenir la documentation de `usermod`.
> 
> Vérifier que le compte 'utilisateur' appartient désormais au groupe 'eleves'.
> 
> ```bash
> # commande pour modifier le groupe pour le compte utilisateur
> 
> # commande pour vérifier le changement
> ```

Il est aussi possible de faire en sorte qu'un utilisateur appartienne à plusieurs groupes. Pour cela, il faut utiliser le paramètre `usermod -G` et séparer les noms des groupes par une virgule, sans espace entre chaque nom de groupe.

> Faire le nécessaire pour que le compte utilisateur soit membre du groupe 'eleves' et 'pi'.
> 
> ```bash
> # modification du compte utilisateur pour qu'il soit membre de deux groupes
> 
> # verification du changement
> ```

### Modification des droits

Chaque fichier et répertoire posséde une liste de droits d'accès (r, w, x), voir le paragraphe sur les droits en fonction des utilisateurs.

Nous allons maintenant donner les droits nécessaires à un utilisateur pour modifier un fichier.

#### En utilisant les chiffres (CHMOD absolu)

Chaque droit est associé à un chiffre :

| Droit | Chiffre |
|:-----:|:-------:|
| r     | 4       |
| w     | 2       |
| x     | 1       |

Si on veut combiner ces droits, il faudra additionner ces valeurs. Par exemple, pour donner des droits de lecture et d'écriture (rw-) cela sera coder par 4 + 2 = 6.

> Compléter le tableau ci-dessous
> 
> | Droits | Calcul    | Chiffre |
> |:------:|:---------:|:-------:|
> | ---    |           |         |
> | r--    |           |         |
> | -w-    |           |         |
> | --x    |           |         |
> | rw-    | 4 + 2 + 0 | 6       |
> | -wx    |           |         |
> | r-x    |           |         |
> | rwx    |           |         |

Les droits sont attribués au propriétaire, au groupe, et aux autres.

Ainsi '640' indique que les droits sont :

* 6 pour le propriétaire soit rw-

* 4 pour le groupe soit r--

* 0 pour les autres soit --- (aucun droit)

Les droits attibués vont donc de 000 (rien) à 777 (tous les droits).

L'opération de modification des droits se réalise avec l'instruction `chmod`. Pour besoin d'être 'root' pour modifier les droits sur un fichier (ou un répertoire), il suffit d'en être propriétaire.

```bash
# faire que seul le propriétaire puisse lire et écrire le fichier 'droits.txt'
chmod 600 droits.txt
```

> * Modifier les droits sur le fichier droits.txt pour que le propriétaire, le groupe et les tous les autres utilisateurs puissent le lire et le modifier.
> 
> * A l'aide de la commande `ls`, vérifier et afficher ces droits.
> 
> ```bash
> # commande pour affecter les droits de lecture et d'écriture au propriétaire, au groupe et aux autres
> 
> # commande pour vérifier
> ```

#### En utilisant les lettres (CHMOD relatif)

Il existe un autre moyen de modifier les droits d'un fichier, il faut pour cela savoir que :

- **u**  = user (propriétaire) ;

- **g**  = group (groupe) ;

- **o**  = other (autres).

… et que :

- **+**  signifie : « Ajouter le droit » ;

- **-**  signifie : « Supprimer le droit » ;

- **=**  signifie : « Affecter le droit ».

On peut alors écrire par exemple :

```bash
# pour ajouter le droit d'écriture au groupe
chmod g+w droits.txt
# pour enlever le droit de lecture aux autres
chmod o-r droits.txt
# pour ajouter les droits de lecture et d'exécution au propriétaire
chmod u+rx droits.txt
# pour ajouter tous les droits au propriétaire, la lecture au groupe et rien aux autres
chmod u+rwx,g=r,o=- droits.txt
```

**Remarque :** le paramètre  `-R`  de `chmod`  appliqué à un répertoire permet d'avoir tous les fichiers et sous-dossiers avec les mêmes droits.

> Faire le nécessaire pour que seul le propriétaire `pi` puisse lire et écrire le fichiers `droits.txt` en utilisant `CHMOD` relatif.
> 
> ```bash
> # commande pour attribuer les droits demandés sur le fichier droits.txt
> 
> # commande pour vérifier
> ```

---

## Les variables d'environnement

Les variables d'environnement système sont des variables dynamiques utilisées par les différents processus d'un système d'exploitation (Windows, Unix, ...). Elles servent à communiquer des informations entre programmes, nous allons découvrir les plus utilisées sous GNU/Linux.

Taper les instructions suivantes et noter le résultat juste en dessous.

```bash
echo $HOME
```

>  /home/pi

```bash
printenv
```

>  On obtient la liste des variables d'environnement du système d'exploitation.  

A partir de la liste obtenue précedemment, et en utilisant l'instruction `echo`, afficher :

- Le nom de votre répertoire personnel et le nom de la variable associée
  
  > ```bash
  > echo $HOME
  > répertoire personnel : /home/pi
  > variable d'environnement associée : $HOME
  > ```

- Le nom du répertoire courant et le nom de la variable associée
  
  > ```bash
  > echo $PWD
  > répertoire courant : /home/pi
  > variable d'environnement associée : $PWD
  > ```

- Le nom du shell que vous utilisez
  
  > ```bash
  > echo $SHELL
  > Shell utilisé () : /bin/bash 
  > BASH ()Bourne again shell) : créé par Brian Fox en 1987
  > variable d'environnement associée : $SHELL
  > ```
