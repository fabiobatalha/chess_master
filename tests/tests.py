# coding: utf-8
import unittest

import chess

class TestsChessMasterPiece(unittest.TestCase):

    def test_instanciation_piece(self):

        pawn = chess.Pawn()

        expected = (0,0)

        self.assertEqual(pawn.position, expected)

    def test_instanciation_preset_position(self):

        pawn = chess.Pawn((1,1))

        expected = (1,1)

        self.assertEqual(pawn.position, expected)


    def test_set_position(self):

        pawn = chess.Pawn()

        pawn.set_position((1,2))

        expected = (1,2)

        self.assertEqual(pawn.position, expected)

    def test_set_invalid_position_1(self):

        pawn = chess.Pawn()

        with self.assertRaises(ValueError):
            pawn.set_position((-1,2))

    def test_set_invalid_position_2(self):

        pawn = chess.Pawn()

        with self.assertRaises(ValueError):
            pawn.set_position((1,-2))


    def test_set_invalid_position_3(self):

        pawn = chess.Pawn()

        with self.assertRaises(ValueError):
            pawn.set_position((-1,-2))

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
        king = chess.King((1,2))

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
        pawn1 = chess.Pawn((1,2))
        pawn2 = chess.Pawn((1,2))

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
            [None, None, None,None, None, None, None],
            [None, None, None,None, None, None, None],
            [None, None, None,None, None, None, None],
            [None, None, None,None, None, None, None],
            [None, None, None,None, None, None, None],
            [None, None, None,None, None, None, None],
            [None, None, None,None, None, None, None]
        ]

        self.assertEqual(board.picture, expected)

if __name__ == '__main__':
    unittest.main()
    