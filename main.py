##
# Grocery Collector game for CPT
#
# @author Colin Chambachan
# @course ICS3U
# @date June 8th, 2020

"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
 
Explanation video: http://youtu.be/4W2AqUetBi4
"""
import pygame
import random
import time

## Model 
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE = (16, 140, 201)
class Player(pygame.sprite.Sprite):
    """ Create a class for the main character of the game, that will be controlled by the user"""
 
    ## Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
 
        # Import the Image to be used as the main character
        self.image = pygame.image.load("Player.png").convert()
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image, (67, 133))
        
        # Make the image mappable
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Have an attrbute as to where the user is facing, this way the image can be flipped if they want to move the other way
        self.direction_facing = "Left"
    
        # Set speed vectors
        self.change_x = 0
        self.change_y = 0
  
    def update(self):
        """Update the location of the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y
    
    def draw(self):
        """ Blits the player onto the screen, and checks for the orientation inputted by the user, """                      
        if self.direction_facing == "right":
            screen.blit(pygame.transform.flip(self.image, True, False), [self.rect.x, self.rect.y])
        else:
            screen.blit(self.image, [self.rect.x, self.rect.y])

class FallingItem(pygame.sprite.Sprite):
    """ Creating a class for the fruits in the game and bacteria, this will make it easier to animate and check for collision detection"""
    ## Methods
    def __init__(self,filename,x,y):
        """Constructor Function"""
        # inherites pygame.sprite.Sprite attributes
        super().__init__() 

        ## Attributes about the fruit
        # Allows the fruits image to be chosen (or rather generated randomly)
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image, (20, 20))
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        # Assign the beginning x and y values based off of the inputted values
        self.rect.x = x
        self.rect.y = y

    def update(self,fallspeed):
        # Update the sprite to look as though it is falling
        self.rect.y += fallspeed
        # Check to see if the item went off of the screen, and set it back to the top with a random x location
        if self.rect.y > 350:
            self.rect.y= random.randrange(-1000,0)
            self.rect.x = random.randrange(screen_width)
    
    def draw(self):
        screen.blit(self.image, self.rect)

class TravellingBaby(pygame.sprite.Sprite):
    """ Creating a class for the travlling baby that could take away points from the user"""
    def __init__(self):
        """constructor function that inherites the attributes of the pygame.sprite.Sprite class"""
        super().__init__

        ## Attributes about the traveling baby
        # Declare the image used for the travelling baby, and transforming its scale so its not as big
        self.image = pygame.image.load("BabyShoppingCart.png").convert()
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image, (50,50) ) 
        # Fetch the rectangly that has the dimensions of the image
        self.rect = self.image.get_rect()
        # Since the baby is only travelling horizontally, the baby only need an x coordinate to deal with
        # Assign a random coordinate off of the screen, so that the baby coming onto the screen seem to have a random change
        self.rect.x = random.randrange(-1000,0)

    def update(self):
        """ Update the location of the baby as it travels horizontally"""
        self.rect.x += 4
    
    def draw(self):
        """Blit the image of the baby onto the screen, thus allowing for it take part in the game"""
        screen.blit(self.image, (self.rect.x, 283))

def ScoreboardUpdate(score, timeLeft):
    # Select the font to be used for score and timer
    font = pygame.font.SysFont('Calibri', 25, True, False) 
    
    ## Adjusting the score the user has
    # Render the text to be printed
    scoreText = font.render("Score: " + str(score), True, BLACK)
    # Draw a rectangle on the screen under the score to make it more astheically pleasing
    pygame.draw.rect(screen, BLUE, [595,320, 102, 28])
    # Given the rectangle a slight outline
    pygame.draw.rect(screen, BLACK, [595,320, 102, 28], 1)
    # Drawing the score on the screen
    screen.blit(scoreText, [600, 325])
    
    ## Adjusting the time left
    timeRemainingText = font.render("Time: " + str(timeLeft), True,BLACK)
    # Draw a rectangle on the screen under the score to make it more astheically pleasing
    pygame.draw.rect(screen, BLUE, [0,0, 90, 28])
    # Given the rectangle a slight outline
    pygame.draw.rect(screen, BLACK, [0,0, 90, 28], 1)
    # Drawing the time left onto the screen
    screen.blit(timeRemainingText, [0,0])

    # Create text to say that there are 30 seconds left
    if timeLeft == 30:
        warningfont = pygame.font.SysFont('Calibri', 45, True, True)
        # Render the font for the text
        ThirtySecondsLeft = warningfont.render("30 SECONDS REMAINING!", True, BLUE)
        # Bliting the warning onto the screen
        screen.blit(ThirtySecondsLeft, [125, 150])

