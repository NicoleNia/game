dino = Actor('character')
dino.pos = 100, 150
WIDTH = 500
HEIGHT = 300

def draw():
    screen.fill((30,25,108))
    dino.draw()

def update():
    dino.left = dino.left + 2
    if dino.left > WIDTH:
        dino.right = 0

def on_mouse_down(pos, button):
    if button == mouse.LEFT and dino.collidepoint(pos):
        print("Ouch!")
        sounds.eep.play()
        set_dino_hurt()
    else:
        print("You missed!")


def set_dino_hurt():
    dino.image = 'clicked'
    clock.schedule_unique(set_dino_normal, 1.0)

def set_dino_normal():
    dino.image = 'character'
