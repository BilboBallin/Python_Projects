_M_HV = [(0, 1), (0, -1), (-1, 0), (1, 0)]      #horinzontale mögliche Moves
_M_DI = [(-1, -1), (1, -1), (-1, 1), (1, 1)]    #vertikale mögliche Moves
_M_NT = [(-2, 1), (-2, -1), (-1, 2), (-1, -2),  #Springer Moves
         (1, 2), (1, -2), (2, 1), (2, -1)]

_MOVES = {'r':[7, *_M_HV],                  #Moves Dictionary
          'b':[7, *_M_DI],
          'k':[1, *_M_HV, *_M_DI],
          'q':[1, *_M_HV, *_M_DI],
          'n':[1, *_M_NT]}

BRETT = {(s, z): s % 2 == z % 2 for s in range(8) for z in range(8)}

def zugGen(weiss, position):
    zuge = []
    pseudo = _pseudoZG(weiss, position)
    #return zuge
    return pseudo

def _pseudoZG(weiss, position):
    pseudo = []
    for von, fig in position.items():
        if fig.isupper() != weiss: continue
        if fig in 'pP': 
            #Platzhalter für Bauern
            continue
        f = fig.lower()
        richtungen = _MOVES[f][1:] # 1: bedeutet: ab Indexpos 1 aufwärts!
        multiplikator = _MOVES[f][0]
        for ds, dz in richtungen:
            for m in range(1, multiplikator+1):
                zu = von[0] + ds * m, von[1] + dz * m
                if zu not in BRETT: break
                if zu in position and position[zu].isupper == weiss: break
                if zu in position and position[zu].isupper != weiss:
                    pseudo.append((fig, von, zu, position[zu]))
                    break #schaue nicht mehr in diese Richtung weiter
                else:
                    pseudo.append((fig, von, zu, False))
    return pseudo
