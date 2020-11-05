from random import randint
import pygame
pygame.init()

ROSSO = (255, 0, 0)
NERO = (0, 0, 0)
VIOLA = (135, 0, 255)
GIALLO = (255,255,0)
VERDE = (0, 255, 0)
BIANCO = (255, 255, 255)

SCHERMO = (900, 900)
schermo = pygame.display.set_mode(SCHERMO)
schermo.fill(NERO)

FONT = pygame.font.SysFont('Arial', 20)
checkpoint_render = FONT.render(("checkpoint"), 1, GIALLO)
FONT2 = pygame.font.SysFont('Comfortaa', 50)

r = 255
x = 0
y = 0
avanzamento = 3
coloramento = -0.5
vittoria = False

GRANDEZZA_BLOCCO = (45, 45)

check = pygame.Rect((6, 396), (50, 3))
immagineC = pygame.Surface((90, 3))
immagineC.fill(ROSSO)

torre1 = pygame.Rect((100, 0), (45, 90))
immagine2 = pygame.Surface((45, 90))
immagine2.fill(VIOLA)

torre2 = pygame.Rect((0, 150), (800, 45))
immagine3 = pygame.Surface((800, 45))
immagine3.fill(VIOLA)

torre3 = pygame.Rect((220, 60), (45, 90))
immagine4 = pygame.Surface((45, 90))
immagine4.fill(VIOLA)

torre4 = pygame.Rect((330, 0), (45, 45))
immagine5 = pygame.Surface((45, 45))
immagine5.fill(VIOLA)

torre5 = pygame.Rect((330, 105), (45, 45))
immagine6 = pygame.Surface((45, 45))
immagine6.fill(VIOLA)

torre6 = pygame.Rect((500, 0), (45, 45))

torre7 = pygame.Rect((500, 45), (200, 45))
immagine7 = pygame.Surface((200, 45))
immagine7.fill(VIOLA)

torre8 = pygame.Rect((755, 60), (45, 90))
immagine8 = pygame.Surface((45, 90))
immagine8.fill(VIOLA)

torre9 = pygame.Rect((100, 350), (800, 45))
immagine9 = pygame.Surface((800, 45))
immagine9.fill(VIOLA)

torre10 = pygame.Rect((750, 275), (45, 90))
immagine10 = pygame.Surface((45, 90))
immagine10.fill(VIOLA)

torre11 = pygame.Rect((385, 195), (300, 90))
immagine11 = pygame.Surface((300, 90))
immagine11.fill(VIOLA)

torre12 = pygame.Rect((100, 250), (220, 45))
immagine12 = pygame.Surface((220, 45))
immagine12.fill(VIOLA)

torre13 = pygame.Rect((0, 550), (800, 45))
immagine13 = pygame.Surface((800, 45))
immagine13.fill(VIOLA)

torre14 = pygame.Rect((150, 450), (200, 45))
immagine14 = pygame.Surface((200, 45))
immagine14.fill(VIOLA)

torre15 = pygame.Rect((305, 395), (45, 55))
immagine15 = pygame.Surface((45, 55))
immagine15.fill(NERO)

torre16 = pygame.Rect((425, 450), (200, 45))
immagine16 = pygame.Surface((200, 45))
immagine16.fill(VIOLA)

torre17 = pygame.Rect((580, 495), (45, 55))

torre18 = pygame.Rect((700, 395), (45, 90))
immagine18 = pygame.Surface((45, 90))

torre19 = pygame.Rect((100, 775), (800, 45))
immagine19 = pygame.Surface((800, 45))
immagine19.fill(VIOLA)

torre20 = pygame.Rect((750, 655), (45, 120))
immagine20 = pygame.Surface((45, 120))

torre21 = pygame.Rect((630, 595), (45, 120))

torre22 = pygame.Rect((510, 655), (45, 120))
immagine22 = pygame.Surface((45, 120))
immagine22.fill(VIOLA)

torre23 = pygame.Rect((390, 595), (45, 120))

torre24 = pygame.Rect((270, 655), (45, 120))

