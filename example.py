# In this example.py you will learn how to make a very simple game using the pygame library.
# One of the best ways of learning to program is by writing games.
# Pygame is a collection of modules in one package.
# You will need to install pygame.
# To do so:
# 1) open the command line interface on your computer,
# 2) cd to the directory that this task is located in,
# 3) follow the instructions here: https://www.pygame.org/wiki/GettingStarted
# 4) if you need help using pip, see here: https://projects.raspberrypi.org/en/projects/using-pip-on-windows

import pygame # Imports a game library that lets you use specific functions in your program.
import random # Import to generate random numbers. 
import time
pygame.font.init()
# Initialize the pygame modules to get everything started.

pygame.init() 

# The screen that will be created needs a width and a height.

screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height)) # This creates the screen and gives it the width and height specified as a 2 item sequence.


#background screen
background = pygame.image.load("background.jpg")

#name of the game

pygame.display.set_caption("First Game")

icon = pygame.image.load("cartoon.png")
pygame.display.set_icon(icon)


#player
player= pygame.image.load("summer.png")

#enemies
enemy = pygame.image.load("bullet.png")
enemy2 = pygame.image.load("dead.png")


prize = pygame.image.load("prize.jpg")




# This creates the player and gives it the image found in this folder (similarly with the enemy image).





playerX = 10
playerY = 250





#score



#textX = 10
#textY = 10


#game over





#score and life of player adn sped of the enemy(stages of the game)
point=0
life=3
speed_enemy = 1
prize_coming = 1




# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).

image_height = player.get_height()
image_width = player.get_width()
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()

enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()

print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))

# Store the positions of the player and enemy as variables so that you can change them later. 

playerXPosition = 100

playerYPosition = 50

# Make the enemy start off screen and at a random y position.


enemyXPosition =  screen_width
enemyYPosition =  random.randint(0, screen_height - enemy_height)

enemy2XPosition =  screen_width
enemy2YPosition =  random.randint(0, screen_height - enemy2_height)


# This checks if the up or down key is pressed.
# Right now they are not so make them equal to the boolean value (True or False) of False. 
# Boolean values are True or False values that can be used to test conditions and test states that are binary, i.e. either one way or the other. 

keyUp = False
keyDown = False
keyLeft = False
keyRight = False





def main():
    run = True
    FPS = 60
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("comicsans",50)
    lost_font = pygame.font.SysFont("comicsans",60)


    clock = pygame.time.Clock()

    lost = False
    lost_count = 0


    
    def redraw_window():
        window.blit(background,(0,0))

        lives_label= main_font.render(f"Lives:{lives}",1,(255,255,255))
        level_label = main_font.render(f"Level:{level}",1,(255,255,255))

        window.blit(lives_label,(10,10))
        window.blit(level_label,(WIDTH-level_label.get_width()-10,10))



        if lost:
            lost_label = lost_font.render("You Lost!!",1,(255,255,255))
            WIN.blit(lost_label,(WIDTH/2 - lost_label.get_width()/2,350))



        pygame.display.update()


    while run:
        clock.tick(FPS)
        redraw_window()

        
        if lives <= 0 or player.health <=0:
            lost = True
            lost_count += 1



        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        
        









# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to 
# represent real time game play. 

while 1: # This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting). In Python the int 1 has the boolean value of 'true'. In fact numbers greater than 0 also do. 0 on the other hand has a boolean value of false. You can test this out with the bool(...) function to see what boolean value types have. You will learn more about while loop structers later. 

    screen.fill(0) # Clears the screen.
    #Background image
    screen.blit(background,(0,0))
    
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(enemy2,(enemy2XPosition, enemy2YPosition))


    #lives
    
    
    
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant. 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
        
        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False


                
        


                    


      #playerBox += playerBox_change
      #if playerBox <= 0:
       #playerBox = 0
       
    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position. 
    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 3
    if keyDown == True:
        if playerYPosition < screen_height - image_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 3
    if keyLeft == True:
        if playerXPosition > 0:
            playerXPosition -=1
    if keyRight == True:
        if playerXPosition < screen_height - image_height:
            playerXPosition +=1

            
    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())


       
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemy:
    
    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition
    
    # Test collision of the boxes:
    
        
    
    if playerBox.colliderect(enemyBox) or playerBox.colliderect(enemy2Box):
    
        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quite game and exit window: 
        
        life-=1

        if life < 0:
            pygame.quit()
            print("You lose!")
            print(f"Your score is:{point}")
            exit(0)
        
    # If the enemy is off the screen the user wins the game:
    
    if enemyXPosition < 0 - enemy_width:
    
        # Display wining status to the user: 
        
        enemyXPosition =  screen_width
        enemyYPosition =  random.randint(0, screen_height - enemy_height)
        
        # Quite game and exit window: 
        point += 1
        if point%5==0:
            print("You win!")
            speed_enemy +=1
            prize_coming +=1


    if point%5 ==0:
        prize_coming +1
    

    if enemy2XPosition < 0 - enemy2_width:
    
        # Display wining status to the user: 
        
        enemy2XPosition =  screen_width
        enemy2YPosition =  random.randint(0, screen_height - enemy2_height)
        
        # Quite game and exit window: 
        point += 1
        if point%5==0:
            print("You win!")
            speed_enemy +=1
        
        
    
 
    
    # Make enemy approach the player.
    
    enemyXPosition -= speed_enemy
    enemy2XPosition -= speed_enemy
    
    # ================The game loop logic ends here. =============
  
