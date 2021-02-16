"""
Handle operations related to games and connections
between player, board, chat, and round
"""
from .Player import Player
from .Board import Board
from .Round import Round

class Game(object):

    def __init__(self, id, players, thread):
        """
        init the game once player threshold is set
        :param id: int
        :param players: Players []
        """
        self.id = id
        self.players =players
        self.word_used = []
        self.round = None
        self.board = Board()
        self.player_draw_ind = 0
        self.connected_thread = thread
        self.start_new_round()

    def start_new_round(self):
        """
        start a new round with a new word
        :return: None
        """
        self.round = Round(self.get_word(), self.players[self.player_draw_ind], self.players, self )
        self.player_draw_ind += 1

        if self.player_draw_ind >= len(self.players):
            self.end_round()
            self.end_game()

    def player_guess(self, player, guess):
        """
        makes the player guess the word
        :param player: Player
        :param guess: str
        :return: bool
        """
        return self.round.guess(player, guess)

    def player_disconnected(self, player):
        """
        Call to clean up objects when player disconnects
        :param player: Player
        :raises: Exception()
        """
        pass

    def skip(self):
        """
        Increments the round skips, if skips are greater than
        threshold, start new round
        :return: None
        """
        if self.round:
            new_round = self.round.skip()
            if new_round:
                self.round_ended()
        else:
            raise Exception("No round started yet!")

    def round_ended(self):
        """
        If the round ends call this
        :return: None
        """
        self.start_new_round()
        self.board.clear()

    def update_board(self, x, y, colour):
        """
        Calls update method on board
        :param x: int
        :param y: int
        :param colour: (int,int,int)
        :return: None
        """
        if not self.board:
            raise Exception("No board created")
        self.board.update(x,y,colour)

    def end_game(self):
        """
        ends the game
        :return:
        """
        pass

    def get_word(self):
        """
        gives a word that has not yet been used
        :return: str
        """
        # TODO get a list of words from somewhere
        pass