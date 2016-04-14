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
    def __init__(self, actions_func):
        """
        :param actions_func: a function object
            actions func is a function that when you feed it a state as an
            argument, you get back a list of available actions.
        """
        self.last_state = None
        self.state = None
        self.last_action = None
        self.win_tally = {"win": 0, "lose": 0, "draw": 0}
        self.learning = True
        self.get_available_actions = actions_func

    # ==========================================================================
    #                                                             SET_TO_LEARN()
    # ==========================================================================
    def set_to_learn(self, learn_state=True):
        self.learning = learn_state

    # ==========================================================================
    #                                                          RESET_WIN_TALLY()
    # ==========================================================================
    def reset_win_tally(self):
        self.win_tally = {"win": 0, "lose": 0, "draw": 0}

    # ==========================================================================
    #                                                     RESET_STATES_ACTIONS()
    # ==========================================================================
    def reset_states_actions(self):
        self.last_state = None
        self.state = None
        self.last_action = None

    # ==========================================================================
    #                                                             CHOSE_ACTION()
    # ==========================================================================
    def chose_action(self, state):
        """
        Given a state it makes a decision of which action to take.
        """
        pass

    # ==========================================================================
    #                                                     ENVIRONMENT_FEEDBACK()
    # ==========================================================================
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

    # ==========================================================================
    #                                                              UPDATE_WINS()
    # ==========================================================================
    def update_wins(self, win_status):
        """ Updates the win tally"""
        self.win_tally[win_status] += 1

    # ==========================================================================
    #                                                           TERMINAL_STATE()
    # ==========================================================================
    def terminal_state(self, s1, a, r):
        """
        :param s1: last state
        :param a:  last action
        :param r:  reward
        """
        pass


