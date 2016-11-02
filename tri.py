# -*- coding: utf8 -*-

"""
Comparaison des performances de divers algorithmes de tri écrit en Python
"""

import sys, os
sys.path.append(os.getcwd())
sys.setrecursionlimit(10005)

from main.compteur import Compteur
from random import randint


def tri_selection(t, n):
    """
    Tri par sélection

    On détermine la position du plus petit élément, on le met en première
    position et on itère le procédé sur le tableau restant.

    Complexité en 0(n2) dans tous les cas.

    :param t: tableau à trier
    :param n: taille du tableau
    :return: tableau trié
    """
    if n < 2:
        # Moins de 2 éléments : pas besoin de trier
        return t
    for i in range(n-1):
        # On suppose que le min est en premier
        min = t[i]
        imin = i
        # j = i+1
        # while j < n:
        #     if t[j] < min:
        #         # On met à jour le min
        #         min = t[j]
        #         imin = j
        #     j += 1
        for j in range(i+1, n):
            if t[j] < min:
                # On met à jour le min
                min = t[j]
                imin = j
        if imin != i:
            # On pertmute pour mettre le min en premier
            t[imin] = t[i]
            t[i] = min
    return t



def tri_recursif(t, n):
    """
    Tri par sélection récursif

    On détermine la position du plus grand élément et on le met en dernière
    position. On réappelle alors la fonction tri_recursif sur le sous tableau
    composé des n-1 premiers éléments de t.

    Complexité en O(n**2) dans tous les cas.

    :param t:
    :param n:
    :return:
    """
    if n < 2:
        # Moins de 2 éléments : pas besoin de trier
        return t
    # On suppose que le max est en dernier
    max = t[n-1]
    imax = n-1
    for i in range(n-2):
        if t[i] > max:
            # On met à jour le max
            max = t[i]
            imax = i
    if imax != n-1:
        # On permute pour mettre le max en dernier
        t[imax] = t[n-1]
        t[n-1] = max
    # Appel de tri_recursif sur t de taille n-1 pour trier le reste du tableau
    t = tri_recursif(t, n-1)
    return t



def tri_insertion(t, n):
    """
    Tri par insertion

    On ordonne les deux premiers éléments.
    On insère le 3ème de manière à ce que les 3 soient ordonnés.
    On insère le i-ème de manière à ce que les i éléments soient ordonnées.

    La complèxité est en O(n**2) dans le pire des cas.

    :param t:
    :param n:
    :return:
    """
    if n < 2:
        # Moins de 2 éléments : pas besoin de trier
        return t
    for i in range(2, n):
        temp = t[i]
        j = i - 1
        while t[j] > t[i] and j >= 0:
            t[j+1] = t[j]
            j -= 1
        t[j] = temp
    return t



def tri_fusion(t, n):
    """
    Tri fusion

    On découpe le tableau à trier en deux sous-tableaux de taille n/2.
    On trie alors les deux sous-tableaux récursivement, ou on ne fait rien
    s'ils sont de taille 1.
    On reconstitue le tableau trié initial en fusionnant les deux sous-tableaux
    triés.

    La complexité est en O(n*log(n)) dans le pire des cas.

    :param t:
    :param n:
    :return:
    """
    def vidage(ta, pa, na, t, p):
        """
        Copie ta de taille na à partir de la position pa dans t à partir de p
        :param ta: tableau à copier
        :param pa: position à partir de laquelle copier
        :param na: taille de ta
        :param t: tableau de destination
        :param p: position à partir de laquelle coller
        :return:
        """
        for i in range(pa, na):
            t[p] = ta[i]
            p += 1
        return t


    if n < 2:
        # Moins de 2 éléments : pas besoin de trier
        return t


    # Cas général : on découpe le tableau en 2 partie que l'on trie
    p = n // 2
    t1 = t[:p]
    n1 = len(t1)
    t1 = tri_fusion(t1, n1)
    t2 = t[p:]
    n2 = len(t2)
    t2 = tri_fusion(t2, n2)
    # Fusion des deux parties
    p1, p2, p = 0, 0, 0 # position dans t1, t2 et t
    while p1 < n1 and p2 < n2:
        if t1[p1] < t2[p2]:
            # On met t1[p1] dans t
            t[p] = t1[p1]
            p1 += 1
        else:
            # On met t2[p2] dans t
            t[p] = t2[p2]
            p2 += 1
        p += 1
    if p1 == len(t1):
        vidage(t2, p2, len(t2), t, p)
    else:
        vidage(t1, p1, len(t1), t, p)
    return t



def tri_bulle(t, n):
    """
    Tri bulle

    On compare les couples d'éléments successifs pour placer systématiquement
    le plus grand après le plus petit. Un parcours complet du tableau selon
    ce processus nous assure que le plus grand élément est en dernière
    position. On réitère alors le processus sur le sous tableau restant.

    Complexité en O(n**2).

    :param t:
    :param n:
    :return:
    """
    if n < 2:
        # Moins de 2 éléments : pas besoin de trier
        return t
    for i in range(n-1):
        for j in range(n-1-i):
            if t[j] > t[j+1]:
                # On permute
                temp = t[j]
                t[j] = t[j+1]
                t[j+1] = temp
    return t





def tri_rapide(t, n):
    """
    Tri rapide

    On choisit un élément du tableau au hasard qui sera 'pivot' et on permute
    tous les éléments de manière à placer à gauche du pivot les éléments qui
    lui sont inférieurs, et à droite ceux qui lui sont supérieurs.
    On trie alors de la meme manière les deux moitiés de part et d'autre du
    pivot.

    Complexité en O(nlog(n)).

    :param t:
    :param n:
    :return:
    """
    def tri_rapide(t, i, j):
        if i >= j:
            # Pas besoin de trier
            return t
        p = i
        # On place les éléments plus petits que le pivot (t[j-1]) au début
        for k in range(i, j-1):
            if t[k] <= t[j-1]:
                t[k], t[p] = t[p], t[k]
                p += 1
        # On remet le pivot après les éléments plus petits
        t[j-1], t[p] = t[p], t[j-1]
        # On trie les deux parties
        tri_rapide(t, i, p-1)
        tri_rapide(t, p+1, j-1)
        return t


    if n < 2:
        # Moins de 2 éléments : pas besoin de trier
        return t

    t = tri_rapide(t, 0, n)
    return t



if __name__ == '__main__':
    t = [randint(0, 1000) for i in range(100)]

    with Compteur("Tri par sélection"):
        t2 = tri_selection(t, len(t))

    with Compteur("Tri par sélection récursif"):
        t3 = tri_recursif(t, len(t))

    with Compteur("Tri par insertion"):
        t4 = tri_insertion(t, len(t))

    with Compteur("Tri fusion"):
        t5 = tri_fusion(t, len(t))

    with Compteur("Tri bulle"):
        t6 = tri_bulle(t, len(t))

    with Compteur("Tri rapide"):
        t7 = tri_rapide(t, len(t))
        print(t7)


    t = [2, 5, 1, 2, 3, 5]
    print(tri_insertion(t, len(t)))