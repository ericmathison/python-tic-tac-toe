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
        self.status = ""
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
            if (250 <= self.clickx <= 650) and (150 <= self.clicky <= 250):
                self.window = "choice"
                self.reset_clicks()
            if (250 <= self.clickx <= 650) and (300 <= self.clicky <= 400):
                done = True

        #Symbol choice Menu Logic
        if self.window == "choice":
            if (200 <= self.clickx <= 300) and (300 <= self.clicky <= 400):
                self.player = "X"
                self.computer =  "O"
                self.window = "game"
                self.reset_clicks()
            if (600 <= self.clickx <= 700) and (300 <= self.clicky <= 400):
                self.player = "O"
                self.computer = "X"
                self.window = "game"
                self.reset_clicks()

        #Win Menu Logic
        if self.window == "win" or self.window == "lose" or self.window == "cats":
            self.process_post_game_menu()

        if self.window == "game":
            self.set_players_choice()

        #<<Cats>>
        if self.status != "won" and self.status != "lost" and self.A1 != "" and self.A2 != "" and self.A3 != "" and self.B1 != "" and self.B2 != "" and self.B3 != "" and self.C1 != "" and self.C2 != "" and self.C3 != "":
            self.reset_clicks()
            self.window = "cats"

        #<<Win>>
        #Two in a row
        #1
        if self.A2 == self.A3 == self.A1 == self.player:
            self.reset_clicks()
            self.status = "won"
        if self.B2 == self.B3 == self.B1 == self.player:
            self.reset_clicks()
            self.status = "won"
        if self.C2 == self.C3 == self.C1 == self.player:
            self.reset_clicks()
            self.status = "won"
        #2
        if self.A1 == self.A3 == self.A2 == self.player:
            self.reset_clicks()
            self.status = "won"
        if self.B1 == self.B3 == self.B2 == self.player:
            self.reset_clicks()
            self.status = "won"
        if self.C1 == self.C3 == self.C2 == self.player:
            self.reset_clicks()
            self.status = "won"
        #3
        if self.A1 == self.A2 == self.A3 == self.player:
            self.reset_clicks()
            self.status = "won"
        if self.B1 == self.B2 == self.B3 == self.player:
            self.reset_clicks()
            self.status = "won"
        if self.C1 == self.C2 == self.C3 == self.player:
            self.reset_clicks()
            self.status = "won"

        #Two in a column
        #A
        if self.C1 == self.B1 == self.A1 == self.player:
            self.reset_clicks()
            self.status = "won"
        if self.C2 == self.B2 == self.A2 == self.player:
            self.reset_clicks()
            self.status = "won"
        if self.C3 == self.B3 == self.A3 == self.player:
            self.reset_clicks()
            self.status = "won"
        #B
        if self.A1 == self.C3 == self.B1 == self.player:
            self.reset_clicks()
            self.status = "won"
        if self.A2 == self.C2 == self.B2 == self.player:
            self.reset_clicks()
            self.status = "won"
        if self.A3 == self.C3 == self.B3 == self.player:
            self.reset_clicks()
            self.status = "won"
        #C
        if self.A1 == self.B1 == self.C1 == self.player:
            self.reset_clicks()
            self.status = "won"
        if self.A2 == self.B2 == self.C2 == self.player:
            self.reset_clicks()
            self.status = "won"
        if self.A3 == self.B3 == self.C3 == self.player:
            self.C3 = self.computer
            self.reset_clicks()
            self.status = "won"

        #Two diagonal
        #A1-C3
        if self.A1 == self.C3 == self.B2 == self.player:
            self.reset_clicks()
            self.status = "won"
        #A3-C1
        if self.A3 == self.C1 == self.B2 == self.player:
            self.reset_clicks()
            self.status = "won"
        #A1-B2
        if self.A1 == self.B2 == self.C3 == self.player:
            self.reset_clicks()
            self.status = "won"
        #C1-B2
        if self.C1 == self.B2 == self.A3 == self.player:
            self.reset_clicks()
            self.status = "won"
        #A3-B2
        if self.A3 == self.B2 == self.C1 == self.player:
            self.reset_clicks()
            self.status = "won"
        #C3-B2
        if self.C3 == self.B2 == self.A1 == self.player:
            self.reset_clicks()
            self.status = "won"
        #End <<Win>>

        setattr(self, self.playchoice, self.player)

        # Computers turn
        comp_try = 0
        while self.turn == "comp" and comp_try < 10:
            self.compmove = random.randint(1,10)
            comp_try = comp_try + 1

            #<<Lose>>
            #Two in a row
            #1
            if self.A2 == self.A3 == self.computer and self.turn == "comp" and self.A1 == "":
                self.A1 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            if self.B2 == self.B3 == self.computer and self.turn == "comp" and self.B1 == "":
                self.B1 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            if self.C2 == self.C3 == self.computer and self.turn == "comp" and self.C1 == "":
                self.C1 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            #2
            if self.A1 == self.A3 == self.computer and self.turn == "comp" and self.A2 == "":
                self.A2 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            if self.B1 == self.B3 == self.computer and self.turn == "comp" and self.B2 == "":
                self.B2 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            if self.C1 == self.C3 == self.computer and self.turn == "comp" and self.C2 == "":
                self.C2 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            #3
            if self.A1 == self.A2 == self.computer and self.turn == "comp" and self.A3 == "":
                self.A3 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            if self.B1 == self.B2 == self.computer and self.turn == "comp" and self.B3 == "":
                self.B3 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            if self.C1 == self.C2 == self.computer and self.turn == "comp" and self.C3 == "":
                self.C3 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"

            #Two in a column
            #A
            if self.C1 == self.B1 == self.computer and self.turn == "comp" and self.A1 == "":
                self.A1 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            if self.C2 == self.B2 == self.computer and self.turn == "comp" and self.A2 == "":
                self.A2 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            if self.C3 == self.B3 == self.computer and self.turn == "comp" and self.A3 == "":
                self.A3 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            #B
            if self.A1 == self.C3 == self.computer and self.turn == "comp" and self.B1 == "":
                self.B1 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            if self.A2 == self.C2 == self.computer and self.turn == "comp" and self.B2 == "":
                self.B2 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            if self.A3 == self.C3 == self.computer and self.turn == "comp" and self.B3 == "":
                self.B3 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
                #C
            if self.A1 == self.B1 == self.computer and self.turn == "comp" and self.C1 == "":
                self.C1 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            if self.A2 == self.B2 == self.computer and self.turn == "comp" and self.C2 == "":
                self.C2 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            if self.A3 == self.B3 == self.computer and self.turn == "comp" and self.C3 == "":
                self.C3 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"

            #Two diagonal
            #A1-C3
            if self.A1 == self.C1 == self.computer and self.turn == "comp" and self.B2 == "":
                self.B2 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            #A3-C1
            if self.A3 == self.C1 == self.computer and self.turn == "comp" and self.B2 == "":
                self.B2 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            #A1-B2
            if self.A1 == self.B2 == self.computer and self.turn == "comp" and self.C3 == "":
                self.C3 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            #C1-B2
            if self.C1 == self.B2 == self.computer and self.turn == "comp" and self.A3 == "":
                self.A3 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            #A3-B2
            if self.A3 == self.B2 == self.computer and self.turn == "comp" and self.C1 == "":
                self.C1 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"
            #C3-B2
            if self.C3 == self.B2 == self.computer and self.turn == "comp" and self.A1 == "":
                self.A1 = self.computer
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"

            #<<Stop player>>
            #Two in a row
            #1
            if self.A2 == self.A3 == self.player and self.turn == "comp" and self.A1 == "":
                self.A1 = self.computer
                self.turn = "player"
            if self.B2 == self.B3 == self.player and self.turn == "comp" and self.B1 == "":
                self.B1 = self.computer
                self.turn = "player"
            if self.C2 == self.C3 == self.player and self.turn == "comp" and self.C1 == "":
                self.C1 = self.computer
                self.turn = "player"
            #2
            if self.A1 == self.A3 == self.player and self.turn == "comp" and self.A2 == "":
                self.A2 = self.computer
                self.turn = "player"
            if self.B1 == self.B3 == self.player and self.turn == "comp" and self.B2 == "":
                self.B2 = self.computer
                self.turn = "player"
            if self.C1 == self.C3 == self.player and self.turn == "comp" and self.C2 == "":
                self.C2 = self.computer
                self.turn = "player"
            #3
            if self.A1 == self.A2 == self.player and self.turn == "comp" and self.A3 == "":
                self.A3 = self.computer
                self.turn = "player"
            if self.B1 == self.B2 == self.player and self.turn == "comp" and self.B3 == "":
                self.B3 = self.computer
                self.turn = "player"
            if self.C1 == self.C2 == self.player and self.turn == "comp" and self.C3 == "":
                self.C3 = self.computer
                self.turn = "player"

            #Two in a column
            #A
            if self.C1 == self.B1 == self.player and self.turn == "comp" and self.A1 == "":
                self.A1 = self.computer
                self.turn = "player"
            if self.C2 == self.B2 == self.player and self.turn == "comp" and self.A2 == "":
                self.A2 = self.computer
                self.turn = "player"
            if self.C3 == self.B3 == self.player and self.turn == "comp" and self.A3 == "":
                self.A3 = self.computer
                self.turn = "player"
            #B
            if self.A1 == self.C3 == self.player and self.turn == "comp" and self.B1 == "":
                self.B1 = self.computer
                self.turn = "player"
            if self.A2 == self.C2 == self.player and self.turn == "comp" and self.B2 == "":
                self.B2 = self.computer
                self.turn = "player"
            if self.A3 == self.C3 == self.player and self.turn == "comp" and self.B3 == "":
                self.B3 = self.computer
                self.turn = "player"
            #C
            if self.A1 == self.B1 == self.player and self.turn == "comp" and self.C1 == "":
                self.C1 = self.computer
                self.turn = "player"
            if self.A2 == self.B2 == self.player and self.turn == "comp" and self.C2 == "":
                self.C2 = self.computer
                self.turn = "player"
            if self.A3 == self.B3 == self.player and self.turn == "comp" and self.C3 == "":
                self.C3 = self.computer
                self.turn = "player"

            #Two diagonal
            #A1-C3
            if self.A1 == self.C3 == self.player and self.turn == "comp" and self.B2 == "":
                self.B2 = self.computer
                self.turn = "player"
            #A3-C1
            if self.A3 == self.C1 == self.player and self.turn == "comp" and self.B2 == "":
                self.B2 = self.computer
                self.turn = "player"
            #A1-B2
            if self.A1 == self.B2 == self.player and self.turn == "comp" and self.C3 == "":
                self.C3 = self.computer
                self.turn = "player"
            #C1-B2
            if self.C1 == self.B2 == self.player and self.turn == "comp" and self.A3 == "":
                self.A3 = self.computer
                self.turn = "player"
            #A3-B2
            if self.A3 == self.B2 == self.player and self.turn == "comp" and self.C1 == "":
                self.C1 = self.computer
                self.turn = "player"
            #C3-B2
            if self.C3 == self.B2 == self.player and self.turn == "comp" and self.A1 == "":
                self.A1 = self.computer
                self.turn = "player"

            #Random moves
            if self.compmove == 1 and self.A1 == "" and self.turn == "comp":
                self.A1 = self.computer
                self.turn = "player"
            elif self.compmove == 2 and self.A2 == "" and self.turn == "comp":
                self.A2 = self.computer
                self.turn = "player"
            elif self.compmove == 3 and self.A3 == "" and self.turn == "comp":
                self.A3 = self.computer
                self.turn = "player"
            elif self.compmove == 4 and self.B1 == "" and self.turn == "comp":
                self.B1 = self.computer
                self.turn = "player"
            elif self.compmove == 5 and self.B2 == "" and self.turn == "comp":
                self.B2 = self.computer
                self.turn = "player"
            elif self.compmove == 6 and self.B3 == "" and self.turn == "comp":
                self.B3 = self.computer
                self.turn = "player"
            elif self.compmove == 7 and self.C1 == "" and self.turn == "comp":
                self.C1 = self.computer
                self.turn = "player"
            elif self.compmove == 8 and self.C2 == "" and self.turn == "comp":
                self.C2 = self.computer
                self.turn = "player"
            elif self.compmove == 9 and self.C3 == "" and self.turn == "comp":
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

        if self.window == "win":
            self.display_post_game_menu("You Won!", BLUE)

        if self.window == "lose":
            self.display_post_game_menu("You lost...", RED)

        if self.window == "cats":
            self.display_post_game_menu("Cat's Game!", GREEN)

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

            self.draw_each_x()
            self.draw_each_o()

            if self.status == "lost":
                self.window = "lose"
                self.status = ""
            if self.status == "won":
                self.window = "win"
                self.status = ""

        pygame.display.flip()

        clock.tick(60)

    def draw_each_x(self):
        coordinates = {
                "A1": [[200,100], [300,200], [300,100], [200,200]],
                "A2": [[400,100], [500,200], [500,100], [400,200]],
                "A3": [[600,100], [700,200], [700,100], [600,200]],
                "B1": [[200,300], [300,400], [300,300], [200,400]],
                "B2": [[400,300], [500,400], [500,300], [400,400]],
                "B3": [[600,300], [700,400], [700,300], [600,400]],
                "C1": [[200,500], [300,600], [300,500], [200,600]],
                "C2": [[400,500], [500,600], [500,500], [400,600]],
                "C3": [[600,500], [700,600], [700,500], [600,600]]
            }

        positions = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

        for p in positions:
            if getattr(self, p) == "X":
                pygame.draw.line(self.screen, BLACK, coordinates[p][0], coordinates[p][1], 5)
                pygame.draw.line(self.screen, BLACK, coordinates[p][2], coordinates[p][3], 5)

        if self.C3 == "X":
            pygame.draw.line(self.screen, BLACK, [600,500], [700,600], 5)
            pygame.draw.line(self.screen, BLACK, [700,500], [600,600], 5)

    def draw_each_o(self):
        coordinates = {"A1": [200,100,100,100], "A2": [400,100,100,100],
                "A3": [600,100,100,100], "B1": [200,300,100,100],
                "B2": [400,300,100,100], "B3": [600,300,100,100],
                "C1": [200,500,100,100], "C2": [400,500,100,100],
                "C3": [600,500,100,100]}

        positions = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

        for p in positions:
            if getattr(self, p) == "O":
                pygame.draw.ellipse(self.screen, RED, coordinates[p], 4)

    def reset_clicks(self):
        self.clickx = 0
        self.clicky = 0

    def process_post_game_menu(self):
        global done
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

    def display_post_game_menu(self, message, message_color):
        titlefont = pygame.font.Font(None, 56)
        title = titlefont.render(message, True, message_color)
        pygame.time.delay(1000)
        menufont = pygame.font.Font(None, 48)
        self.screen.blit(title, [175, 100])

        newgame = menufont.render("Play Again", True, BLACK)
        self.screen.blit(newgame, [365, 285])
        pygame.draw.rect(self.screen, BLACK, [250, 250, 400, 100], 2)

        quitgame = menufont.render("Quit Game", True, BLACK)
        self.screen.blit(quitgame, [365, 435])
        pygame.draw.rect(self.screen, BLACK, [250, 400, 400, 100], 2)

    def get_position_from_click_coordinates(self):
        column = ""
        if (150 < self.clickx < 350):
            column = "1"
        elif (350 < self.clickx < 550):
            column = "2"
        elif (550 < self.clickx < 750):
            column = "3"

        row = ""
        if (50 < self.clicky < 250):
            row = "A"
        elif (250 < self.clicky < 450):
            row = "B"
        elif (450 < self.clicky < 650):
            row = "C"

        return row + column

    def set_players_choice(self):
        self.playchoice = self.get_position_from_click_coordinates()

game = Game()
game.run()