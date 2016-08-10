# coding: utf-8

class BoardExceptions(Exception):
    pass

class OccupiedSquare(BoardExceptions):

    def __init__(self, value):
        self.value = value

class Board(object):

    def __init__(self, size):
        self.board = None
        self.pieces = []
        self._setup_board(size)

    def _setup_board(self, size):
        """
        This method will setup the size of the board setting up a 2 dimension 
        list in self.board.

        Arguments:
        size -- integer
        """

        if not isinstance(size, int):
            raise ValueError ('board size must be integer')

        self.board = [[None for i in range(size)] for i in range(size)]

    def _update_board(self):
        """
        Update the self.board with the position of each piece available in 
        self.pieces.
        """

        for piece in self.pieces:
            x, y = piece.position
            self.board[x][y] = piece

    @property
    def picture(self):
        """
        Return a 2 dimension list with a picture of the current state of the
        board and pieces position.
        """
        return [[(str(x) if x else x) for x in i] for i in self.board]

    def place_piece(self, piece):
        """
        Put a given piece on the board.

        The piece must not threatening any other piece already available in
        the board. If so, it will raise Threatened Exception.

        The piece position must not match with the position of any other piece
        already available in the board. If so, it will raise OccupiedSquare
        Exception.

        Arguments:
        piece -- a instance o Pieces (Pawn, King, Bishop, Queen, Rook, Kinight)
        """
        x, y = piece.position

        if self.picture[x][y] != None:
            raise OccupiedSquare(str(piece.position))

        self.pieces.append(piece)
        self._update_board()


class Pieces(object):

    def __init__(self, position=None):

        self.set_position(position or (0,0))

    def set_position(self, position):
        """
        Set the x,y position of the piece on the board.
        position: (interger, interger)
        """

        if len(position) != 2:
            raise ValueError('Position must be a tuple of 2 integers')

        if not isinstance(position[0], int) or not isinstance(position[1], int):
            raise ValueError('Position must be a tuple of integers')

        if position[0] < 0 or position[1] < 0:
            raise ValueError('Position must be 0 or positive intergers')

        self.position = position


class Bishop(Pieces):

    NAME = 'bishop'

    def __str__(self):

        return self.NAME
    
    def threatening_zone(self, max_size):
        """
        Get the current position of the piece and produce a list of threathening
        places in the board.

        Arguments:
        max_size -- integer that defines de boundary limits of the board.
        """
        
        import pdb; pdb.set_trace()
        
        self.position

class Kinight(Pieces):

    NAME = 'kinight'

    def __str__(self):

        return self.NAME

    def threatening_zone():
        """
        Get the current position of the piece and produce a list of threathening
        places in the board.
        """
        
        pass

class King(Pieces):

    NAME = 'king'

    def __str__(self):

        return self.NAME

    def threatening_zone(self):
        """
        Get the current position of the piece and produce a list of threathening
        places in the board.
        """
        
        pass

class Pawn(Pieces):

    NAME = 'pawn'

    def __str__(self):

        return self.NAME

    def threatening_zone(self, max_size):
        """
        Get the current position of the piece and produce a list of threathening
        places in the board.

        Arguments:
        max_size -- integer that defines de boundary limits of the board.
        """
        zone = []

        x, y = self.position

        zone.append((x+1, y+1))
        zone.append((x-1, y+1))

        return [(x, y) for x, y in zone if x in range(max_size) and y in range(max_size)]


class Queen(Pieces):

    NAME = 'queen'

    def __str__(self):

        return self.NAME

    def threatening_zone():
        """
        Get the current position of the piece and produce a list of threathening
        places in the board.
        """
        
        pass

class Rook(Pieces):

    NAME = 'rook'

    def __str__(self):

        return self.NAME

    def threatening_zone():
        """
        Get the current position of the piece and produce a list of threathening
        places in the board.
        """
        
        pass
