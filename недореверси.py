import pygame
import random
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton

print("Введите размер поля")
n1, n2 = list(map(int, input().split()))


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[True] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.col = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                    (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))]
        self.board_col = [(random.choice(self.col)) * width for _ in range(height)]
        self.pl1 = None
        self.pl2 = None

        self.ask = Ask(self, self.col[0], self.col[1])
        self.ask.show()


    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(screen, pygame.Color("white"),
                                 ((self.left + self.cell_size * i,
                                   self.top + self.cell_size * j),
                                  (self.cell_size, self.cell_size)), 1)
                pygame.draw.circle(screen2, self.board_col[j][i],
                                   (
                                   self.left + self.cell_size * i + self.cell_size // 2,
                                   self.top + self.cell_size * j + self.cell_size // 2),
                                   self.cell_size // 2 - 2, 2)

    def get_cell(self, mouse_pos):
        if (self.left <= mouse_pos[
            0] <= self.left + self.cell_size * self.width and
                self.top <= mouse_pos[
                    1] <= self.top + self.cell_size * self.height):
            y = (mouse_pos[0] - self.left) // self.cell_size
            x = (mouse_pos[1] - self.top) // self.cell_size
            return x, y
        else:
            return None

    def on_click(self, cell_pos):
        '''if cell_pos:
            y, x = cell_pos[0], cell_pos[1]
            if self.player == 1 and self.board[y][x] is True:
                pygame.draw.line(screen2, pygame.Color("blue"),
                                 (self.left + self.cell_size * x,
                                  self.top + self.cell_size * y),
                                 (self.left + self.cell_size * (x + 1) - 2,
                                  self.top + self.cell_size * (y + 1)), 2)
                pygame.draw.line(screen2, pygame.Color("blue"),
                                 (self.left + self.cell_size * (x + 1) - 2,
                                  self.top + self.cell_size * y),
                                 (self.left + self.cell_size * x + 2,
                                  self.top + self.cell_size * (y + 1) - 2), 2)
            elif self.player == 2 and self.board[y][x] is True:
                pygame.draw.circle(screen2, pygame.Color("red"),
                                   (self.left + self.cell_size * x + self.cell_size // 2,
                                    self.top + self.cell_size * y + self.cell_size // 2),
                                   self.cell_size // 2 - 2, 2)
            self.board[y][x] = False
            if self.player == 1:
                self.player = 2
            else:
                self.player = 1'''

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)



class Ask(QWidget):
    def __init__(self, par, col1, col2):
        super().__init__()
        parrent = par
        self.col_1 = col1
        self.col_2 = col2

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("ыбор цвета игрока 1")

        self.lbl = QLabel(self)
        self.lbl.setText("Выберите цвет")
        self.move(60, 30)

        self.btn_c1 = QPushButton(self)
        self.btn_c1.setStyleSheet(f'background-color: {self.col_1}')
        self.btn_c1.setText(self.col_1)
        self.btn_c1.move(50, 150)
        self.btn_c1.clicked.connect(self.pl_c)

        self.btn_c2 = QPushButton(self)
        self.btn_c2.setStyleSheet(f'background-color: {self.col_2}')
        self.btn_c2.setText(self.col_2)
        self.btn_c2.move(100, 150)
        self.btn_c2.clicked.connect(self.pl_c)

    def pl_c(self):
        if self.sender().text() == self.col_1:
            self.parrent.pl1 = self.col_1
            self.parrent.pl2 = self.col_2
        else:
            self.parrent.pl1 = self.col_2
            self.parrent.pl2 = self.col_1



pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
screen2 = pygame.Surface(screen.get_size())

board = Board(n1, n2)

board.set_view(20, 60, 50)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    screen.blit(screen2, (0, 0))
    board.render()
    pygame.display.flip()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ask(col1, col2)
    sys.exit(app.exec_())
