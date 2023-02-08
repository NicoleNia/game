star = Actor('character')
star.pos = 100, 150
WIDTH = 500
HEIGHT = 300

def draw():
    screen.fill((30,25,108))
    star.draw()

def update():
    star.left = star.left + 2
    if star.left > WIDTH:
        star.right = 0

