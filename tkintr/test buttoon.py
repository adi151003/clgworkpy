import pygame
WIDTH = 800
HEIGHT = 500
FPS = 20                                             #controls how often the gameDisplay should refresh. In our case, it will refresh every 1/12th second
pygame.init()
pygame.display.set_caption('BLADE MASTER')
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))   #setting game display size
clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

font_name = pygame.font.match_font('fruit\\comic.ttf')
def draw_text(display, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    displaysurface.blit(text_surface, text_rect)

def show_gameover_screen():
    draw_text(displaysurface, "BLADE!", 90, WIDTH / 2, 30)
    draw_text(displaysurface,"Score : ", 70, WIDTH / 2, 130)
    draw_text(displaysurface,"GAME OVER", 70,400, 230)
    img2 = pygame.image.load('images/game_over.png')
    displaysurface.blit(img2,(350,300))
    draw_text(displaysurface, "Press a key to begin!", 64, WIDTH / 2, 450)
    pygame.display.flip()

smallfont = pygame.font.SysFont('Corbel',16) 
pygame.draw.rect(displaysurface, BLUE, [590, 315, 80 , 30])
text = smallfont.render('LOAD' , True , BLUE)
displaysurface.blit(text , (600 , 320))
mouse = pygame.mouse.get_pos()
while True:  
    for event in pygame.event.get():
        # For events that occur upon clicking the mouse (left click) 
        if event.type == pygame.MOUSEBUTTONDOWN:
              if 590 <= mouse[0] <= 670 and 315 <= mouse[1] <= 345:
                    show_gameover_screen()