import time

class Compteur(object):
    def __init__(self, nom):
        self.nom = nom
    def __enter__(self):
        self.t_debut = time.time()
    def __exit__(self, exc_ty, exc_val, exc_tb):
        t_fin = time.time()
        print('{}: {}'.format(self.nom, t_fin - self.t_debut))



if __name__ == "__main__":
    n = 10000000
    with Compteur('Boucle for'):
        for i in range(n):
            pass
    with Compteur('Boucle while'):
        while n > 0:
            n -= 1



