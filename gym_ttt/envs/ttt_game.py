# Actual Tic-Tac-Toe game implementation

from gym import spaces
import numpy as np


class Game():
    def __init__(self, m=3, n=3, k=3):
        """Implement m,n,k game, defaulting to standard Tic-Tac-Toe"""
        self.m = m
        self.n = n
        self.k = k

        self.board = np.zeros((m, n), dtype=int)

    def reset(self):
        self.board = np.zeros((self.m, self.n), dtype=int)
        return self.board

    def move(self, player, square):
        # self.board[square] = player # for direct matrix moves, doesn't work with OpenAI Baseline DeepQ
        info = {'win': False, 'draw': False}

        self.board.reshape(self.m * self.n)[square] = player

        done, endType = self.checkDone()

        if done:
            if endType == 'draw':
                info['draw'] = True
            else:
                info['win'] = True


        return self.board, done, info

    def printGagme(self):
        n = self.board.shape[0]

        print("   ", end="")
        for y in range(n):
            print(y, "", end="")
        print("")
        print("  ", end="")
        for _ in range(n):
            print("-", end="-")
        print("--")
        for y in range(n):
            print(y, "|", end="")  # print the row #
            for x in range(n):
                piece = self.board[y][x]  # get the piece to print
                if piece == 1:
                    print("X ", end="")
                elif piece == -1:
                    print("O ", end="")
                else:
                    if x == n:
                        print("-", end="")
                    else:
                        print("- ", end="")
            print("|")

        print("  ", end="")
        for _ in range(n):
            print("-", end="-")
        print("--")

    def checkDone(self):
        done = not (self.board == 0).any()
        if done:
            return done, 'draw'

        done = (abs(self.board.sum(0)) == self.k).any()
        done = done or (abs(self.board.sum(1)) == self.k).any()
        done = done or abs(self.board.diagonal().sum()) == self.k
        done = done or abs(self.board.diagonal(axis1=1, axis2=0).sum()) == self.k
        if done:
            return done, 'win'

        return done, ''
