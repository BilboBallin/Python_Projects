import pygame as pg

def sz2xy(sz):
    return sz[0]*FELD, sz[1]*FELD


def zeichneBrett(BRETT):
    for sz, feld in BRETT.items():
        color = '#DFBF93' if feld else '#C5844E'
        pg.draw.rect(screen, color, (*sz2xy(sz), FELD, FELD))

def fen2position(fen):
    position, s, z = {}, 0, 0
    figurenstellung, zugrecht, rochade, enpassant, zug50, zugnr = fen.split()
    for char in figurenstellung:
        if char.isalpha():
            position[(s, z)] = char
            s += 1
        elif char.isnumeric():
            s += int(char)
        else:
            s, z = 0, z+1
    return position, zugrecht 


pg.init()
BREITE, HOHE = 800, 800
FELD = BREITE // 8
FPS = 60
screen = pg.display.set_mode((BREITE, HOHE))
BRETT = {(s, z): s % 2 == z % 2 for s in range(8) for z in range(8)}
fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
position, zugrecht = fen2position(fen)
print(BRETT)
print(position)

weitermachen = True
clock = pg.time.Clock()





while weitermachen:
    clock.tick(FPS)
    for ereignis in pg.event.get():
        if ereignis.type == pg.QUIT:
            weitermachen = False
    
    screen.fill((0, 0, 0))
    zeichneBrett(BRETT)
    pg.display.flip()

pg.quit()

