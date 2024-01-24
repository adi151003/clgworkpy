import pygame
pygame.init()

#screen
gameWindow =pygame.display.set_mode((1200,800))
pygame.display.set_caption ("First game")




#game specific var
exit_game = False
game_over = False

#creating a game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("you have pressed right key")


        

    

pygame.quit()
quit()
