import gym
from gym import error, spaces, utils
from gym.utils import seeding

import numpy as np

from .ttt_game import Game


class TTTEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, m=3, n=3, k=3):
        """Implement m,n,k game, defaulting to standard Tic-Tac-Toe"""
        self.m = m
        self.n = n
        self.k = k

        self.action_space = spaces.Discrete(m * n)
        # self.action_space = spaces.Box(-1, 1, (m, n), np.float32)
        self.observation_space = spaces.Box(-1, 1, (m, n), np.float32)
        self.reward_range = (-1, 1)

        self.player = 1
        self.game = Game(m, n, k)

        self.mainPlayer = 'placeholder'
        self.secondPlayer = 'placeholder'

    def step(self, action):
        """Observation, Reward, done, info"""

        # Dumb illegal move handling since I can't easily modify the Baseline DQN model
        if self.game.board.reshape(self.m * self.n)[action] != 0:
            return self.game.board, -2, False, {}

        reward = 0

        # Run player 1
        newState, done, endType = self.game.move(self.player, action)

        if done and endType['win']:
            reward = 1

        # If not done, run player 2
        if not done:
            # TODO: get player 2 action
            newState, done, endType = self.game.move(-self.player, self.action_space.sample())

        if done and endType['win']:
            reward = -1

        if done:
            self.render()

        return newState, reward, done, endType

    def reset(self):
        return self.game.reset()

    def render(self, mode='human', close=False):
        self.game.printGagme()
