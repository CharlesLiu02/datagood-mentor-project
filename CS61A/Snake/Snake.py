import pygame
pygame.init()
game_over = False
screen = pygame.display.set_mode((800,600))

class Cube:
    def __init__(self, start, dirx=1, diry=0,)

class Snake(Cube):
    body = []
    turns = {}
    def __init__(self, color= (255,255,255), position):
        self.color = color
        self.head = Cube(position)
        self.body.append(self.head)
        self.dirx = 1
        self.diry = 0
    def move(self):
         for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        for i, c in enumerate(self.body):
        p = c.pos[:]
        if p in self.turns:
            turn = self.turns[p]
            c.move(turn[0],turn[1])
            if i == len(self.body)-1:
                self.turns.pop(p)
        else:
            if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
            elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])
            elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
            elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
            else: c.move(c.dirnx,c.dirny)

def drawGrid(w, rows, surface):
    size = w//rows
    x, y = 0 , 0
    for l in range(rows):
        x += size
        y += size
        pygame.draw.line(surface, (255,255,255), (x,0), (x,w))
        pygame.draw.line(surface, (255,255,255), (0,y), (w,y))
def redrawWindow(surface):
    global rows, width, length
    surface.fill((0,0,0))
    drawGrid(width,rows,surface)
    pygame.display.update()

def main():
    global rows, width, length
    width = 800
    rows = 40
    length = 600

    win = pygame.display.set_mode((width,length))
    #s = Snake((255,0,0)(10,10))
    clock = pygame.time.Clock()
    while not game_over:
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(win)
    pass
main()
