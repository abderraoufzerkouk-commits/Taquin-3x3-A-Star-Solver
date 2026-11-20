import heapq
from itertools import count

from Puzzle import Puzzle


class Node:
    """Représente un état et son parent dans la recherche."""

    def __init__(self, state, parent=None):
        self.state = tuple(state)
        self.parent = parent

    @property
    def path(self):
        chemin = []
        node = self
        while node is not None:
            chemin.append(node.state)
            node = node.parent
        return list(reversed(chemin))


class Solver:
    """Algorithme A* utilisant la distance de Manhattan."""

    def __init__(self):
        self.etats_explores = 0

    @staticmethod
    def heuristique(etat):
        distance = 0
        positions_but = {
            valeur: position
            for position, valeur in enumerate(Puzzle.ETAT_FINAL)
        }
        for position, valeur in enumerate(etat):
            if valeur == 0:
                continue
            cible = positions_but[valeur]
            ligne, colonne = divmod(position, 3)
            ligne_cible, colonne_cible = divmod(cible, 3)
            distance += abs(ligne - ligne_cible) + abs(colonne - colonne_cible)
        return distance

    def solve(self, etat_initial):
        etat_initial = tuple(etat_initial)
        but = Puzzle.ETAT_FINAL
        self.etats_explores = 0

        if not Puzzle.est_resoluble(etat_initial, but):
            return None

        if etat_initial == but:
            return [etat_initial]

        compteur = count()
        file_priorite = [
            (self.heuristique(etat_initial), next(compteur), 0, etat_initial)
        ]
        meilleur_g = {etat_initial: 0}
        parents = {}

        while file_priorite:
            f, _, g, etat = heapq.heappop(file_priorite)

            if g != meilleur_g.get(etat):
                continue

            self.etats_explores += 1

            if etat == but:
                chemin = [etat]
                while etat in parents:
                    etat = parents[etat]
                    chemin.append(etat)
                chemin.reverse()
                return chemin

            for voisin in Puzzle.voisins(etat):
                nouveau_g = g + 1
                if nouveau_g < meilleur_g.get(voisin, float("inf")):
                    meilleur_g[voisin] = nouveau_g
                    parents[voisin] = etat
                    nouveau_f = nouveau_g + self.heuristique(voisin)
                    heapq.heappush(
                        file_priorite,
                        (nouveau_f, next(compteur), nouveau_g, voisin)
                    )

        return None
