__author__ = 'Ronny Restrepo'


################################################################################
#                                                                          AGENT
################################################################################
class Agent(object):
    """
    Base Template object for Agents. Do not instantiate this class, use one of
    the subclasses instead.
    """
    # ==========================================================================
    #                                                                 __INIT__()
    # ==========================================================================
    def __init__(self):
        self.last_state = None
        self.state = None
        self.last_action = None
        self.win_tally = {"win": 0, "lose": 0, "draw": 0}
        self.learning = True


    # ==========================================================================
    #                                                             set_to_learn()
    # ==========================================================================
    def set_to_learn(self, learn_state=True):
        self.learning = learn_state

    def reset_win_tally(self):
        self.win_tally = {"win": 0, "lose": 0, "draw": 0}

    def reset_states_actions(self):
        self.last_state = None
        self.state = None
        self.last_action = None

    def chose_action(self, state):
        pass

    def environment_feedback(self, s1, a, s2, r=0):
        """
        takes a state, action, state transition with an optional reward
        :param s1:
        :param a:
        :param s2:
        :param r:
        :return:
        """
        self.state = s2
        self.last_state = s1
        self.last_action = a
        #self.process_reward(r)

    def update_wins(self, win_status):
        self.win_tally[win_status] += 1

    def terminal_state(self, s1, a, r):
        """
        :param r:
        :param s1: last state
        :param a: last action
        """
        pass


