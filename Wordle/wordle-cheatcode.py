"""
    Wordle-Cheatcode : Extraire tous les mots du dictionnaire français et les filter
"""


def get_liste_mots_fr(chemin_fichier: str) -> list[str]:
    """
        Cette fonction extrait les mots contenus dans le fichier dont le path est spécifié en paramètre,
        les stocke dans une liste et renvoie ladite liste.

        :param chemin_fichier: chemin (absolu ou relatif) du fichier à lire.
        :return: une liste contenant chaque ligne du fichier lu.
    """
    with open(chemin_fichier, "r", encoding="utf8") as fichier:     # ouverture du fichier en mode read-only
        motsfr = fichier.readlines()        # Liste qui va contenir les mots du dico français

    return motsfr
# Fin de getListeMotsFr


def liste_mots_length5(liste_mots: list[str]) -> list[str]:
    """
        Cette fonction filtre la liste de mots passé en paramètre ; conserve, stocke et renvoie
        uniquement les mots de longueur 5 dans une nouvelle liste.

        :param liste_mots: liste de mots ayant des longueurs quelconques.
        :return: une nouvelle liste contenant des mots de longueurs 5.
    """
    mots_length5 = []
    for mot in liste_mots:
        if len(mot.strip()) == 5:
            mots_length5.append(mot.upper().strip())

    return mots_length5
# Fin de liste_mots_length5


def tri_lettre_index_exact(liste_mots: list[str], liste_charat: list[tuple]) -> list[str]:
    """
        Cette fonction filtre la liste de mots initiale passé en paramètre dépendamment de la liste de
        tuple qui lui est passé en paramètre. Elle s'utilise lorsqu'on connait la postion exact de n
        caractères du mot à deviner.\r

        Exemple : Si liste_charat = [('I', 3), ('N', 4)] alors la fonction renverra tous les mots issus
        de liste_mots qui contiennent I à l'index 3 et N à l'index 4.


        :param liste_mots: La liste de mots initiale à filtrer
        :param liste_charat: La liste de tuple ('Caractère','Index du caractère') qui sert de filtre.
        :return: Une nouvelle liste contenant uniquement les mots qui contiennent tous les caractères spécifiés
        dans la liste tuple, aux index attribués.
    """

    mots_potentiel = []                 # Liste des mots potentiel

    for mot in liste_mots:              # Pour chaque mot de la liste de mots initiale
        for paire in liste_charat:         # Pour chaque paire de (char,index)
            if mot[paire[1]] == paire[0]:     # Vérifie que par exemple mot[4] == 'N'
                if liste_charat.index(paire) == len(liste_charat)-1:      # Si on atteint la fin de la liste de paire
                    mots_potentiel.append(mot)
            else:
                break

    return mots_potentiel
# Fin de la fonction tri_lettre_index_exact


def tri_lettre_index_inexact(liste_mots: list[str], liste_char: list[str]) -> list[str]:
    """
        Cette fonction filtre la liste de mots initiale passé en paramètre dépendamment de la liste de
        caractère qui lui est passé en paramètre. Elle s'utilise lorsqu'on connait n >= 1 caractères du mot
        du mot à deviner mais qu'on ignore leurs index exact.

        Exemple : Si liste_char = ['I','N'] alors la fonction renverra tous les mots issus
        de liste_mots qui contiennent I et N.


        :param liste_mots: La liste de mots initiale à filtrer
        :param liste_char: La liste des caractères dont on ne connait pas l'index exact.
        :return: Une nouvelle liste contenant uniquement les mots qui contiennent tous les caractères spécifiés.
    """

    mots_potentiel = []
    count = 0
    for mot in liste_mots:
        for char in liste_char:
            if mot.__contains__(char):
                count += 1
                if count == len(liste_char):  # Si on atteint la fin de la liste de char
                    mots_potentiel.append(mot)
            else:
                break
        count = 0       # Réinitialiser le compteur pour le prochain mot

    return mots_potentiel
# Fin de la fonction tri_lettre_index_inexact


def tri_lettre_inexact(liste_mots: list[str], liste_char: list[str]) -> list[str]:
    """
        Cette fonction filtre la liste de mots initiale passé en paramètre dépendamment de la liste de
        caractère qui lui est passé en paramètre. Elle s'utilise lorsqu'on connait n >= 1 caractères qui ne
        font pas parti du mot à deviner.

        Exemple : Si liste_char = ['I','N'] alors la fonction renverra tous les mots issus
        de liste_mots qui ne contiennent ni I ni N.


        :param liste_mots: La liste de mots initiale à filtrer
        :param liste_char: La liste des caractères qui n'appartiennent pas au mot.
        :return: Une nouvelle liste contenant uniquement les mots qui ne contiennent pas les caractères spécifiés.
    """

    mots_potentiel = []
    count = 0
    for mot in liste_mots:
        for char in liste_char:
            count += 1
            if mot.__contains__(char):
                break
            else:
                if count == len(liste_char):
                    mots_potentiel.append(mot)
        count = 0
    return mots_potentiel
# Fin de la fonction tri_lettre_inexact


def main():

    # 0. Obtenir la liste de tous les mots français
    dico = get_liste_mots_fr("./dictionnaire/ListeMotsFr.txt")
    print("Nombre total de mots : ", len(dico))

    # 1. Faire un premier tri et conserver uniquement les mots qui ont une longueur de 5
    dico_mots5 = liste_mots_length5(dico)
    print("Nombre total de mots de taille 5 : ", len(dico_mots5))

    # 2. Faire des extractions dépendamment des filtres
    """
        # Cas d'utilisation où on connais les lettres et leurs index : Utiliser la fonction 'tri_lettre_index_exact'
        words = [('I', 3), ('N', 4)]
        wordlist00 = tri_lettre_index_exact(dico_mots5, words)
        print("Nombre total de mots potentiel (tri 1): ", len(wordlist00))
    
        # Cas d'utilisation où on ne connais que les lettres : Utiliser la fonction 'tri_lettre_index_inexact'
        chars = ['E']
        wordlist00 = tri_lettre_index_inexact(dico_mots5, chars)
        print("Nombre total de mots potentiel (tri 2): ", len(wordlist00), "\n", wordlist00)
        
        # Cas d'utilisation où on ne connais que les lettres qui ne sont pas dans le mot : fonction 'tri_lettre_inexact'
        chars = ['E']
        wordlist01 = tri_lettre_inexact(dico_mots5, chars)
        print("Nombre total de mots potentiel (tri 2): ", len(wordlist01), "\n", wordlist01)
    """
# Fin du main


main()
