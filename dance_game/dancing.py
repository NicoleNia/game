WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH/2
CENTER_Y = HEIGHT/2

move_list = []
display_list = []

score = 0
current_move = 0
count = 4
dance_lenght = 4

say_dance = False
show_countdown = True
moves_complete = False
game_over = False

dancer = actor ("daneu.png")
dancer.pos = CENTER_x + 20, CENTER_Y - 40

up = Actor("danceu.png")
up.pos = CENTER_x, CENTER_Y + 100
right = Actor("dancer.png")
right.pos = CENTER_X + 60, CENTER_Y +170
down = Actor("dancerd.png")
down.pos = CENTER_X, CENTER_Y +230
left = Actor("dancel.png")
left.pos = CENTER_X - 60, CENTER_Y + 170
