# coding: utf-8

class Pieces(object):

    def position(self):
        """
        Retrieve the position of the piece on the board.
        """

        return self.position

    def set_position(self, board, position):
        """
        Set the x,y position of the piece on the board.
        board: board object
        position: (x, y)
        """
        for i in position:
            if < 0:
                return None
        self.position = position

class Pawn(Pieces):

    NAME = 'pawn'

    def __init__(self):

        self.position = (0,0)

class King(Pieces):

    NAME = 'king'

    def __init__(self):

        self.position = (0,0)

class Queen(Pieces):

    NAME = 'queen'

    def __init__(self):

        self.position = (0,0)

class Rook(Pieces):

    NAME = 'rook'

    def __init__(self):

        self.position = (0,0)

class Bishop(Pieces):

    NAME = 'bishop'

    def __init__(self):

        self.position = (0,0)

class Kinight(Pieces):

    NAME = 'kinight'

    def __init__(self):

        self.position = (0,0)