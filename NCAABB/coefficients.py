class Coefficients(object):

    def __init__(self, PLAY_T25=1, WIN_T25=5, WIN_L12=2, PERCENT=100):
        """The coefficients were more art than science. More guessing than art.
        Default vals: 1, 5, 2, and 100, respectively.
        """
        self.PLAY_T25 = PLAY_T25
        self.WIN_T25 = WIN_T25
        self.WIN_L12 = WIN_L12
        self.PERCENT = PERCENT
