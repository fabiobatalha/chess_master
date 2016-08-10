import unittest

from masterchess import chess


class TestsChessMasterPiece(unittest.TestCase):

    def test_instanciation_piece(self):

        pawn = chess.Pawn()

        expected = (0, 0)

        self.assertEqual(pawn.position, expected)

    def test_instanciation_preset_position(self):

        pawn = chess.Pawn((1, 1))

        expected = (1, 1)

        self.assertEqual(pawn.position, expected)

    def test_set_position(self):

        pawn = chess.Pawn()

        pawn.set_position((1, 2))

        expected = (1, 2)

        self.assertEqual(pawn.position, expected)

    def test_set_invalid_position_1(self):

        pawn = chess.Pawn()

        with self.assertRaises(ValueError):
            pawn.set_position((-1, 2))

    def test_set_invalid_position_2(self):

        pawn = chess.Pawn()

        with self.assertRaises(ValueError):
            pawn.set_position((1, -2))

    def test_set_invalid_position_3(self):

        pawn = chess.Pawn()

        with self.assertRaises(ValueError):
            pawn.set_position((-1, -2))

    def test_set_invalid_position_4(self):

        pawn = chess.Pawn()

        with self.assertRaises(ValueError):
            pawn.set_position(('a', 2))

    def test_set_invalid_position_5(self):

        pawn = chess.Pawn()

        with self.assertRaises(ValueError):
            pawn.set_position((1, 'a'))

    def test_set_invalid_position_6(self):

        pawn = chess.Pawn()

        with self.assertRaises(ValueError):
            pawn.set_position(('a', 'a'))

    def test_set_invalid_position_7(self):

        pawn = chess.Pawn()

        with self.assertRaises(ValueError):
            pawn.set_position((1, ))

    def test_set_invalid_position_8(self):

        pawn = chess.Pawn()

        with self.assertRaises(ValueError):
            pawn.set_position((1, 2, 4,))

    def test_pawn_threatening_zone(self):
        """
        Testing pawn when the piece is able to threatening other piece in both
        sides.
        """

        pawn = chess.Pawn((4, 0))

        expected = [
            (3, 1),
            (5, 1)
        ]

        self.assertEqual(
            sorted(pawn.threatening_zone(8)), sorted(expected)
        )

    def test_pawn_threatening_x_boundary_left(self):
        """
        Testing boundary where the pawn can not move to the left
        """

        pawn = chess.Pawn((0, 0))

        expected = [
            (1, 1)
        ]

        self.assertEqual(
            sorted(pawn.threatening_zone(8)), sorted(expected)
        )

    def test_pawn_threatening_x_boundary_right(self):
        """
        Testing boundary where the pawn can not move to the right
        """

        pawn = chess.Pawn((7, 0))

        expected = [
            (6, 1)
        ]

        self.assertEqual(
            sorted(pawn.threatening_zone(8)), sorted(expected)
        )

    def test_pawn_threatening_zone_y_boundary(self):
        """
        Testing boundary where the pawn can not move forward
        """

        pawn = chess.Pawn((4, 7))

        expected = []

        self.assertEqual(
            sorted(pawn.threatening_zone(8)), sorted(expected)
        )

    def test_pawn_threatening_zone_y_boundary_last_move(self):
        """
        Testing boundary where the pawn can make your last move forward
        """

        pawn = chess.Pawn((4, 6))

        expected = [
            (3, 7),
            (5, 7)
        ]

        self.assertEqual(
            sorted(pawn.threatening_zone(8)), sorted(expected)
        )

    def test_se_positions(self):

        piece = chess.Pieces((3, 4))

        expected = [
            (4, 3),
            (5, 2),
            (6, 1),
            (7, 0),
        ]

        self.assertEqual(
            sorted(piece._se_positions(8)), sorted(expected)
        )

    def test_ne_positions(self):

        piece = chess.Pieces((3, 4))

        expected = [
            (4, 5),
            (5, 6),
            (6, 7)
        ]

        self.assertEqual(
            sorted(piece._ne_positions(8)), sorted(expected)
        )

    def test_nw_positions(self):

        piece = chess.Pieces((3, 4))

        expected = [
            (2, 5),
            (1, 6),
            (0, 7)
        ]

        self.assertEqual(
            sorted(piece._nw_positions(8)), sorted(expected)
        )

    def test_sw_positions(self):

        piece = chess.Pieces((3, 4))

        expected = [
            (2, 3),
            (1, 2),
            (0, 1)
        ]

        self.assertEqual(
            sorted(piece._sw_positions(8)), sorted(expected)
        )


    def test_bishop_threatening_zone(self):
        """
        Testing bishop moves when the piece is able to threatening other pieces
        in all directions.
        """

        bishop = chess.Bishop((3, 4))

        expected = [
            (0, 1),
            (0, 7),
            (1, 2),
            (1, 6),
            (2, 3),
            (2, 5),
            (4, 3),
            (4, 5),
            (5, 2),
            (5, 6),
            (6, 1),
            (6, 7),
            (7, 0)
        ]

        self.assertEqual(
            sorted(bishop.threatening_zone(8)), sorted(expected)
        )


class TestsChessMasterBoard(unittest.TestCase):

    def test_put_1_piece(self):

        pawn = chess.Pawn()

        board = chess.Board(3)

        board.place_piece(pawn)

        expected = [
            ['pawn', None, None],
            [None, None, None],
            [None, None, None]
        ]

        self.assertEqual(board.picture, expected)

    def test_put_2_pieces(self):

        pawn = chess.Pawn()
        king = chess.King((1, 2))

        board = chess.Board(3)

        board.place_piece(pawn)
        board.place_piece(king)

        expected = [
            ['pawn', None, None],
            [None, None, 'king'],
            [None, None, None]
        ]

        self.assertEqual(board.picture, expected)

    def test_put_piece_in_occupied_square(self):
        pawn1 = chess.Pawn((1, 2))
        pawn2 = chess.Pawn((1, 2))

        board = chess.Board(3)

        board.place_piece(pawn1)

        with self.assertRaises(chess.OccupiedSquare):
            board.place_piece(pawn2)

    def test_instanciating_board_wrong_size(self):

        with self.assertRaises(ValueError):
            board = chess.Board('wrong size')

    def test_instanciating_board_size_3(self):

        board = chess.Board(3)

        expected = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]

        self.assertEqual(board.picture, expected)

    def test_instanciating_board_size_7(self):

        board = chess.Board(7)

        expected = [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None]
        ]

        self.assertEqual(board.picture, expected)

if __name__ == '__main__':
    unittest.main()
