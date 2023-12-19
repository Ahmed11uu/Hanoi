from collections import deque

class HanoiGame:
    def __init__(self, numberdisks):
        #Initialisatiion du jeu avec un nombre de disque 
        #La première tour doit contenir tous les disques par ordre décroissant: du plus grand au plus petit
        self.numberdisks = numberdisks
        self.towers = [[i for i in range(numberdisks, 0, -1)],[],[]]
        #La fonction range(nimberdisks, 0, -1) créé une séquence décroissante du disque (3,2 1) si numberdisks=3

    def move(self, fromtower, totower):
        #Déplacer le disque du haut de fromtower vers totowzer
        disk=self.towers[fromtower].pop()
        self.towers[totowers].append(disk)

    def get_neighbors(self, state):
        #Donner tous les mouvements possibles à partir de l'état donné à un momment donné
        neighbors = []
        for i in range(3):
            for j in range (3):
                if i != j and state[i]:
                    #Créer un nouvel état, une nouvelle situation pour chaque mouvement valide
                    new_state = [tower.copy() for tower in state]
                    new_state[i].pop()
                    new_state[j].append((new_state, i, j))
        return neighbors
    
    def finalstate(self, state):
        #Vérifier si tous les disques sont dans la troisième tour et dans le bon ordre
        return state[2]==[i for i in range(self.numberdisks, 0, -1)]
    
    def solve(self):
        #Utiliser le recherche en largeur pour trouver une solution
        queue = deque([([tower.copy() for tower in self.towers], -1, -1)])
        visited=set()
        parents = {tuple(map(tuple, self.towers)):(None, None, None)}
        while queue:
            #Extraire l'état actuel de la file
            currentstate, fromtower, totower = queue.popleft()
            #Vérifiee si l'état actuel est l'état final
            if self.finalstate(currentstate):
                #construire et retourner le chemin de la solution trouvée
                return self.reconstruct_path(parents, currentstate)
            #Explore tous les voisins de l'état actuel
            for neighbor, src, dest in self.get_neighbors(currentstate);
                neighbor_tuple = tuple(map(tuple, neighbor))
                if neighbor_tuple not in visited:
                    #Ajouter l'état voisin à la liste des visités et à al file
                    visited.add(neighbor_tuple)
                    parents[neighbor_tuple] = (currentstate, src, dest)
                    queue.append((naighbor, src, dest))

    def reconstruct_path(self, parents, state):
        #Reconstruire le chemoin de la soltuon à partir de l'état final
        path = []
        while state:
            state, fromtower, totower = parents[tuple(map(tuple, state))]
            if fromtower is not None:
                #Ajouter le mouvement au chemin
                path.append((fromtower, totower))
            #Retourner le chemin inversé: de la racine à l'état final
            return path[::-1]
        
    
    #Exemple d'utlisation du programme
    HanoiGame = HanoiGame(3)
    solution = HanoiGame.solev()
    for move in solution:
        print(f"move disk from tower {move[0]} to tower {move[1]}")

