import pygame
import random

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
BLUE = ( 0, 0, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

pygame.init()

size = (900, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe")

done = False #Loop until the user clicks the close button.
window = "main" #Window: menu, game, win, lose
player = "X" #Player's symbol
computer = "O" #computer's symbol
compmove = 0 #Random integer for computer turn
turn = "player" #to keep track of turn
status = "" #to show last move

#Mouse click event 
clickx = 0
clicky = 0
playchoice = ""

#Coordinates
A1 = ""
A2 = ""
A3 = ""
B1 = ""
B2 = ""
B3 = ""
C1 = ""
C2 = ""
C3 = ""



clock = pygame.time.Clock()


while not done:
    
# --- Main event loop
#Wait for player input
     #= pygame.event.wait()
    
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            clickx = pos[0]
            clicky = pos[1]
            if window == "game":
                turn = "comp"

#Main Menu Logic
    if window == "main":
        if (clickx >= 250 and clickx <= 650) and (clicky >= 150 and clicky <= 250):
            window = "choice"
            clickx = 0
            clicky = 0
        if (clickx >= 250 and clickx <= 650) and (clicky >= 300 and clicky <= 400):
            done = True

#Symbol choice Menu Logic
    if window == "choice":
        if (clickx >= 200 and clickx <= 300) and (clicky >= 300 and clicky <= 400):
            player = "X"
            computer =  "O"
            window = "game"
            clickx = 0
            clicky = 0
        if (clickx >= 600 and clickx <= 700) and (clicky >= 300 and clicky <= 400):
            player = "O"
            computer = "X"
            window = "game"
            clickx = 0
            clicky = 0

#Win Menu Logic
    if window == "win":
        if (clickx >= 250 and clickx <= 650) and (clicky >= 250 and clicky <= 350):
            window = "choice"
            clickx = 0
            clicky = 0
            A1 = "" #Reset coordinates
            A2 = ""
            A3 = ""
            B1 = ""
            B2 = ""
            B3 = ""
            C1 = ""
            C2 = ""
            C3 = ""
            turn = "player" #Reset turn
            playchoice = ""  #Reset players coice
        if (clickx >= 250 and clickx <= 650) and (clicky >= 400 and clicky <= 500):
            done = True
#Lose Menu Logic
    if window == "lose":
        if (clickx >= 250 and clickx <= 650) and (clicky >= 250 and clicky <= 350):
            window = "choice"
            clickx = 0
            clicky = 0
            A1 = "" #Reset coordinates
            A2 = ""
            A3 = ""
            B1 = ""
            B2 = ""
            B3 = ""
            C1 = ""
            C2 = ""
            C3 = ""
            turn = "player" #Reset turn
            playchoice = ""  #Reset players coice
        if (clickx >= 250 and clickx <= 650) and (clicky >= 400 and clicky <= 500):
            done = True

#Cat's Game Menu Logic
    if window == "cats":
        if (clickx >= 250 and clickx <= 650) and (clicky >= 250 and clicky <= 350):
            window = "game"
            clickx = 0
            clicky = 0
            A1 = "" #Reset coordinates
            A2 = ""
            A3 = ""
            B1 = ""
            B2 = ""
            B3 = ""
            C1 = ""
            C2 = ""
            C3 = ""
            turn = "player" #Reset turn
            playchoice = ""  #Reset players coice
        if (clickx >= 250 and clickx <= 650) and (clicky >= 400 and clicky <= 500):
            done = True

# -----Main Game Logic-----
    
#Get players choice
    if window == "game":
        if (clickx > 150 and clickx < 350) and (clicky > 50 and clicky < 250):
            playchoice = "A1"
        if (clickx > 350 and clickx < 550) and (clicky > 50 and clicky < 250):
            playchoice = "A2"
        if (clickx > 550 and clickx < 750) and (clicky > 50 and clicky < 250):
            playchoice = "A3"
        if (clickx > 150 and clickx < 350) and (clicky > 250 and clicky < 450):
            playchoice = "B1"
        if (clickx > 350 and clickx < 550) and (clicky > 250 and clicky < 450):
            playchoice = "B2"
        if (clickx > 550 and clickx < 750) and (clicky > 250 and clicky < 450):
            playchoice = "B3"
        if (clickx > 150 and clickx < 350) and (clicky > 450 and clicky < 650):
            playchoice = "C1"
        if (clickx > 350 and clickx < 550) and (clicky > 450 and clicky < 650):
            playchoice = "C2"
        if (clickx > 550 and clickx < 750) and (clicky > 450 and clicky < 650):
            playchoice = "C3"

#<<Cats>>
    if status != "won" and status != "lost" and A1 != "" and A2 != "" and A3 != "" and B1 != "" and B2 != "" and B3 != "" and C1 != "" and C2 != "" and C3 != "":
        clickx = 0 #Reset click
        clicky = 0
        window = "cats"

#<<Win>>
#Two in a row
    #1
    if A2 == player and A3 == player and A1 == player:
        clickx = 0 #Reset click
        clicky = 0
        status = "won"
    if B2 == player and B3 == player and B1 == player:
        clickx = 0 #Reset click
        clicky = 0
        status = "won"
    if C2 == player and C3 == player and C1 == player:
        clickx = 0 #Reset click
        clicky = 0
        status = "won"
    #2
    if A1 == player and A3 == player and A2 == player:
        clickx = 0 #Reset click
        clicky = 0
        status = "won"
    if B1 == player and B3 == player and B2 == player:
        clickx = 0 #Reset click
        clicky = 0
        status = "won"
    if C1 == player and C3 == player and C2 == player:
        clickx = 0 #Reset click
        clicky = 0
        status = "won"
    #3
    if A1 == player and A2 == player and A3 == player:
        clickx = 0 #Reset click
        clicky = 0
        status = "won"
    if B1 == player and B2 == player and B3 == player:
        clickx = 0 #Reset click
        clicky = 0
        status = "won"
    if C1 == player and C2 == player and C3 == player:
        clickx = 0 #Reset click
        clicky = 0
        status = "won"

#Two in a column
    #A
    if C1 == player and B1 == player and A1 == player:
        clickx = 0 #Reset click
        clicky = 0
        status = "won"
    if C2 == player and B2 == player and A2 == player:
        clickx = 0 #Reset click
        clicky = 0
        status = "won"
    if C3 == player and B3 == player and A3 == player:
        clickx = 0 #Reset click
        clicky = 0
        status = "won"
    #B
    if A1 == player and C3 == player and B1 == player:
        clickx = 0 #Reset click
        clicky = 0
        status = "won"
    if A2 == player and C2 == player and B2 == player:
        clickx = 0 #Reset click
        clicky = 0
        status = "won"
    if A3 == player and C3 == player and B3 == player:
        clickx = 0 #Reset click
        clicky = 0
        status = "won"
    #C
    if A1 == player and B1 == player and C1 == player:
        clickx = 0 #Reset click
        clicky = 0
        status = "won"
    if A2 == player and B2 == player and C2 == player:
        clickx = 0 #Reset click
        clicky = 0
        status = "won"
    if A3 == player and B3 == player and C3 == player:
        C3 = computer
        clickx = 0 #Reset click
        clicky = 0
        status = "won"

#Two diagonal
    #A1-C3
    if A1 == player and C3 == player and B2 == player:
        clickx = 0 #Reset click
        clicky = 0
        status = "won"
    #A3-C1
    if A3 == player and C1 == player and B2 == player:
        clickx = 0 #Reset click
        clicky = 0
        status = "won"
    #A1-B2
    if A1 == player and B2 == player and C3 == player:
        clickx = 0 #Reset click
        clicky = 0
        status = "won"
    #C1-B2
    if C1 == player and B2 == player and A3 == player:
        clickx = 0 #Reset click
        clicky = 0
        status = "won"
    #A3-B2
    if A3 == player and B2 == player and C1 == player:
        clickx = 0 #Reset click
        clicky = 0
        status = "won"
    #C3-B2
    if C3 == player and B2 == player and A1 == player:
        clickx = 0 #Reset click
        clicky = 0
        status = "won"
#End <<Win>>
            
        #Move choice to coordinate variables
    if playchoice == "A1" and A1 == "":
        A1 = player
    elif playchoice == "A2" and A2 == "":
        A2 = player
    elif playchoice == "A3" and A3 == "":
        A3 = player
    elif playchoice == "B1" and B1 == "":
        B1 = player
    elif playchoice == "B2" and B2 == "":
        B2 = player
    elif playchoice == "B3" and B3 == "":
        B3 = player
    elif playchoice == "C1" and C1 == "":
        C1= player
    elif playchoice == "C2" and C2 == "":
        C2 = player
    elif playchoice == "C3" and C3 == "":
        C3 = player
    else:
        turn = "player"
            
    #_____Computers turn_____

    comp_try = 0
    while turn == "comp" and comp_try < 10:
        compmove = random.randint(1,10)        
        comp_try = comp_try + 1

#<<Lose>>
#Two in a row
        #1
        if A2 == computer and A3 == computer and turn == "comp" and A1 == "":
            A1 = computer
            clickx = 0 #Reset click
            clicky = 0
            status = "lost"
            turn = "player"
        if B2 == computer and B3 == computer and turn == "comp" and B1 == "":
            B1 = computer
            clickx = 0 #Reset click
            clicky = 0
            status = "lost"
            turn = "player"
        if C2 == computer and C3 == computer and turn == "comp" and C1 == "":
            C1 = computer
            clickx = 0 #Reset click
            clicky = 0
            status = "lost"
            turn = "player"
        #2
        if A1 == computer and A3 == computer and turn == "comp" and A2 == "":
            A2 = computer
            clickx = 0 #Reset click
            clicky = 0
            status = "lost"
            turn = "player"
        if B1 == computer and B3 == computer and turn == "comp" and B2 == "":
            B2 = computer
            clickx = 0 #Reset click
            clicky = 0
            status = "lost"
            turn = "player"
        if C1 == computer and C3 == computer and turn == "comp" and C2 == "":
            C2 = computer
            clickx = 0 #Reset click
            clicky = 0
            status = "lost"
            turn = "player"
        #3
        if A1 == computer and A2 == computer and turn == "comp" and A3 == "":
            A3 = computer
            clickx = 0 #Reset click
            clicky = 0
            status = "lost"
            turn = "player"
        if B1 == computer and B2 == computer and turn == "comp" and B3 == "":
            B3 = computer
            clickx = 0 #Reset click
            clicky = 0
            status = "lost"
            turn = "player"
        if C1 == computer and C2 == computer and turn == "comp" and C3 == "":
            C3 = computer
            clickx = 0 #Reset click
            clicky = 0
            status = "lost"
            turn = "player"

#Two in a column
        #A
        if C1 == computer and B1 == computer and turn == "comp" and A1 == "":
            A1 = computer
            clickx = 0 #Reset click
            clicky = 0
            status = "lost"
            turn = "player"
        if C2 == computer and B2 == computer and turn == "comp" and A2 == "":
            A2 = computer
            clickx = 0 #Reset click
            clicky = 0
            status = "lost"
            turn = "player"
        if C3 == computer and B3 == computer and turn == "comp" and A3 == "":
            A3 = computer
            clickx = 0 #Reset click
            clicky = 0
            status = "lost"
            turn = "player"
        #B
        if A1 == computer and C3 == computer and turn == "comp" and B1 == "":
            B1 = computer
            clickx = 0 #Reset click
            clicky = 0
            status = "lost"
            turn = "player"
        if A2 == computer and C2 == computer and turn == "comp" and B2 == "":
            B2 = computer
            clickx = 0 #Reset click
            clicky = 0
            status = "lost"
            turn = "player"
        if A3 == computer and C3 == computer and turn == "comp" and B3 == "":
            B3 = computer
            clickx = 0 #Reset click
            clicky = 0
            status = "lost"
            turn = "player"
            #C
        if A1 == computer and B1 == computer and turn == "comp" and C1 == "":
            C1 = computer
            clickx = 0 #Reset click
            clicky = 0
            status = "lost"
            turn = "player"
        if A2 == computer and B2 == computer and turn == "comp" and C2 == "":
            C2 = computer
            clickx = 0 #Reset click
            clicky = 0
            status = "lost"
            turn = "player"
        if A3 == computer and B3 == computer and turn == "comp" and C3 == "":
            C3 = computer
            clickx = 0 #Reset click
            clicky = 0
            status = "lost"
            turn = "player"

#Two diagonal
        #A1-C3
        if A1 == computer and C1 == computer and turn == "comp" and B2 == "":
            B2 = computer
            clickx = 0 #Reset click
            clicky = 0
            status = "lost"
            turn = "player"
        #A3-C1
        if A3 == computer and C1 == computer and turn == "comp" and B2 == "":
            B2 = computer
            clickx = 0 #Reset click
            clicky = 0
            status = "lost"
            turn = "player"
        #A1-B2
        if A1 == computer and B2 == computer and turn == "comp" and C3 == "":
            C3 = computer
            clickx = 0 #Reset click
            clicky = 0
            status = "lost"
            turn = "player"
        #C1-B2
        if C1 == computer and B2 == computer and turn == "comp" and A3 == "":
            A3 = computer
            clickx = 0 #Reset click
            clicky = 0
            status = "lost"
            turn = "player"
        #A3-B2
        if A3 == computer and B2 == computer and turn == "comp" and C1 == "":
            C1 = computer
            clickx = 0 #Reset click
            clicky = 0
            status = "lost"
            turn = "player"
        #C3-B2
        if C3 == computer and B2 == computer and turn == "comp" and A1 == "":
            A1 = computer
            clickx = 0 #Reset click
            clicky = 0
            status = "lost"
            turn = "player"


#<<Stop player>>
#Two in a row
            #1
        if A2 == player and A3 == player and turn == "comp" and A1 == "":
            A1 = computer
            turn = "player"
        if B2 == player and B3 == player and turn == "comp" and B1 == "":
            B1 = computer
            turn = "player"
        if C2 == player and C3 == player and turn == "comp" and C1 == "":
            C1 = computer
            turn = "player"
            #2
        if A1 == player and A3 == player and turn == "comp" and A2 == "":
            A2 = computer
            turn = "player"
        if B1 == player and B3 == player and turn == "comp" and B2 == "":
            B2 = computer
            turn = "player"
        if C1 == player and C3 == player and turn == "comp" and C2 == "":
            C2 = computer
            turn = "player"
            #3
        if A1 == player and A2 == player and turn == "comp" and A3 == "":
            A3 = computer
            turn = "player"
        if B1 == player and B2 == player and turn == "comp" and B3 == "":
            B3 = computer
            turn = "player"
        if C1 == player and C2 == player and turn == "comp" and C3 == "":
            C3 = computer
            turn = "player"

#Two in a column
            #A
        if C1 == player and B1 == player and turn == "comp" and A1 == "":
            A1 = computer
            turn = "player"
        if C2 == player and B2 == player and turn == "comp" and A2 == "":
            A2 = computer
            turn = "player"
        if C3 == player and B3 == player and turn == "comp" and A3 == "":
            A3 = computer
            turn = "player"
            #B
        if A1 == player and C3 == player and turn == "comp" and B1 == "":
            B1 = computer
            turn = "player"
        if A2 == player and C2 == player and turn == "comp" and B2 == "":
            B2 = computer
            turn = "player"
        if A3 == player and C3 == player and turn == "comp" and B3 == "":
            B3 = computer
            turn = "player"
            #C
        if A1 == player and B1 == player and turn == "comp" and C1 == "":
            C1 = computer
            turn = "player"
        if A2 == player and B2 == player and turn == "comp" and C2 == "":
            C2 = computer
            turn = "player"
        if A3 == player and B3 == player and turn == "comp" and C3 == "":
            C3 = computer
            turn = "player"

#Two diagonal
            #A1-C3
        if A1 == player and C3 == player and turn == "comp" and B2 == "":
            B2 = computer
            turn = "player"
            #A3-C1
        if A3 == player and C1 == player and turn == "comp" and B2 == "":
            B2 = computer
            turn = "player"
            #A1-B2
        if A1 == player and B2 == player and turn == "comp" and C3 == "":
            C3 = computer
            turn = "player"
            #C1-B2
        if C1 == player and B2 == player and turn == "comp" and A3 == "":
            A3 = computer
            turn = "player"
            #A3-B2
        if A3 == player and B2 == player and turn == "comp" and C1 == "":
            C1 = computer
            turn = "player"
            #C3-B2
        if C3 == player and B2 == player and turn == "comp" and A1 == "":
            A1 = computer
            turn = "player"
            
            
#Random moves
        if compmove == 1 and A1 != player and A1 != computer and turn == "comp":
            A1 = computer
            turn = "player"
        elif compmove == 2 and A2 != player and A2 != computer and turn == "comp":
            A2 = computer
            turn = "player"
        elif compmove == 3 and A3 != player and A3 != computer and turn == "comp":
            A3 = computer
            turn = "player"
        elif compmove == 4 and B1 != player and B1 != computer and turn == "comp":
            B1 = computer
            turn = "player"
        elif compmove == 5 and B2 != player and B2 != computer and turn == "comp":
            B2 = computer
            turn = "player"
        elif compmove == 6 and B3 != player and B3 != computer and turn == "comp":
            B3 = computer
            turn = "player"
        elif compmove == 7 and C1 != player and C1 != computer and turn == "comp":
            C1 = computer
            turn = "player"
        elif compmove == 8 and C2 != player and C2 != computer and turn == "comp":
            C2 = computer
            turn = "player"
        elif compmove == 9 and C3 != player and C3 != computer and turn == "comp":
            C3 = computer
            turn = "player"

            
#-----Drawing code-----
    screen.fill(WHITE)

#Main Menu window
    if window == "main":
        titlefont = pygame.font.Font(None, 56)
        menufont = pygame.font.Font(None, 48)
        title = titlefont.render("Welcome to Daniel's Tic Tac Toe",True,BLACK)
        screen.blit(title, [175,50])
        #New game Button
        newgame = menufont.render("New Game",True,BLACK)
        screen.blit(newgame, [365,185])
        pygame.draw.rect(screen,BLACK,[250,150,400,100],2)
        #Quit Button
        quitgame = menufont.render("Quit Game",True,BLACK)
        screen.blit(quitgame, [365,335])
        pygame.draw.rect(screen,BLACK,[250,300,400,100],2)

#Symbol choice Menu window
    if window == "choice":
        titlefont = pygame.font.Font(None, 56)
        title = titlefont.render("Choose your symbol...",True,BLACK)
        screen.blit(title, [235,100])
        #Choice X
        pygame.draw.rect(screen, BLACK, [175,275,150,150],2)
        pygame.draw.line(screen, BLACK, [200,300], [300,400], 5)
        pygame.draw.line(screen, BLACK, [300,300], [200,400], 5)
        #Choice O
        pygame.draw.rect(screen, BLACK, [575,275,150,150],2)
        pygame.draw.ellipse(screen,RED,[600,300,100,100],4)

#Win Menu window
    if window == "win":
        pygame.time.delay(1000)
        titlefont = pygame.font.Font(None, 56)
        menufont = pygame.font.Font(None, 48)
        title = titlefont.render("You Won!",True,BLUE)
        screen.blit(title, [175,100])
        #Play Again Button
        newgame = menufont.render("Play Again",True,BLACK)
        screen.blit(newgame, [365,285])
        pygame.draw.rect(screen,BLACK,[250,250,400,100],2)
        #Quit Button
        quitgame = menufont.render("Quit Game",True,BLACK)
        screen.blit(quitgame, [365,435])
        pygame.draw.rect(screen,BLACK,[250,400,400,100],2)
        
#Lose Menu window
    if window == "lose":
        pygame.time.delay(1000)
        titlefont = pygame.font.Font(None, 56)
        menufont = pygame.font.Font(None, 48)
        title = titlefont.render("You lost...",True,RED)
        screen.blit(title, [175,100])
        #Play Again Button
        newgame = menufont.render("Play Again",True,BLACK)
        screen.blit(newgame, [365,285])
        pygame.draw.rect(screen,BLACK,[250,250,400,100],2)
        #Quit Button
        quitgame = menufont.render("Quit Game",True,BLACK)
        screen.blit(quitgame, [365,435])
        pygame.draw.rect(screen,BLACK,[250,400,400,100],2)
        
#Cat's Game Menu window
    if window == "cats":
        pygame.time.delay(1000)
        titlefont = pygame.font.Font(None, 56)
        menufont = pygame.font.Font(None, 48)
        title = titlefont.render("Cat's Game!",True,GREEN)
        screen.blit(title, [175,100])
        #Play Again Button
        newgame = menufont.render("Play Again",True,BLACK)
        screen.blit(newgame, [365,285])
        pygame.draw.rect(screen,BLACK,[250,250,400,100],2)
        #Quit Button
        quitgame = menufont.render("Quit Game",True,BLACK)
        screen.blit(quitgame, [365,435])
        pygame.draw.rect(screen,BLACK,[250,400,400,100],2)
        
    if window == "game":
        gamefont = pygame.font.Font(None, 48)
        game_text = gamefont.render("Player is: " + player,True,BLACK)
        screen.blit(game_text, [350,5])
        turn_text = gamefont.render("It's your turn...",True,BLACK)
        screen.blit(turn_text, [350,655])


        
        pygame.draw.line(screen, BLACK, [150,250], [750,250], 5)
        pygame.draw.line(screen, BLACK, [150,450], [750,450], 5)
        pygame.draw.line(screen, BLACK, [350,50], [350,650], 5)
        pygame.draw.line(screen, BLACK, [550,50], [550,650], 5)
    
        if A1 == "X":
            pygame.draw.line(screen, BLACK, [200,100], [300,200], 5)
            pygame.draw.line(screen, BLACK, [300,100], [200,200], 5)
        if A2 == "X":
            pygame.draw.line(screen, BLACK, [400,100], [500,200], 5)
            pygame.draw.line(screen, BLACK, [500,100], [400,200], 5)
        if A3 == "X":
            pygame.draw.line(screen, BLACK, [600,100], [700,200], 5)
            pygame.draw.line(screen, BLACK, [700,100], [600,200], 5)
        if B1 == "X":
            pygame.draw.line(screen, BLACK, [200,300], [300,400], 5)
            pygame.draw.line(screen, BLACK, [300,300], [200,400], 5)
        if B2 == "X":
            pygame.draw.line(screen, BLACK, [400,300], [500,400], 5)
            pygame.draw.line(screen, BLACK, [500,300], [400,400], 5)
        if B3 == "X":
            pygame.draw.line(screen, BLACK, [600,300], [700,400], 5)
            pygame.draw.line(screen, BLACK, [700,300], [600,400], 5)
        if C1 == "X":
            pygame.draw.line(screen, BLACK, [200,500], [300,600], 5)
            pygame.draw.line(screen, BLACK, [300,500], [200,600], 5)
        if C2 == "X":
            pygame.draw.line(screen, BLACK, [400,500], [500,600], 5)
            pygame.draw.line(screen, BLACK, [500,500], [400,600], 5)
        if C3 == "X":
            pygame.draw.line(screen, BLACK, [600,500], [700,600], 5)
            pygame.draw.line(screen, BLACK, [700,500], [600,600], 5)
 
        if A1 == "O":
            pygame.draw.ellipse(screen,RED,[200,100,100,100],4)
        if A2 == "O":
            pygame.draw.ellipse(screen,RED,[400,100,100,100],4)
        if A3 == "O":
            pygame.draw.ellipse(screen,RED,[600,100,100,100],4)
        if B1 == "O":
            pygame.draw.ellipse(screen,RED,[200,300,100,100],4)
        if B2 == "O":
            pygame.draw.ellipse(screen,RED,[400,300,100,100],4)
        if B3 == "O":
            pygame.draw.ellipse(screen,RED,[600,300,100,100],4)
        if C1 == "O":
            pygame.draw.ellipse(screen,RED,[200,500,100,100],4)
        if C2 == "O":
            pygame.draw.ellipse(screen,RED,[400,500,100,100],4)
        if C3 == "O":
            pygame.draw.ellipse(screen,RED,[600,500,100,100],4)
    #To show last move
        if status == "lost":
            window = "lose"
            status = "" #Reset status
        if status == "won":
            window = "win"
            status = "" #Reset status
    
# --- Add drawings to screen output
    pygame.display.flip()

# --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
