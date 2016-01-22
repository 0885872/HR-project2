#This code has to be added ...

import pygame
import time
import random
 
pygame.init()
 
display_width = 1280
display_height = 720
 
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

navy = (0,150,200)

gray = (100,100,100)
dark_gray = (80,80,80)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Survivor')
clock = pygame.time.Clock()

next = "menu"

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(gameDisplay, black,(x-5,y-5,w+10,h+10))
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("freesansbold.ttf",40)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def game_loop():

  print("Game loop")

def rtext(txt,offset):
  smallText = pygame.font.Font('freesansbold.ttf',20)
  TextSurf, TextRect = text_objects(txt, smallText)
  TextRect.left = (20)
  TextRect.top = (display_height/4+50+(offset*23))
  gameDisplay.blit(TextSurf, TextRect)

def game_rules():

    next = "rules"

    while next == "rules":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(navy)
        pygame.draw.rect(gameDisplay, black,(10,(display_height/4+40),display_width-20,385))
        pygame.draw.rect(gameDisplay, gray,(15,(display_height/4+45),display_width-30,375))
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("RULES", largeText)
        TextRect.center = ((display_width/2),(display_height/6))
        gameDisplay.blit(TextSurf, TextRect)
        rtext("1. Diegene die het hoogst gooit begint met het spel", 0)
        rtext("2. Elke speler heeft zijn eigen hoek en start in die hoek met de klok mee", 1)
        rtext("3. Elke speler begint met 100 levenspunten en 15 conditiepunten", 2)
        rtext("4. Elke speler heeft een scorekaart van zijn karakter en een bijpassende pion", 3)
        rtext("5. Er wordt gedobbeld om voort te bewegen over het spelbord", 4)
        rtext("6. Wanneer een speler op een vakje 'Fight!' terecht komt, moet deze vechten tegen een superfighter", 5)
        rtext("7. Aan de hand van de scorekaart en de gedobbelde waarde kan een speler zijn aanval kiezen", 6)
        rtext("8. Wanneer men geen conditiepunten heeft, kan er geen aanval gekozen", 7)
        rtext("9. Wanneer er gevochten moet worden en beide spelers geen conditiepunten hebben, verliest de verdediger 15 levenspunten", 8)
        rtext("10. De hoogste aanval - de laagste aanval = het aantal levenspunten dat de speler met de laagste aanval kwijt raakt", 9)
        rtext("11. Wanneer er twee spelers op hetzelfde vak komen, wordt er tegen elkaar gevochten", 10)
        rtext("12. Wanneer er twee spelers op hetzelfde 'Fight!'-vak terecht komen wordt er alleen gevochten met de superfighter", 11)
        rtext("13. Als je langs je eigen hoek komt krijg je het maximale aantal conditiepunten (15)", 12)
        rtext("14. Je ontvangt 10 levenspunten als je op je eigen hoek komt", 13)
        rtext("15. Als de speler van een hoek af is of als een hoek geen speler heeft, geven de vakjes van die hoek -10 levenspunten schade", 14)
        rtext("16. Als je geen levenspunten meer hebt, heb je verloren", 15)

        button("BACK",(display_width/2-100),640,200,50,dark_gray,gray,game_menu)

        pygame.display.update()
        clock.tick(15)

def quitgame():
  pygame.quit()
  quit()

def game_menu():

    next = "menu"
    while next == "menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(navy)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("MENU", largeText)
        TextRect.center = ((display_width/2),(display_height/6))
        gameDisplay.blit(TextSurf, TextRect)
      
        button("PLAY",(display_width/2-100),240,200,50,dark_gray,gray,game_loop)
        button("RULES",(display_width/2-100),340,200,50,dark_gray,gray,game_rules)
        button("EXIT",(display_width/2-100),440,200,50,dark_gray,gray,quitgame)

        pygame.display.update()
        clock.tick(15)

game_menu()

#----------------------------------------------------------------------------------------------------------------------------

import pygame
from pygame.locals import*

pygame.init()

img = pygame.image.load('board.png')
lol = pygame.image.load("pawn.png")

navy = (0, 150, 200)
w = 800
h = 700
screen = pygame.display.set_mode((w, h))
screen.fill((navy))
running = 1


while running:
    screen.fill((navy))
    screen.blit(img,(0,0))
    screen.blit(lol,(0,0))
    pygame.display.flip()

#--------------------------------------------------------------------------------------------------------------------------
class Dice:
  def __init__(self, x, y):
    self.X = x
    self.Y = y

  diceval = 0

  dice1 = pygame.image.load("Content\dice_1.png").convert_alpha()
  dice2 = pygame.image.load("Content\dice_2.png").convert_alpha()
  dice3 = pygame.image.load("Content\dice_3.png").convert_alpha()
  dice4 = pygame.image.load("Content\dice_4.png").convert_alpha()
  dice5 = pygame.image.load("Content\dice_5.png").convert_alpha()
  dice6 = pygame.image.load("Content\dice_6.png").convert_alpha()

  def dice(self, diceval):
    dthrow = random.randint(1,6)
    while diceval == dthrow:
      dthrow = random.randint(1,6)
    diceval = dthrow

    if dthrow == 1:
      #draw pic with 1 eye
      gameDisplay.blit(self.dice1, (self.X, self.Y))
    elif dthrow == 2:
      #draw pic with 2 eyes
      gameDisplay.blit(self.dice2, (self.X, self.Y))
    elif dthrow == 3:
      #draw pic with 3 eyes
      gameDisplay.blit(self.dice3, (self.X, self.Y))
    elif dthrow == 4:
      #draw lic with 4 eyes
      gameDisplay.blit(self.dice4, (self.X, self.Y))
    elif dthrow == 5:
      #draw pic with 5 eyes
      gameDisplay.blit(self.dice5, (self.X, self.Y))
    else:
      #draw pic with 6 eyes
      gameDisplay.blit(self.dice6, (self.X, self.Y))
    pygame.display.update()
    return diceval


  def throwdice(self):
    for x in range(0,8):
      diceval = self.dice(self.diceval)
      time.sleep(((x/1.5)**2*0.05))

