__author__ = 'Ronny Restrepo'

from Agent import Agent
import random

class Random_Agent(Agent):
    def __init__(self):
        Agent.__init__(self)

    def chose_action(self, state, available_actions):
        return random.choice(available_actions)

