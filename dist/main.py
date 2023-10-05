from pygame import *
from time import time as  timer
from random import randint

mixer.init()
mixer.music.load('musica.mp3')
mixer.music.set_volume(0.15)
mixer.music.play()



win_width =  1000
win_height = 1000
display.set_caption("one day...")
win = display.set_mode((win_width, win_height))
background = transform.scale(image.load("room.jpg"), (win_width, win_height))

font.init()
font1 = font.SysFont(None, 80)
q1 = font1.render("Найди и включи радио", True, (255,255,255))

img_main = "hero.jpg"
img_attack = "belt.jpg"
img_mafaka = "ogre.jpg"
img_radio = "radio.jpg"

class GameSprite(sprite.Sprite):
    def  __init__(self, player_image, player_x, player_y, width, height, player_speed):
        sprite.Sprite.__init__(self)
        self.image  = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
        
    def update(self):
        keys = key.get_pressed()
        if keys[K_a]  and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 100:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width -100:
            self.rect.y +=  self.speed


class Attack1(GameSprite):
    def __init__(self, player_image, player_x, player_y, width, height, player_speed,  damage):
        super().__init__(player_image, player_x, player_y, width, height, player_speed)
        self.dmg = damage
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_height or self.rect.x > win_width:
            self.kill()

class Attack2(GameSprite):
    def __init__(self, player_image, player_x, player_y, width, height, player_speed,  damage):
        super().__init__(player_image, player_x, player_y, width, height, player_speed)
        self.dmg = damage
    def update(self):
        self.rect.y += self.speed
        self.rect.x += self.speed
        if self.rect.y > win_height or self.rect.x > win_width:
            self.kill()
class Attack3(GameSprite):
    def __init__(self, player_image, player_x, player_y, width, height, player_speed,  damage):
        super().__init__(player_image, player_x, player_y, width, height, player_speed)
        self.dmg = damage
    def update(self):
        self.rect.y += self.speed
        self.rect.x -= self.speed
        if self.rect.y > win_height or self.rect.x > win_width:
            self.kill()


        
take_sound = mixer.Sound('ugabuga.mp3')
roar_sound = mixer.Sound('t-rex-roar.mp3')
enter_sound = mixer.Sound('tu-tu-tu-du-max-verstappen.mp3')
break_em = mixer.Sound('lego-breaking.mp3')
whip1 = mixer.Sound('whip_c09ceQZ.mp3')
whip2 =  mixer.Sound('whip-sound-effect-1.mp3')
whip3 = mixer.Sound('crack_the_whip.mp3')
he_came = mixer.Sound('yt1s_nYWSz5R.mp3')        
    

belt1 = Attack1(img_attack, 500, 890, 40, 80, 3, 1)
belt2 = Attack2(img_attack, 500, 890, 40, 80, 3, 1)
belt3 = Attack3(img_attack, 500, 890, 40, 80, 3, 1)
player = Player(img_main, 700, 700, 100, 100, 1)
radio = GameSprite(img_radio, 120, 420, 80, 80, 0)
ogre = GameSprite(img_mafaka, 700, 700, 100, 100, 0)

def whip():
    y = randint(1,3)
    if y == 1:
        mixer.music.play(whip1)
    if y == 2:
        mixer.music.play(whip2)
    else:
        mixer.music.play(whip3)
here = False
broke = False
finish =  False
run = True
hp = 3
i = 0
strt_time = 0
cur_time = 0
while run:
    for e  in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        win.blit(background, (0,0))


        if player.rect.colliderect(radio.rect):
            broke = True
        if broke == True:
            radio.kill()           
            mixer.music.stop()
            break_em.play()           
            roar_sound.set_volume(0.15)
            roar_sound.play()
            strt_time = timer()
            cur_time = strt_time
            broke = False

        cur_time = timer()
        timme = cur_time - strt_time
        if timme == 4:
            timme = False
            mixer.music.play(enter_sound)
            heis = timer()
            if heis == 7 and timme == False:
                mixer.music.play(he_came)
                ogre.reset()
                mixer.music.play(roar_sound)
                if heis == 2:
                    belt1.update()
                    belt1.reset()
                    whip()
                    i += 1
                    if heis == 3:
                        belt2.update()
                        belt2.reset()
                        whip()
                        i += 1
                        if heis == 4:
                            belt3.update()
                            belt3.reset()
                            whip()
                            i += 1
                            if heis == 6:
                                belt1.update()
                                belt1.reset()
                                whip()
                                i += 1
                                if heis == 8:
                                    belt2.update()
                                    belt2.reset()
                                    whip()
                                    i += 1
                                    if heis == 10:
                                        belt3.update()
                                        belt3.reset()
                                        whip()
                                        i += 1
                                        ogre.kill()
                                        heis = False
                                        mixer.music.play(roar_sound)
                                        mixer.music.play("happy-monkey-circle.mp3")
                                
        if player.rect.colliderect(belt1.rect) or player.rect.colliderect( belt2.rect) or player.rect.colliderect( belt3.rect):            
           
            
            hp-=1

        if hp == 0:
            finish = True
            mixer.music.play(take_sound)


        

        player.update()
        player.reset()
        radio.reset()

    display.update()