def EndGameScreen(score):
    # Create a computer reaction depending on the score of the user, and ouput the score dependantly
    if score > 30:
        # Playing the winning sound
        game_won.play()
        # Create the font to be used for the end game screen
        endGameFont = pygame.font.SysFont("Calibri", 45, True, False)
        computerReaction = "nice!"
        # Render the text to be put onto the end game screen
        endGameText = endGameFont.render("Your score was "+ str(score) + ", "+ str(computerReaction), False, BLACK )
        # Create a rectangle that the text of the end game screen will be on
        pygame.draw.rect(screen, BLUE, [100,125, 497, 75])
        pygame.draw.rect(screen, BLACK, [100,125, 497, 75], 5)
        # blit the text onto the screen
        screen.blit(endGameText, (110, 135))
    else:
        # Playing the losing sound
        game_lost.play()
        # Create the font to be used for the end game screen
        endGameFont = pygame.font.SysFont("Calibri", 39, True, False)
        computerReaction = "better luck next time :("
        # Render the text to be put onto the end game screen
        endGameText = endGameFont.render("Your score was "+ str(score) + ", "+ str(computerReaction), False, BLACK )
        # Create a rectangle that the text of the end game screen will be on
        pygame.draw.rect(screen, BLUE, [0,125, 700, 75])
        pygame.draw.rect(screen, BLACK, [0,125, 700, 75], 5)
        # blit the text onto the screen
        screen.blit(endGameText, (10, 135))

# Initialize Pygame
pygame.init()
 
# Open and Create Window
screen_width = 700
screen_height = 350
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Grocery Mayhem!")

## Creating the sound of the game
# Music that going to played throughout the game
game_music = pygame.mixer.Sound("GameMusic.wav")
# Ambient music for the effect of being in a grocery store
ambient_noise = pygame.mixer.Sound("GroceryAmbience.wav")
# Adjusting the volume of the ambient noise to be quieter
ambient_noise.set_volume(0.5)
# Music to signify the end of the game and the user got a good score
game_won = pygame.mixer.Sound("GameWon.wav")
# Music to signify the end of the game and the user got a bad score
game_lost = pygame.mixer.Sound("GameLost.wav")
# Music that plays when either the fruit is caught or the bacteria is hit
fruit_hit = pygame.mixer.Sound("FruitCollected.wav")
bacteria_hit = pygame.mixer.Sound("BacteriaHit.wav")

# playing both the game music and the ambient music
game_music.play()
ambient_noise.play()

## Creating the images seen in the game
# Importing the backround image for the game
background_image = pygame.image.load("BackgroundImage.jpg").convert()
# Create the instance of the main character
main_character = Player(350,200)
# Create instance of the travelling baby
travelling_baby = TravellingBaby()


# Create a list of fruits so that the fruits generated a randomly chosen
possibleFruits = ["Apple.png","Banana.png","Melon.png","Orange.png", "Pear.png"]
# Use the pygame.sprite.group() to put all the falling fruits into one list and the bacteria in one list
fruits_list = pygame.sprite.Group()
bacteria_list = pygame.sprite.Group()
# Create a for loop that will create all the instances of the fruits
for i in range(100):
    # Creates a random item selector which will pick (as an index parameter) which fruit is being loaded
    itemSelector = random.randrange(5)
    # Setting a random x location of the fruit and a random y location above the screen
    GroceryFruit_x = random.randrange(screen_width)
    GroceryFruit_y = random.randrange(-7500,0)
    # Create the instance of the fruit
    GroceryFruit = FallingItem(possibleFruits[itemSelector], GroceryFruit_x, GroceryFruit_y)
    # Add the fruit to the list of objects
    fruits_list.add(GroceryFruit)

# Create a for loop that will create all the instances of the bacteria
for i in range(20):
    # Creates instances of the of the FallingItems 
    Bacteria_x = random.randrange(screen_width)
    Bacteria_y = random.randrange(-9000,0)
    bacteria = FallingItem("Bacteria.png",Bacteria_x, Bacteria_y)
    # Add the instance to a list of all the bacteria
    bacteria_list.add(bacteria)

