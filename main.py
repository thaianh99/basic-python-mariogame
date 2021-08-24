import pgzrun
from random import randint


#Khai bao bien
HEIGHT = 564
WIDTH = 564
score = 0
game_over = False
mario = Actor('mario.png')
coin = Actor('coin.png')
mario.pos = 100, 200
coin.pos = 300, 300
music.play('nhac.ogg')

def draw():
    screen.blit('background.jpg',(0,0))
    mario.draw()
    coin.draw()
    screen.draw.text('Score: ' + str(score), color='black', topleft=(10,10))
    if game_over:
        screen.blit('background.jpg',(0,0))
        screen.draw.text('YOUR SCORE: ' + str(score), color='black', fontsize=70, midleft=(30,230))

def coin_position():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def update():
    global score
    if keyboard.left:
        mario.x = mario.x - 4
    elif keyboard.right:
        mario.x = mario.x + 4
    elif keyboard.up:
        mario.y = mario.y - 4
    elif keyboard.down:
        mario.y = mario.y + 4
    coin_collected = mario.colliderect(coin)
    if coin_collected:
        score += 10
        sounds.epp.play()
        coin_position()
        
def time_up():
    global game_over
    game_over = True
    music.stop()

clock.schedule(time_up, 20.0)
coin_position()
pgzrun.go()