torre25 = pygame.Rect((150, 595), (45, 125))
immagine25 = pygame.Surface((45, 125))
immagine25.fill(VIOLA)

Traguardo = pygame.Rect((800, 820), (100, 80))
immagineT = pygame.Surface((100, 80))
immagineT.fill(VERDE)

Navicella_UP = pygame.image.load('12-138961_vector-spaces-ship-8-bit-spaceship-sprite.jpg')
Navicella_UP = pygame.transform.scale(Navicella_UP, (45, 45))
n_UP = False
Navicella_DX = pygame.image.load('13-138961_vector-spaces-ship-8-bit-spaceship-sprite.jpg')
Navicella_DX = pygame.transform.scale(Navicella_DX, (45, 45))
n_DX = False
Navicella_DOWN = pygame.image.load('14-138961_vector-spaces-ship-8-bit-spaceship-sprite.jpg')
Navicella_DOWN = pygame.transform.scale(Navicella_DOWN, (45, 45))
n_DOWN = True
Navicella_SX = pygame.image.load('15-138961_vector-spaces-ship-8-bit-spaceship-sprite.jpg')
Navicella_SX = pygame.transform.scale(Navicella_SX, (45, 45))
n_SX = False

Navicella_R_UP = pygame.image.load('RED16-138961_vector-spaces-ship-8-bit-spaceship-sprite.jpg')
Navicella_R_UP = pygame.transform.scale(Navicella_R_UP, (45, 45))
r_UP = False
Navicella_R_DX = pygame.image.load('RED17-138961_vector-spaces-ship-8-bit-spaceship-sprite.jpg')
Navicella_R_DX = pygame.transform.scale(Navicella_R_DX, (45, 45))
r_DX = False
Navicella_R_SX = pygame.image.load('RED18-138961_vector-spaces-ship-8-bit-spaceship-sprite.jpg')
Navicella_R_SX = pygame.transform.scale(Navicella_R_SX, (45, 45))
r_SX = False
Navicella_R_DOWN = pygame.image.load('RED19-138961_vector-spaces-ship-8-bit-spaceship-sprite.jpg')
Navicella_R_DOWN = pygame.transform.scale(Navicella_R_DOWN, (45, 45))
r_DOWN = False

clock = pygame.time.Clock()
FPS = 60
time = 0
a_t = 0.02

q = 5
a_q = 1