# Create a counter that will be used as the 'timer' of the game
secondsLeft = 60   
# Updates the pygame.USEREVENT every 1000 milliseconds, the equivalent of one second in the game, design used from https://stackoverflow.com/questions/30720665/countdown-timer-in-pygame
pygame.time.set_timer(pygame.USEREVENT, 1000) 
# Create a variable that depicts the fall speed of the items, which can then be adjusted if the if the time is below a certain amount
fruitFallSpeed = 1
# Have a score variable that will be blit'd onto the screen
score = 0
# Loop until the user clicks the close button.
done = False 
# Used to manage how fast the screen updates
clock = pygame.time.Clock() 
# -------- Main Program Loop -----------
while not done:
    ## Control
    # Check to see if any user action has occurred
    for event in pygame.event.get(): 
        # Check to the see if the user wants to quit the game
        if event.type == pygame.QUIT: 
            done = True
        # Check to see if any event as occured, and subtract one from the number of seconds left
        if event.type == pygame.USEREVENT:
            secondsLeft-= 1
        # Check to see if the user wants to move a certain direction, including jumping, and adjust the attributes accrodingly
        elif event.type == pygame.KEYDOWN: 
            # User wants to jump
            if event.key == pygame.K_UP:
                # Change the value of the characters y value to rise on the screen, and then eventually fall
                main_character.change_y = -10
            # User wants to move left
            if event.key == pygame.K_LEFT:
                main_character.change_x = -4
                # change the orientation of the character, so that it will be drawn accordingly in the draw() method
                main_character.direction_facing = "left"
            # User wants to move right
            elif event.key == pygame.K_RIGHT:
                main_character.change_x = 4
                # change the orientation of the character, so that it will be drawn accordingly in the draw() method
                main_character.direction_facing = "right"               
       
       
        # Check tto see if the user wants to stop moving, and adjust the attributes accrodingly
        elif event.type == pygame.KEYUP:
            # User wants to stop jumping
            if event.key == pygame.K_UP:
                main_character.change_y = 10
            # User wants to stop moving left
            if event.key == pygame.K_LEFT:
                main_character.change_x = 0    
            # User wants to stop moving right
            elif event.key == pygame.K_RIGHT:
                main_character.change_x = 0   
    
    # Check to see if the game ended (the timer ran out) and then break out of the while loop the game is running within
    if secondsLeft <= 0:
        done = True

    # Check to see if the player went off of the screen and bring them back on the other side
    if main_character.rect.x < 0:
        main_character.rect.x = screen_width
    if main_character.rect.x > screen_width:
        main_character.rect.x = 0
    # Check to see if the user jumped too high or is falling too far down and adjust accordingly
    if main_character.rect.y < 150:
        main_character.rect.y = 150
    elif main_character.rect.y > 200:
        main_character.rect.y = 200
    # Check to see if it is the last 20 seconds of the game, and if it is, increase the fall speed of the items
    if secondsLeft <= 30:
        fruitFallSpeed = 2
    
    # Check to see if the baby went off of the screen, and if so reassign its x coordinate
    if travelling_baby.rect.x > screen_width:
        travelling_baby.rect.x = random.randrange(-1000,0)
    
    # Update the location of the player, fruits and the baby
    main_character.update()
    fruits_list.update(fruitFallSpeed)
    bacteria_list.update(fruitFallSpeed)
    travelling_baby.update()

    # Check to see if the play hit any of the fruits, and if so reward them with a point
    fruits_hit_list = pygame.sprite.spritecollide(main_character, fruits_list, True)
    for GroceryFruit in fruits_hit_list:
        # Play the good sound FX noise for hitting the fruit
        fruit_hit.play()
        # Increasing the score by one if the player gets the fruit
        score += 1
    
    bacteria_hit_list = pygame.sprite.spritecollide(main_character, bacteria_list, True)
    # Check to see if the play hit any of the bacteria, and if so deduct a point
    for Bacteria in bacteria_hit_list:
        # Play the bad sound FX noise for hitting the bacteria
        bacteria_hit.play()
        # Decrease the score by one if the player gets the fruit
        score -= 1
    
    babyPlayerCollision = pygame.sprite.collide_rect(main_character,travelling_baby)
    # Check for collision detection between the baby and the character
    if babyPlayerCollision == True:
        # Decrease the score by 5 if the character hits the baby
        score -= 5

    ## View
    
    # Clear the screen
    screen.fill(WHITE)
    # Blit the Backround onto the screen
    screen.blit(background_image,[0,0])
    
    # Draw the character, fruits, bacteria, and baby onto the given location
    main_character.draw()
    fruits_list.draw(screen)
    bacteria_list.draw(screen)
    travelling_baby.draw()

    # Update and output the scoreboard and time left to the user
    ScoreboardUpdate(score, secondsLeft)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)


# Blit the final score onto the screen using the EndGameScreen function
EndGameScreen(score)
pygame.display.flip()
# Make the window pause long enough for the user to read the end screen
time.sleep(5)
# Exit the window
pygame.quit()