import pygame
import random

done = False

clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Game:

    def __init__(self):
        self.window = "main"
        self.player = "X"
        self.computer = "O"
        self.compmove = 0
        self.turn = "player"
        self.status = "" #to show last move
        self.clickx = 0
        self.clicky = 0
        self.playchoice = ""
        self.A1 = ""
        self.A2 = ""
        self.A3 = ""
        self.B1 = ""
        self.B2 = ""
        self.B3 = ""
        self.C1 = ""
        self.C2 = ""
        self.C3 = ""

        pygame.init()

        size = (900, 700)
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Tic Tac Toe")

    def run(self):
        while not done:
            self.event_loop()
        pygame.quit()

    def event_loop(self):
        global done
        global clock
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                self.clickx = pos[0]
                self.clicky = pos[1]
                if self.window == "game":
                    self.turn = "comp"

        #Main Menu Logic
        if self.window == "main":
            if (self.clickx >= 250 and self.clickx <= 650) and (self.clicky >= 150 and self.clicky <= 250):
                self.window = "choice"
                self.reset_clicks()
            if (self.clickx >= 250 and self.clickx <= 650) and (self.clicky >= 300 and self.clicky <= 400):
                done = True

        #Symbol choice Menu Logic
        if self.window == "choice":
            if (self.clickx >= 200 and self.clickx <= 300) and (self.clicky >= 300 and self.clicky <= 400):
                self.player = "X"
                self.computer =  "O"
                self.window = "game"
                self.reset_clicks()
            if (self.clickx >= 600 and self.clickx <= 700) and (self.clicky >= 300 and self.clicky <= 400):
                self.player = "O"
                self.computer = "X"
                self.window = "game"
                self.reset_clicks()

        #Win Menu Logic
        if self.window == "win":
            if (self.clickx >= 250 and self.clickx <= 650) and (self.clicky >= 250 and self.clicky <= 350):
                self.window = "choice"
                self.reset_clicks()
                self.A1 = ""
                self.A2 = ""
                self.A3 = ""
                self.B1 = ""
                self.B2 = ""
                self.B3 = ""
                self.C1 = ""
                self.C2 = ""
                self.C3 = ""
                self.turn = "player"
                self.playchoice = ""
            if (self.clickx >= 250 and self.clickx <= 650) and (self.clicky >= 400 and self.clicky <= 500):
                done = True

        #Lose Menu Logic
        if self.window == "lose":
            if (self.clickx >= 250 and self.clickx <= 650) and (self.clicky >= 250 and self.clicky <= 350):
                self.window = "choice"
                self.reset_clicks()
                self.A1 = ""
                self.A2 = ""
                self.A3 = ""
                self.B1 = ""
                self.B2 = ""
                self.B3 = ""
                self.C1 = ""
                self.C2 = ""
                self.C3 = ""
                self.turn = "player"
                self.playchoice = ""
            if (self.clickx >= 250 and self.clickx <= 650) and (self.clicky >= 400 and self.clicky <= 500):
                done = True

        #Cat's Game Menu Logic
        if self.window == "cats":
            if (self.clickx >= 250 and self.clickx <= 650) and (self.clicky >= 250 and self.clicky <= 350):
                self.window = "game"
                self.reset_clicks()
                self.A1 = ""
                self.A2 = ""
                self.A3 = ""
                self.B1 = ""
                self.B2 = ""
                self.B3 = ""
                self.C1 = ""
                self.C2 = ""
                self.C3 = ""
                self.turn = "player"
                self.playchoice = ""
            if (self.clickx >= 250 and self.clickx <= 650) and (self.clicky >= 400 and self.clicky <= 500):
                done = True

        #Get players choice
        if self.window == "game":
            if (self.clickx > 150 and self.clickx < 350) and (self.clicky > 50 and self.clicky < 250):
                self.playchoice = "A1"
            if (self.clickx > 350 and self.clickx < 550) and (self.clicky > 50 and self.clicky < 250):
                self.playchoice = "A2"
            if (self.clickx > 550 and self.clickx < 750) and (self.clicky > 50 and self.clicky < 250):
                self.playchoice = "A3"
            if (self.clickx > 150 and self.clickx < 350) and (self.clicky > 250 and self.clicky < 450):
                self.playchoice = "B1"
            if (self.clickx > 350 and self.clickx < 550) and (self.clicky > 250 and self.clicky < 450):
                self.playchoice = "B2"
            if (self.clickx > 550 and self.clickx < 750) and (self.clicky > 250 and self.clicky < 450):
                self.playchoice = "B3"
            if (self.clickx > 150 and self.clickx < 350) and (self.clicky > 450 and self.clicky < 650):
                self.playchoice = "C1"
            if (self.clickx > 350 and self.clickx < 550) and (self.clicky > 450 and self.clicky < 650):
                self.playchoice = "C2"
            if (self.clickx > 550 and self.clickx < 750) and (self.clicky > 450 and self.clicky < 650):
                self.playchoice = "C3"

        #<<Cats>>
        if self.status != "won" and self.status != "lost" and self.A1 != "" and self.A2 != "" and self.A3 != "" and self.B1 != "" and self.B2 != "" and self.B3 != "" and self.C1 != "" and self.C2 != "" and self.C3 != "":
            self.reset_clicks()
            self.window = "cats"

        #<<Win>>
        #Two in a row
        #1
        if self.A2 == self.player and self.A3 == self.player and self.A1 == self.player:
            self.reset_clicks()
            self.status = "won"
        if self.B2 == self.player and self.B3 == self.player and self.B1 == self.player:
            self.reset_clicks()
            self.status = "won"
        if self.C2 == self.player and self.C3 == self.player and self.C1 == self.player:
            self.reset_clicks()
            self.status = "won"
        #2
        if self.A1 == self.player and self.A3 == self.player and self.A2 == self.player:
            self.reset_clicks()
            self.status = "won"
        if self.B1 == self.player and self.B3 == self.player and self.B2 == self.player:
            self.reset_clicks()
            self.status = "won"
        if self.C1 == self.player and self.C3 == self.player and self.C2 == self.player:
            self.reset_clicks()
            self.status = "won"
        #3
        if self.A1 == self.player and self.A2 == self.player and self.A3 == self.player:
            self.reset_clicks()
            self.status = "won"
        if self.B1 == self.player and self.B2 == self.player and self.B3 == self.player:
            self.reset_clicks()
            self.status = "won"
        if self.C1 == self.player and self.C2 == self.player and self.C3 == self.player:
            self.reset_clicks()
            self.status = "won"

        #Two in a column
        #A
        if self.C1 == self.player and self.B1 == self.player and self.A1 == self.player:
            self.reset_clicks()
            self.status = "won"
        if self.C2 == self.player and self.B2 == self.player and self.A2 == self.player:
            self.reset_clicks()
            self.status = "won"
        if self.C3 == self.player and self.B3 == self.player and self.A3 == self.player:
            self.reset_clicks()
            self.status = "won"
        #B
        if self.A1 == self.player and self.C3 == self.player and self.B1 == self.player:
            self.reset_clicks()
            self.status = "won"
        if self.A2 == self.player and self.C2 == self.player and self.B2 == self.player:
            self.reset_clicks()
            self.status = "won"
        if self.A3 == self.player and self.C3 == self.player and self.B3 == self.player:
            self.reset_clicks()
            self.status = "won"
        #C
        if self.A1 == self.player and self.B1 == self.player and self.C1 == self.player:
            self.reset_clicks()
            self.status = "won"
        if self.A2 == self.player and self.B2 == self.player and self.C2 == self.player:
            self.reset_clicks()
            self.status = "won"
        if self.A3 == self.player and self.B3 == self.player and self.C3 == self.player:
            self.C3 = self.computer
            self.reset_clicks()
            self.status = "won"

        #Two diagonal
        #A1-C3
        if self.A1 == self.player and self.C3 == self.player and self.B2 == self.player:
            self.reset_clicks()
            self.status = "won"
        #A3-C1
        if self.A3 == self.player and self.C1 == self.player and self.B2 == self.player:
            self.reset_clicks()
            self.status = "won"
        #A1-B2
        if self.A1 == self.player and self.B2 == self.player and self.C3 == self.player:
            self.reset_clicks()
            self.status = "won"
        #C1-B2
        if self.C1 == self.player and self.B2 == self.player and self.A3 == self.player:
            self.reset_clicks()
            self.status = "won"
        #A3-B2
        if self.A3 == self.player and self.B2 == self.player and self.C1 == self.player:
            self.reset_clicks()
            self.status = "won"
        #C3-B2
        if self.C3 == self.player and self.B2 == self.player and self.A1 == self.player:
            self.reset_clicks()
            self.status = "won"
        #End <<Win>>

        #Move choice to coordinate variables
        if self.playchoice == "A1" and self.A1 == "":
            self.A1 = self.player
        elif self.playchoice == "A2" and self.A2 == "":
            self.A2 = self.player
        elif self.playchoice == "A3" and self.A3 == "":
            self.A3 = self.player
        elif self.playchoice == "B1" and self.B1 == "":
            self.B1 = self.player
        elif self.playchoice == "B2" and self.B2 == "":
            self.B2 = self.player
        elif self.playchoice == "B3" and self.B3 == "":
            self.B3 = self.player
        elif self.playchoice == "C1" and self.C1 == "":
            self.C1= self.player
        elif self.playchoice == "C2" and self.C2 == "":
            self.C2 = self.player
        elif self.playchoice == "C3" and self.C3 == "":
            self.C3 = self.player
        else:
            self.turn = "player"

        # Computers turn
        comp_try = 0
        while self.turn == "comp" and comp_try < 10:
            self.compmove = random.randint(1,10)
            comp_try = comp_try + 1

            #<<Lose>>
            #Two in a row
            #1
            if self.A2 == self.computer and self.A3 == self.computer and self.turn == "comp" and self.A1 == "":
                self.A1 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            if self.B2 == self.computer and self.B3 == self.computer and self.turn == "comp" and self.B1 == "":
                self.B1 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            if self.C2 == self.computer and self.C3 == self.computer and self.turn == "comp" and self.C1 == "":
                self.C1 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            #2
            if self.A1 == self.computer and self.A3 == self.computer and self.turn == "comp" and self.A2 == "":
                self.A2 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            if self.B1 == self.computer and self.B3 == self.computer and self.turn == "comp" and self.B2 == "":
                self.B2 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            if self.C1 == self.computer and self.C3 == self.computer and self.turn == "comp" and self.C2 == "":
                self.C2 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            #3
            if self.A1 == self.computer and self.A2 == self.computer and self.turn == "comp" and self.A3 == "":
                self.A3 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            if self.B1 == self.computer and self.B2 == self.computer and self.turn == "comp" and self.B3 == "":
                self.B3 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            if self.C1 == self.computer and self.C2 == self.computer and self.turn == "comp" and self.C3 == "":
                self.C3 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"

            #Two in a column
            #A
            if self.C1 == self.computer and self.B1 == self.computer and self.turn == "comp" and self.A1 == "":
                self.A1 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            if self.C2 == self.computer and self.B2 == self.computer and self.turn == "comp" and self.A2 == "":
                self.A2 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            if self.C3 == self.computer and self.B3 == self.computer and self.turn == "comp" and self.A3 == "":
                self.A3 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            #B
            if self.A1 == self.computer and self.C3 == self.computer and self.turn == "comp" and self.B1 == "":
                self.B1 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            if self.A2 == self.computer and self.C2 == self.computer and self.turn == "comp" and self.B2 == "":
                self.B2 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            if self.A3 == self.computer and self.C3 == self.computer and self.turn == "comp" and self.B3 == "":
                self.B3 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
                #C
            if self.A1 == self.computer and self.B1 == self.computer and self.turn == "comp" and self.C1 == "":
                self.C1 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            if self.A2 == self.computer and self.B2 == self.computer and self.turn == "comp" and self.C2 == "":
                self.C2 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            if self.A3 == self.computer and self.B3 == self.computer and self.turn == "comp" and self.C3 == "":
                self.C3 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"

            #Two diagonal
            #A1-C3
            if self.A1 == self.computer and self.C1 == self.computer and self.turn == "comp" and self.B2 == "":
                self.B2 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            #A3-C1
            if self.A3 == self.computer and self.C1 == self.computer and self.turn == "comp" and self.B2 == "":
                self.B2 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            #A1-B2
            if self.A1 == self.computer and self.B2 == self.computer and self.turn == "comp" and self.C3 == "":
                self.C3 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            #C1-B2
            if self.C1 == self.computer and self.B2 == self.computer and self.turn == "comp" and self.A3 == "":
                self.A3 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            #A3-B2
            if self.A3 == self.computer and self.B2 == self.computer and self.turn == "comp" and self.C1 == "":
                self.C1 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            #C3-B2
            if self.C3 == self.computer and self.B2 == self.computer and self.turn == "comp" and self.A1 == "":
                self.A1 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"

            #<<Stop player>>
            #Two in a row
            #1
            if self.A2 == self.player and self.A3 == self.player and self.turn == "comp" and self.A1 == "":
                self.A1 = self.computer
                self.turn = "player"
            if self.B2 == self.player and self.B3 == self.player and self.turn == "comp" and self.B1 == "":
                self.B1 = self.computer
                self.turn = "player"
            if self.C2 == self.player and self.C3 == self.player and self.turn == "comp" and self.C1 == "":
                self.C1 = self.computer
                self.turn = "player"
            #2
            if self.A1 == self.player and self.A3 == self.player and self.turn == "comp" and self.A2 == "":
                self.A2 = self.computer
                self.turn = "player"
            if self.B1 == self.player and self.B3 == self.player and self.turn == "comp" and self.B2 == "":
                self.B2 = self.computer
                self.turn = "player"
            if self.C1 == self.player and self.C3 == self.player and self.turn == "comp" and self.C2 == "":
                self.C2 = self.computer
                self.turn = "player"
            #3
            if self.A1 == self.player and self.A2 == self.player and self.turn == "comp" and self.A3 == "":
                self.A3 = self.computer
                self.turn = "player"
            if self.B1 == self.player and self.B2 == self.player and self.turn == "comp" and self.B3 == "":
                self.B3 = self.computer
                self.turn = "player"
            if self.C1 == self.player and self.C2 == self.player and self.turn == "comp" and self.C3 == "":
                self.C3 = self.computer
                self.turn = "player"

            #Two in a column
            #A
            if self.C1 == self.player and self.B1 == self.player and self.turn == "comp" and self.A1 == "":
                self.A1 = self.computer
                self.turn = "player"
            if self.C2 == self.player and self.B2 == self.player and self.turn == "comp" and self.A2 == "":
                self.A2 = self.computer
                self.turn = "player"
            if self.C3 == self.player and self.B3 == self.player and self.turn == "comp" and self.A3 == "":
                self.A3 = self.computer
                self.turn = "player"
            #B
            if self.A1 == self.player and self.C3 == self.player and self.turn == "comp" and self.B1 == "":
                self.B1 = self.computer
                self.turn = "player"
            if self.A2 == self.player and self.C2 == self.player and self.turn == "comp" and self.B2 == "":
                self.B2 = self.computer
                self.turn = "player"
            if self.A3 == self.player and self.C3 == self.player and self.turn == "comp" and self.B3 == "":
                self.B3 = self.computer
                self.turn = "player"
            #C
            if self.A1 == self.player and self.B1 == self.player and self.turn == "comp" and self.C1 == "":
                self.C1 = self.computer
                self.turn = "player"
            if self.A2 == self.player and self.B2 == self.player and self.turn == "comp" and self.C2 == "":
                self.C2 = self.computer
                self.turn = "player"
            if self.A3 == self.player and self.B3 == self.player and self.turn == "comp" and self.C3 == "":
                self.C3 = self.computer
                self.turn = "player"

            #Two diagonal
            #A1-C3
            if self.A1 == self.player and self.C3 == self.player and self.turn == "comp" and self.B2 == "":
                self.B2 = self.computer
                self.turn = "player"
            #A3-C1
            if self.A3 == self.player and self.C1 == self.player and self.turn == "comp" and self.B2 == "":
                self.B2 = self.computer
                self.turn = "player"
            #A1-B2
            if self.A1 == self.player and self.B2 == self.player and self.turn == "comp" and self.C3 == "":
                self.C3 = self.computer
                self.turn = "player"
            #C1-B2
            if self.C1 == self.player and self.B2 == self.player and self.turn == "comp" and self.A3 == "":
                self.A3 = self.computer
                self.turn = "player"
            #A3-B2
            if self.A3 == self.player and self.B2 == self.player and self.turn == "comp" and self.C1 == "":
                self.C1 = self.computer
                self.turn = "player"
            #C3-B2
            if self.C3 == self.player and self.B2 == self.player and self.turn == "comp" and self.A1 == "":
                self.A1 = self.computer
                self.turn = "player"

            #Random moves
            if self.compmove == 1 and self.A1 != self.player and self.A1 != self.computer and self.turn == "comp":
                self.A1 = self.computer
                self.turn = "player"
            elif self.compmove == 2 and self.A2 != self.player and self.A2 != self.computer and self.turn == "comp":
                self.A2 = self.computer
                self.turn = "player"
            elif self.compmove == 3 and self.A3 != self.player and self.A3 != self.computer and self.turn == "comp":
                self.A3 = self.computer
                self.turn = "player"
            elif self.compmove == 4 and self.B1 != self.player and self.B1 != self.computer and self.turn == "comp":
                self.B1 = self.computer
                self.turn = "player"
            elif self.compmove == 5 and self.B2 != self.player and self.B2 != self.computer and self.turn == "comp":
                self.B2 = self.computer
                self.turn = "player"
            elif self.compmove == 6 and self.B3 != self.player and self.B3 != self.computer and self.turn == "comp":
                self.B3 = self.computer
                self.turn = "player"
            elif self.compmove == 7 and self.C1 != self.player and self.C1 != self.computer and self.turn == "comp":
                self.C1 = self.computer
                self.turn = "player"
            elif self.compmove == 8 and self.C2 != self.player and self.C2 != self.computer and self.turn == "comp":
                self.C2 = self.computer
                self.turn = "player"
            elif self.compmove == 9 and self.C3 != self.player and self.C3 != self.computer and self.turn == "comp":
                self.C3 = self.computer
                self.turn = "player"

        #Drawing code
        self.screen.fill(WHITE)

        #Main Menu window
        if self.window == "main":
            titlefont = pygame.font.Font(None, 56)
            menufont = pygame.font.Font(None, 48)
            title = titlefont.render("Welcome to Daniel's Tic Tac Toe",True,BLACK)
            self.screen.blit(title, [175,50])
            #New game Button
            newgame = menufont.render("New Game",True,BLACK)
            self.screen.blit(newgame, [365,185])
            pygame.draw.rect(self.screen,BLACK,[250,150,400,100],2)
            #Quit Button
            quitgame = menufont.render("Quit Game",True,BLACK)
            self.screen.blit(quitgame, [365,335])
            pygame.draw.rect(self.screen,BLACK,[250,300,400,100],2)

        #Symbol choice Menu window
        if self.window == "choice":
            titlefont = pygame.font.Font(None, 56)
            title = titlefont.render("Choose your symbol...",True,BLACK)
            self.screen.blit(title, [235,100])
            #Choice X
            pygame.draw.rect(self.screen, BLACK, [175,275,150,150],2)
            pygame.draw.line(self.screen, BLACK, [200,300], [300,400], 5)
            pygame.draw.line(self.screen, BLACK, [300,300], [200,400], 5)
            #Choice O
            pygame.draw.rect(self.screen, BLACK, [575,275,150,150],2)
            pygame.draw.ellipse(self.screen,RED,[600,300,100,100],4)

        #Win Menu window
        if self.window == "win":
            pygame.time.delay(1000)
            titlefont = pygame.font.Font(None, 56)
            menufont = pygame.font.Font(None, 48)
            title = titlefont.render("You Won!",True,BLUE)
            self.screen.blit(title, [175,100])
            #Play Again Button
            newgame = menufont.render("Play Again",True,BLACK)
            self.screen.blit(newgame, [365,285])
            pygame.draw.rect(self.screen,BLACK,[250,250,400,100],2)
            #Quit Button
            quitgame = menufont.render("Quit Game",True,BLACK)
            self.screen.blit(quitgame, [365,435])
            pygame.draw.rect(self.screen,BLACK,[250,400,400,100],2)

        #Lose Menu window
        if self.window == "lose":
            pygame.time.delay(1000)
            titlefont = pygame.font.Font(None, 56)
            menufont = pygame.font.Font(None, 48)
            title = titlefont.render("You lost...",True,RED)
            self.screen.blit(title, [175,100])
            #Play Again Button
            newgame = menufont.render("Play Again",True,BLACK)
            self.screen.blit(newgame, [365,285])
            pygame.draw.rect(self.screen,BLACK,[250,250,400,100],2)
            #Quit Button
            quitgame = menufont.render("Quit Game",True,BLACK)
            self.screen.blit(quitgame, [365,435])
            pygame.draw.rect(self.screen,BLACK,[250,400,400,100],2)

        #Cat's Game Menu window
        if self.window == "cats":
            pygame.time.delay(1000)
            titlefont = pygame.font.Font(None, 56)
            menufont = pygame.font.Font(None, 48)
            title = titlefont.render("Cat's Game!",True,GREEN)
            self.screen.blit(title, [175,100])
            #Play Again Button
            newgame = menufont.render("Play Again",True,BLACK)
            self.screen.blit(newgame, [365,285])
            pygame.draw.rect(self.screen,BLACK,[250,250,400,100],2)
            #Quit Button
            quitgame = menufont.render("Quit Game",True,BLACK)
            self.screen.blit(quitgame, [365,435])
            pygame.draw.rect(self.screen,BLACK,[250,400,400,100],2)

        if self.window == "game":
            gamefont = pygame.font.Font(None, 48)
            game_text = gamefont.render("Player is: " + self.player,True,BLACK)
            self.screen.blit(game_text, [350,5])
            turn_text = gamefont.render("It's your turn...",True,BLACK)
            self.screen.blit(turn_text, [350,655])

            pygame.draw.line(self.screen, BLACK, [150,250], [750,250], 5)
            pygame.draw.line(self.screen, BLACK, [150,450], [750,450], 5)
            pygame.draw.line(self.screen, BLACK, [350,50], [350,650], 5)
            pygame.draw.line(self.screen, BLACK, [550,50], [550,650], 5)

            if self.A1 == "X":
                pygame.draw.line(self.screen, BLACK, [200,100], [300,200], 5)
                pygame.draw.line(self.screen, BLACK, [300,100], [200,200], 5)
            if self.A2 == "X":
                pygame.draw.line(self.screen, BLACK, [400,100], [500,200], 5)
                pygame.draw.line(self.screen, BLACK, [500,100], [400,200], 5)
            if self.A3 == "X":
                pygame.draw.line(self.screen, BLACK, [600,100], [700,200], 5)
                pygame.draw.line(self.screen, BLACK, [700,100], [600,200], 5)
            if self.B1 == "X":
                pygame.draw.line(self.screen, BLACK, [200,300], [300,400], 5)
                pygame.draw.line(self.screen, BLACK, [300,300], [200,400], 5)
            if self.B2 == "X":
                pygame.draw.line(self.screen, BLACK, [400,300], [500,400], 5)
                pygame.draw.line(self.screen, BLACK, [500,300], [400,400], 5)
            if self.B3 == "X":
                pygame.draw.line(self.screen, BLACK, [600,300], [700,400], 5)
                pygame.draw.line(self.screen, BLACK, [700,300], [600,400], 5)
            if self.C1 == "X":
                pygame.draw.line(self.screen, BLACK, [200,500], [300,600], 5)
                pygame.draw.line(self.screen, BLACK, [300,500], [200,600], 5)
            if self.C2 == "X":
                pygame.draw.line(self.screen, BLACK, [400,500], [500,600], 5)
                pygame.draw.line(self.screen, BLACK, [500,500], [400,600], 5)
            if self.C3 == "X":
                pygame.draw.line(self.screen, BLACK, [600,500], [700,600], 5)
                pygame.draw.line(self.screen, BLACK, [700,500], [600,600], 5)

            if self.A1 == "O":
                pygame.draw.ellipse(self.screen,RED,[200,100,100,100],4)
            if self.A2 == "O":
                pygame.draw.ellipse(self.screen,RED,[400,100,100,100],4)
            if self.A3 == "O":
                pygame.draw.ellipse(self.screen,RED,[600,100,100,100],4)
            if self.B1 == "O":
                pygame.draw.ellipse(self.screen,RED,[200,300,100,100],4)
            if self.B2 == "O":
                pygame.draw.ellipse(self.screen,RED,[400,300,100,100],4)
            if self.B3 == "O":
                pygame.draw.ellipse(self.screen,RED,[600,300,100,100],4)
            if self.C1 == "O":
                pygame.draw.ellipse(self.screen,RED,[200,500,100,100],4)
            if self.C2 == "O":
                pygame.draw.ellipse(self.screen,RED,[400,500,100,100],4)
            if self.C3 == "O":
                pygame.draw.ellipse(self.screen,RED,[600,500,100,100],4)

            if self.status == "lost":
                self.window = "lose"
                self.status = ""
            if self.status == "won":
                self.window = "win"
                self.status = ""

        pygame.display.flip()

        clock.tick(60)

    def reset_clicks(self):
        self.clickx = 0
        self.clicky = 0

game = Game()
game.run()