while True:
 clock.tick(FPS)
 time_render = FONT2.render(str(time), 1, BIANCO)
 time2_render = FONT2.render(("Tempo trascorso: "), 1, BIANCO)
 time += a_t
 r += coloramento
 immagine15.fill((r, r, r))
 immagine18.fill((r, r, r))
 immagine20.fill((r, r, r))
 if vittoria != True:
     schermo.fill(NERO)
 else:
     schermo.fill(ROSSO)
 
 q += a_q
 if q == 255 or q == 0:
     a_q *= -1


 if n_UP == True:
     schermo.blit(Navicella_UP, (x, y))
 elif n_DOWN == True:
     schermo.blit(Navicella_DOWN, (x, y))
 elif n_DX == True:
     schermo.blit(Navicella_DX, (x, y))
 elif n_SX == True:
     schermo.blit(Navicella_SX, (x, y))
 else:
     pass 

 if r_UP == True:
     schermo.blit(Navicella_R_UP, (x, y))
 elif r_DOWN == True:
     schermo.blit(Navicella_R_DOWN, (x, y))
 elif r_DX == True:
     schermo.blit(Navicella_R_DX, (x, y))
 elif r_SX == True:
     schermo.blit(Navicella_R_SX, (x, y))
 else:
     pass 

 keys = pygame.key.get_pressed() 
 if keys[pygame.K_LEFT]:
     x -= avanzamento
     if vittoria != True:
         n_UP = False
         n_DX = False
         n_DOWN = False
         n_SX = True
     else:
         r_UP = False
         r_DX = False
         r_DOWN = False
         r_SX = True

 if keys[pygame.K_RIGHT]:
     x += avanzamento
     if vittoria != True:
         n_UP = False
         n_DX = True
         n_DOWN = False
         n_SX = False
     else:
         r_UP = False
         r_DX = True
         r_DOWN = False
         r_SX = False


 if keys[pygame.K_DOWN]:
     y += avanzamento
     if vittoria != True:
         n_UP = False
         n_DX = False
         n_DOWN = True
         n_SX = False
     else:
         r_UP = False
         r_DX = False
         r_DOWN = True
         r_SX = False


 if keys[pygame.K_UP]:
     y -= avanzamento
     if vittoria != True:
         n_UP = True
         n_DX = False
         n_DOWN = False
         n_SX = False
     else:
         r_UP = True
         r_DX = False
         r_DOWN = False
         r_SX = False


 if x >= 900 or y >= 900:
     quit()

 if y < 351: #1 sx          #1 dx                   #1 sotto                            #2 sopra                 #2 sotto                 #2 dx                                 #3 sx                                #3 dx                                #3 sopra                             #4 sx                   #4 dx                   #4 sotto                             #5 sx                               #5 dx                                #5 sopra                             #6+7 sx                  #7 sotto                             #7 dx                               #8 sx                                #8 dx                               #8 sopra                             #9 sopra                 #9 sotto                 #9 sx                               #10 dx                                #10 sx                                #10 sopra                             #11 sx                                #11 dx                                 #11 sotto                            #12 sotto                             #12 sopra                            #12 dx                                #12 sx                               #13 sopra                #13 sotto                #13 dx                                #14 sx                                #14 dx                                #14 sopra                             #14 sotto                               #15 sx                              #15 dx                                #16 sx                                #16 dx                               #16 sopra                              #16 sotto                             #17 sx                                #17 dx                               #18 sx                                #18 dx                                #19 sopra               #19 sotto               #19 sx                               #20 dx                                #20 sx                                #20 sopra                             #21 dx                                #21 sx                                #21 sotto                             #22 dx                                #22 sx                                #22 sopra                            #23 dx                                #23 sx                                #23 sotto                             #24 dx                                #24 sx                                   #24 sopra                          #25 dx                                #25 sx                                #25 sotto
     if x == 54 and y <= 90 or x == 144 and y <= 90 or x >= 54 and x <= 144 and y == 90 or x <= 800 and y == 105 or x <= 800 and y == 192 or x == 801 and y <= 195 and y >= 150 or x == 174 and y >= 15 and y <= 105 or x == 264 and y >= 15 and y <= 105 or x >= 174 and x <= 264 and y == 15 or x == 285 and y <= 45 or x == 375 and y <= 45 or x >= 285 and x <= 375 and y == 45 or x == 285 and y >= 60 and y <= 105 or x == 375 and y >= 60 and y <= 105 or x >= 285 and x <= 375 and y == 60 or x == 444 and y <= 90 or x >= 501 and x <= 698 and y == 90 or x == 696 and y <= 90 and y >= 36 or x == 711 and y >= 15 and y <= 105 or x == 798 and y >= 15 and y <= 105 or x <= 711 and x >= 798 and y == 15 or x >= 100 and y == 303 or x >= 54 and y == 390 or x == 57 and y >= 342 and y <= 396 or x == 795 and y <= 340 and y >= 250 or x == 705 and y <= 340 and y >= 250 or x >= 705 and x <= 795 and y == 340 or x == 342 and y <= 285 and y >= 180 or x == 681 and y <= 285 and y >= 180 or x >= 342 and x <= 681 and y == 285 or x >= 102 and x <= 327 and y == 294 or x >= 86 and x <= 324 and y == 204 or x == 318 and y >= 246 and y <= 282 or x == 57 and y >= 216 and y <= 282 or x <= 801 and y == 504 or x <= 801 and y == 594 or x == 801 and y >= 504 and y <= 594 or x == 105 and y >= 420 and y <= 495 or x == 351 and y >= 420 and y <= 495 or y == 405 and x >= 129 and x <= 321 or y == 495 and x >= 129 and x <= 321 or x == 261 and y <= 408 and y >= 381 or x == 351 and y <= 408 and y >= 381 or x == 381 and y >= 411 and y <= 495 or x == 627 and y >= 420 and y <= 495 or y == 405 and x >= 402 and x <= 624 or y == 495 and x >= 402 and x <= 624 or x == 534 and y >= 483 and y <= 552 or x == 624 and y >= 483 and y <= 552 or x == 657 and y >= 393 and y <= 483 or x == 747 and y >= 393 and y <= 483 or x >= 60 and y == 729 or x >= 60 and y == 819 or x == 66 and y >= 729 and y <= 819 or x == 795 and y >= 615 and y <= 765 or x == 705 and y >= 615 and y <= 765 or x >= 705 and x <= 795 and y == 615 or x == 675 and y >= 595 and y <= 715 or x == 585 and y >= 595 and y <= 714 or x >= 585 and x <= 675 and y == 714 or x == 555 and y >= 615 and y <= 765 or x == 465 and y >= 615 and y <= 765 or x >= 465 and x <= 555 and y == 615 or x == 435 and y >= 595 and y <= 715 or x == 345 and y >= 595 and y <= 715 or x >= 345 and x <= 435 and y == 714 or x == 315 and y >= 615 and y <= 765 or x == 225 and y >= 615 and y <= 765 or x >= 225 and x <= 315 and y == 615 or x == 195 and y >= 595 and y <= 715 or x == 105 and y >= 594 and y <= 715 or x >= 105 and x <= 195 and y == 714:
         y = 0
         x = 0
         r = 255
         coloramento = -0.5
    
 if y > 351:
     if x == 54 and y <= 90 or x == 144 and y <= 90 or x >= 54 and x <= 144 and y == 90 or x <= 800 and y == 105 or x <= 800 and y == 192 or x == 801 and y <= 195 and y >= 150 or x == 174 and y >= 15 and y <= 105 or x == 264 and y >= 15 and y <= 105 or x >= 174 and x <= 264 and y == 15 or x == 285 and y <= 45 or x == 375 and y <= 45 or x >= 285 and x <= 375 and y == 45 or x == 285 and y >= 60 and y <= 105 or x == 375 and y >= 60 and y <= 105 or x >= 285 and x <= 375 and y == 60 or x == 444 and y <= 90 or x >= 501 and x <= 698 and y == 90 or x == 696 and y <= 90 and y >= 36 or x == 711 and y >= 15 and y <= 105 or x == 798 and y >= 15 and y <= 105 or x <= 711 and x >= 798 and y == 15 or x >= 100 and y == 303 or x >= 54 and y == 390 or x == 57 and y >= 342 and y <= 396 or x == 795 and y <= 340 and y >= 250 or x == 705 and y <= 340 and y >= 250 or x >= 705 and x <= 795 and y == 340 or x == 342 and y <= 285 and y >= 180 or x == 681 and y <= 285 and y >= 180 or x >= 342 and x <= 681 and y == 285 or x >= 102 and x <= 327 and y == 294 or x >= 86 and x <= 324 and y == 204 or x == 318 and y >= 246 and y <= 282 or x == 57 and y >= 216 and y <= 282 or x <= 801 and y == 504 or x <= 801 and y == 594 or x == 801 and y >= 504 and y <= 594 or x == 105 and y >= 420 and y <= 495 or x == 351 and y >= 420 and y <= 495 or y == 405 and x >= 129 and x <= 321 or y == 495 and x >= 129 and x <= 321 or x == 261 and y <= 408 and y >= 381 or x == 351 and y <= 408 and y >= 381 or x == 381 and y >= 411 and y <= 495 or x == 627 and y >= 420 and y <= 495 or y == 405 and x >= 402 and x <= 624 or y == 495 and x >= 402 and x <= 624 or x == 534 and y >= 483 and y <= 552 or x == 624 and y >= 483 and y <= 552 or x == 657 and y >= 393 and y <= 483 or x == 747 and y >= 393 and y <= 483 or x >= 60 and y == 729 or x >= 60 and y == 819 or x == 66 and y >= 729 and y <= 819 or x == 795 and y >= 615 and y <= 765 or x == 705 and y >= 615 and y <= 765 or x >= 705 and x <= 795 and y == 615 or x == 675 and y >= 595 and y <= 715 or x == 585 and y >= 595 and y <= 714 or x >= 585 and x <= 675 and y == 714 or x == 555 and y >= 615 and y <= 765 or x == 465 and y >= 615 and y <= 765 or x >= 465 and x <= 555 and y == 615 or x == 435 and y >= 595 and y <= 715 or x == 345 and y >= 595 and y <= 715 or x >= 345 and x <= 435 and y == 714 or x == 315 and y >= 615 and y <= 765 or x == 225 and y >= 615 and y <= 765 or x >= 225 and x <= 315 and y == 615 or x == 195 and y >= 595 and y <= 715 or x == 105 and y >= 594 and y <= 715 or x >= 105 and x <= 195 and y == 714:
         y = 381
         x = 0
         r = 255
         coloramento = -0.5
         
 if r == 0:
     coloramento *= 0

 if x >= 800 and y >= 820 and vittoria != True:
     checkpoint_render = FONT.render(("checkpoint"), 1, NERO)
     x = 0
     y = 0
     schermo.fill(ROSSO)
     vittoria = True

 if vittoria == True and not(x == 800 and y == 820):
     demon_render = FONT.render(("Demon level?..."), 1, NERO)
     schermo.blit(demon_render, (150,10))
     immagineC.fill(NERO)
     immagine2.fill((q, 0, 0))
     immagine3.fill((q, 0, 0))
     immagine4.fill((q, 0, 0))
     immagine5.fill((q, 0, 0))
     immagine6.fill((q, 0, 0))
     immagine7.fill((q, 0, 0))
     immagine8.fill((q, 0, 0))
     immagine9.fill((q, 0, 0))
     immagine10.fill((q, 0, 0))
     immagine11.fill((q, 0, 0))
     immagine12.fill((q, 0, 0))
     immagine13.fill((q, 0, 0))
     immagine14.fill((q, 0, 0))
     immagine15.fill((q, 0, 0))
     immagine16.fill((q, 0, 0))
     immagine18.fill((q, 0, 0))
     immagine19.fill((q, 0, 0))
     immagine20.fill((q, 0, 0))
     immagine22.fill((q, 0, 0))
     immagine25.fill((q, 0, 0))
     immagineT.fill(NERO)

 if vittoria == True and x >= 800 and y >= 820:
     schermo.fill(NERO)
     vittoria_render = FONT2.render(("Hai vinto sul serio... Complimenti"), 1, VIOLA)
     schermo.blit(vittoria_render, (200, 300))
     a_t *= 0


 for event in pygame.event.get():
     if event.type == pygame.QUIT:
         quit()


 schermo.blit(checkpoint_render, (9, 372))
 schermo.blit(immagineC, check)
 schermo.blit(immagine2, torre1)
 schermo.blit(immagine3, torre2)
 schermo.blit(immagine4, torre3)
 schermo.blit(immagine5, torre4)
 schermo.blit(immagine6, torre5)
 schermo.blit(immagine5, torre6)
 schermo.blit(immagine7, torre7)
 schermo.blit(immagine8, torre8)
 schermo.blit(immagine9, torre9)
 schermo.blit(immagine10, torre10)
 schermo.blit(immagine11, torre11)
 schermo.blit(immagine12, torre12)
 schermo.blit(immagine13, torre13)
 schermo.blit(immagine14, torre14)
 schermo.blit(immagine15, torre15)
 schermo.blit(immagine16, torre16)
 schermo.blit(immagine15, torre17)
 schermo.blit(immagine18, torre18)
 schermo.blit(immagine19, torre19)
 schermo.blit(immagine20, torre20)
 schermo.blit(immagine20, torre21)
 schermo.blit(immagine22, torre22)
 schermo.blit(immagine20, torre23)
 schermo.blit(immagine20, torre24)
 schermo.blit(immagine25, torre25)
 schermo.blit(immagineT, Traguardo)
 schermo.blit(time_render, (835, 783))
 schermo.blit(time2_render, (535, 783))
 pygame.display.update()