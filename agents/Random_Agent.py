__author__ = 'Ronny Restrepo'

from Agent import Agent
import random

################################################################################
#                                                                   RANDOM_AGENT
################################################################################
class Random_Agent(Agent):
    """
    An agent that when asked to make a choice of actions, always chooses one of
    the available actions at random, using uniform distribution.
    """
    # ==========================================================================
    #                                                                 __INIT__()
    # ==========================================================================
    def __init__(self):
        Agent.__init__(self)

    # ==========================================================================
    #                                                             CHOSE_ACTION()
    # ==========================================================================
    def chose_action(self, state, available_actions):
        return random.choice(available_actions)

