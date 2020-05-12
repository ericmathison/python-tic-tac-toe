import pygame
import random

BLACK, WHITE, BLUE, GREEN, RED = (0,0,0), (255,255,255), (0,0,255), (0,255,0), (255,0,0)

class Board:

    possible_wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
                     [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    def __init__(self):
        self.turn = "player"
        self.playchoice = ""
        self.state = "---------"

    def status(self, player):
        opponent = "X" if player == "O" else "O"
        if self.is_winner(player):
            return "won"
        elif self.is_winner(opponent):
            return "lost"
        elif self.is_game_over():
            return "cats"
        else:
            return "unfinished"

    def is_game_over(self):
        for char in self.state:
            if char == '-':
                return False
        return True

    def is_winner(self, contestant):
        for first, second, third in self.possible_wins:
            if (self.state[first - 1] == self.state[second - 1] ==
                self.state[third - 1] == contestant):
                return True

    def move(self, position, piece):
        self.state = self.state[:position - 1] + piece + self.state[position:]


class Game:

    def __init__(self):
        self.board = Board()
        self.reset_clicks()
        self.window = "main"
        self.player = "X"
        self.computer = "O"
        self.letter_coordinates = [[200, 100], [400, 100], [600, 100],
            [200, 300], [400, 300], [600, 300], [200, 500], [400, 500], [600, 500]]
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((900, 700))
        pygame.display.set_caption("Tic Tac Toe")
        pygame.init()

    def run(self):
        while True:
            self.event_loop()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                self.clickx, self.clicky = pygame.mouse.get_pos()
                if self.window == "game":
                    self.board.turn = "comp"

        self.screen.fill(WHITE)

        if self.window == "choice":
            self.display_letter_choice_menu()
            self.select_symbol()

        if self.window == "game":
            self.set_players_choice()
            gamefont = pygame.font.Font(None, 48)
            game_text = gamefont.render("Player is: " + self.player, True, BLACK)
            self.screen.blit(game_text, [350, 5])
            turn_text = gamefont.render("It's your turn...", True, BLACK)
            self.screen.blit(turn_text, [350, 655])

            for x, y in [[[150, 250], [750, 250]], [[150, 450], [750, 450]],
                          [[350, 50],  [350, 650]], [[550, 50],  [550, 650]]]:
                pygame.draw.line(self.screen, BLACK, x, y, 5)

            self.draw_all_letters()

            if self.board.status(self.player) in ["won", "lost", "cats"]:
                self.window = "over"

        if self.board.playchoice != '':
            self.board.move(self.board.playchoice, self.player)

        if self.board.turn == "comp":
            self.computers_turn()

        if self.window == "main":
            self.display_menu("Welcome to Daniel's Tic Tac Toe", "New Game", BLACK)
            self.process_menu()

        if self.window == "over":
            mesages = {"won": "You Won!", "lost": "You lost...", "cats": "Cat's Game!"}
            colors = {"won": BLUE, "lost": RED, "cats": GREEN}
            status = self.board.status(self.player)
            self.display_menu(mesages[status], "Play Again", colors[status])
            self.process_menu()

        pygame.display.flip()

        self.clock.tick(30)

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

    def try_preventing_win(self):
        preventable_wins = [
            [2, 3, 1], [5, 6, 4], [8, 9, 7], [1, 3, 2], [4, 6, 5], [7, 9, 8],
            [1, 2, 3], [4, 5, 6], [7, 8, 9], [7, 4, 1], [8, 5, 2], [9, 6, 3],
            [1, 9, 5], [2, 8, 5], [3, 9, 6], [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [3, 7, 5], [1, 5, 9], [7, 5, 3], [3, 5, 7], [9, 5, 1], [1, 7, 4]]

        for first, second, third in preventable_wins:
            if (self.board.state[first - 1] == self.board.state[second - 1] == self.player and self.board.state[third - 1] == "-"):
                    self.board.move(third, self.computer)
                    self.board.turn = "player"
                    return

    def attempt_computer_win(self):
        for n in range(0, 9):
            state = self.board.state[:n] + self.computer + self.board.state[n + 1:]
            for first, second, third in Board.possible_wins:
                if (state[first - 1] == state[second - 1] == state[third - 1]
                        == self.computer and self.board.state[n] == "-"):
                    self.board.move(n + 1, self.computer)
                    self.board.turn = "player"
                    return

    def make_random_computer_move(self):
        if self.board.turn == "comp":
            rand_list = random.sample(list(range(0, 9)), 9)
            for n in rand_list:
                if self.board.state[n] == "-":
                    self.board.move(n + 1, self.computer)
                    self.board.turn = "player"
                    return

    def computers_turn(self):
        self.attempt_computer_win()
        self.try_preventing_win()
        self.make_random_computer_move()
        if self.board.is_winner(self.computer):
            self.reset_clicks()
        self.board.turn = "player"

    def draw_all_letters(self):
        for i in range(9):
            self.draw_letter(self.board.state[i], self.letter_coordinates[i][0], self.letter_coordinates[i][1])

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
            self.board = Board()
            self.reset_clicks()
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
        pygame.draw.rect(self.screen, BLACK, [175, 275, 150, 150], 2)
        self.draw_letter("X", 200, 300)
        pygame.draw.rect(self.screen, BLACK, [575, 275, 150, 150], 2)
        self.draw_letter("O", 600, 300)

    def get_position_from_click(self):
        coordinates = [[x, y] for y in [50, 250, 450] for x in [150, 350, 550]]
        for (index, (x, y)) in enumerate(coordinates):
            if x < self.clickx < x + 200 and y < self.clicky < y + 200:
                return index + 1

    def set_players_choice(self):
        position = self.get_position_from_click()
        if isinstance(position, int) and self.board.state[position - 1] == "-":
            self.board.playchoice = position
        else:
            self.board.turn = "player"

game = Game()
game.run()
