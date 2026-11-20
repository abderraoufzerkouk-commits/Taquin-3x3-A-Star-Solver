import random


class Puzzle:
    """Modèle du Taquin 3x3. L'utilisateur construit l'état initial."""

    TAILLE = 3
    ETAT_FINAL = (1, 2, 3, 8, 0, 4, 7, 6, 5)

    def __init__(self, board=None):
        if board is None:
            board = self.ETAT_FINAL
        self.board = tuple(board)
        self._verifier_board(self.board)

    @staticmethod
    def _verifier_board(board):
        if len(board) != 9 or set(board) != set(range(9)):
            raise ValueError("Le plateau doit contenir les nombres 1 à 8 et une case vide (0).")

    @property
    def solved(self):
        return self.board == self.ETAT_FINAL

    @property
    def actions(self):
        return self.voisins(self.board)

    @staticmethod
    def voisins(etat):
        zero = etat.index(0)
        ligne, colonne = divmod(zero, 3)
        positions = []

        if ligne > 0:
            positions.append(zero - 3)
        if ligne < 2:
            positions.append(zero + 3)
        if colonne > 0:
            positions.append(zero - 1)
        if colonne < 2:
            positions.append(zero + 1)

        resultat = []
        for pos in positions:
            nouveau = list(etat)
            nouveau[zero], nouveau[pos] = nouveau[pos], nouveau[zero]
            resultat.append(tuple(nouveau))
        return resultat

    def move_tile(self, position):
        zero = self.board.index(0)
        ligne0, colonne0 = divmod(zero, 3)
        ligne, colonne = divmod(position, 3)

        if abs(ligne - ligne0) + abs(colonne - colonne0) != 1:
            return False

        nouveau = list(self.board)
        nouveau[zero], nouveau[position] = nouveau[position], nouveau[zero]
        self.board = tuple(nouveau)
        return True

    def shuffle(self, nombre_coups=30):
        """Mélange en effectuant des coups légaux depuis le but."""
        etat = self.ETAT_FINAL
        precedent = None

        for _ in range(nombre_coups):
            candidats = self.voisins(etat)
            if precedent is not None and len(candidats) > 1:
                sans_retour = [e for e in candidats if e != precedent]
                if sans_retour:
                    candidats = sans_retour
            suivant = random.choice(candidats)
            precedent, etat = etat, suivant

        self.board = etat

    @staticmethod
    def est_resoluble(etat, but=None):
        """Vérifie la résolubilité par rapport à l'état final choisi."""
        if but is None:
            but = Puzzle.ETAT_FINAL

        # Le rang de chaque tuile est défini par sa position dans le but.
        ordre_but = {valeur: rang for rang, valeur in enumerate(but) if valeur != 0}
        valeurs = [ordre_but[x] for x in etat if x != 0]
        inversions = sum(
            1 for i in range(len(valeurs))
            for j in range(i + 1, len(valeurs))
            if valeurs[i] > valeurs[j]
        )
        return inversions % 2 == 0

    def pprint(self):
        for i in range(3):
            print(self.board[i * 3:i * 3 + 3])
