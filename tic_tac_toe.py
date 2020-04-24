import pygame
import random

BLACK, WHITE, BLUE, GREEN, RED = (0,0,0), (255,255,255), (0,0,255), (0,255,0), (255,0,0)

class Game:

    def __init__(self):
        self.initialize_game_state()
        self.window = "main"
        self.player = "X"
        self.computer = "O"
        self.positions = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
        self.letter_coordinates = {
                "A1": [200, 100], "A2": [400, 100], "A3": [600, 100],
                "B1": [200, 300], "B2": [400, 300], "B3": [600, 300],
                "C1": [200, 500], "C2": [400, 500], "C3": [600, 500]
            }
        self.possible_wins = [
            ["A1", "A2", "A3"], ["B1", "B2", "B3"], ["C1", "C2", "C3"],
            ["A1", "B1", "C1"], ["A2", "B2", "C2"], ["A3", "B3", "C3"],
            ["A1", "B2", "C3"], ["A3", "B2", "C1"]]
        self.clock = pygame.time.Clock()

        pygame.init()

        self.screen = pygame.display.set_mode((900, 700))
        pygame.display.set_caption("Tic Tac Toe")

    def initialize_game_state(self):
        self.turn = "player"
        self.status = ""
        self.reset_clicks()
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

    def run(self):
        while True:
            self.event_loop()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                self.clickx, self.clicky = pygame.mouse.get_pos()
                if self.window == "game":
                    self.turn = "comp"

        self.screen.fill(WHITE)

        if self.window == "choice":
            self.display_letter_choice_menu()
            self.select_symbol()

        if self.window in ["main", "win", "lose", "cats"]:
            self.process_menu()

        if self.window == "game":
            self.set_players_choice()
            gamefont = pygame.font.Font(None, 48)
            game_text = gamefont.render("Player is: " + self.player, True, BLACK)
            self.screen.blit(game_text, [350, 5])
            turn_text = gamefont.render("It's your turn...", True, BLACK)
            self.screen.blit(turn_text, [350, 655])

            for coord in [[[150, 250], [750, 250]], [[150, 450], [750, 450]],
                          [[350, 50],  [350, 650]], [[550, 50],  [550, 650]]]:
                pygame.draw.line(self.screen, BLACK, coord[0], coord[1], 5)

            self.draw_all_letters()

            if self.status == "lost":
                self.window = "lose"
            if self.status == "won":
                self.window = "win"


        self.check_for_cats_game()

        self.check_for_win()

        self.move(self.playchoice, self.player)

        if self.turn == "comp":
            self.computers_turn()

        if self.window == "main":
            self.display_menu("Welcome to Daniel's Tic Tac Toe", "New Game", BLACK)

        if self.window == "win":
            self.display_menu("You Won!", "Play Again", BLUE)

        if self.window == "lose":
            self.display_menu("You lost...", "Play Again", RED)

        if self.window == "cats":
            self.display_menu("Cat's Game!", "Play Again", GREEN)

        pygame.display.flip()

        self.clock.tick(60)

    def select_symbol(self):
        if 200 <= self.clickx <= 300 and 300 <= self.clicky <= 400:
            self.player = "X"
            self.computer =  "O"
            self.window = "game"
            self.reset_clicks()
        if 600 <= self.clickx <= 700 and 300 <= self.clicky <= 400:
            self.player = "O"
            self.computer = "X"
            self.window = "game"
            self.reset_clicks()

    def check_for_cats_game(self):
        for p in self.positions:
            if getattr(self, p) == "":
                return
        if self.status not in ["won", "lost"]:
            self.reset_clicks()
            self.window = "cats"

    def check_for_win(self):
        for cond in self.possible_wins:
            if (getattr(self, cond[0]) == getattr(self, cond[1]) ==
                    getattr(self, cond[2]) == self.player):
                self.reset_clicks()
                self.status = "won"
                return

    def try_preventing_win(self):
        preventable_wins = [
            ["A2", "A3", "A1"], ["B2", "B3", "B1"], ["C2", "C3", "C1"],
            ["A1", "A3", "A2"], ["B1", "B3", "B2"], ["C1", "C3", "C2"],
            ["A1", "A2", "A3"], ["B1", "B2", "B3"], ["C1", "C2", "C3"],
            ["C1", "B1", "A1"], ["C2", "B2", "A2"], ["C3", "B3", "A3"],
            ["A1", "C3", "B2"], ["A2", "C2", "B2"], ["A3", "C3", "B3"],
            ["A1", "B1", "C1"], ["A2", "B2", "C2"], ["A3", "B3", "C3"],
            ["A1", "C3", "B2"], ["A3", "C1", "B2"], ["A1", "B2", "C3"],
            ["C1", "B2", "A3"], ["A3", "B2", "C1"], ["C3", "B2", "A1"],
            ["A1", "C1", "B1"]]

        for position in preventable_wins:
            if (getattr(self, position[0]) == getattr(self, position[1]) == self.player and
                getattr(self, position[2]) == ""):
                    self.move(position[2], self.computer)
                    self.turn = "player"
                    return

    def make_random_computer_move(self):
        rand = random.randint(0, 8)
        if getattr(self, self.positions[rand]) == "" and self.turn == "comp":
            self.move(self.positions[rand], self.computer)
            self.turn = "player"

    def move(self, position, piece):
        setattr(self, position, piece)

    def check_for_loss(self):
        for scenario in self.possible_wins:
            if (getattr(self, scenario[0]) == getattr(self, scenario[1]) ==
                getattr(self, scenario[2]) == self.computer):
                self.reset_clicks()
                self.status = "lost"
                self.turn = "player"

    def computers_turn(self):
        self.try_preventing_win()
        self.make_random_computer_move()
        self.check_for_loss()

    def draw_all_letters(self):
        for pos in self.positions:
            self.draw_letter(getattr(self, pos), self.letter_coordinates[pos][0], self.letter_coordinates[pos][1])

    def draw_letter(self, letter, top_left_x, top_left_y):
        if letter == "X":
            pygame.draw.line(self.screen, BLACK, [top_left_x, top_left_y], [top_left_x + 100, top_left_y + 100], 5)
            pygame.draw.line(self.screen, BLACK, [top_left_x + 100, top_left_y], [top_left_x, top_left_y + 100], 5)
        elif letter == "O":
            pygame.draw.ellipse(self.screen, RED, [top_left_x, top_left_y, 100, 100], 4)

    def reset_clicks(self):
        self.clickx = 0
        self.clicky = 0

    def process_menu(self):
        if 250 <= self.clickx <= 650 and 250 <= self.clicky <= 350:
            self.initialize_game_state()
            self.window = "choice"
        if 250 <= self.clickx <= 650 and 400 <= self.clicky <= 500:
            exit()

    def display_menu(self, message, play_message, message_color):
        titlefont = pygame.font.Font(None, 56)
        title = titlefont.render(message, True, message_color)
        menufont = pygame.font.Font(None, 48)
        self.screen.blit(title, [175, 100])

        newgame = menufont.render(play_message, True, BLACK)
        self.screen.blit(newgame, [365, 285])
        pygame.draw.rect(self.screen, BLACK, [250, 250, 400, 100], 2)

        quitgame = menufont.render("Quit Game", True, BLACK)
        self.screen.blit(quitgame, [365, 435])
        pygame.draw.rect(self.screen, BLACK, [250, 400, 400, 100], 2)

    def display_letter_choice_menu(self):
        titlefont = pygame.font.Font(None, 56)
        title = titlefont.render("Choose your symbol...", True, BLACK)
        self.screen.blit(title, [235, 100])
        #Choice X
        pygame.draw.rect(self.screen, BLACK, [175, 275, 150, 150], 2)
        pygame.draw.line(self.screen, BLACK, [200, 300], [300, 400], 5)
        pygame.draw.line(self.screen, BLACK, [300, 300], [200, 400], 5)
        #Choice O
        pygame.draw.rect(self.screen, BLACK, [575, 275, 150, 150], 2)
        pygame.draw.ellipse(self.screen, RED, [600, 300, 100, 100], 4)

    def get_position_from_click_coordinates(self):
        position = ""
        if 50 < self.clicky < 250:
            position += "A"
        elif 250 < self.clicky < 450:
            position += "B"
        elif 450 < self.clicky < 650:
            position += "C"

        if 150 < self.clickx < 350:
            position += "1"
        elif 350 < self.clickx < 550:
            position += "2"
        elif 550 < self.clickx < 750:
            position += "3"

        return position

    def set_players_choice(self):
        self.playchoice = self.get_position_from_click_coordinates()

game = Game()
game.run()
