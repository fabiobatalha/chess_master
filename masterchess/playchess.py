# coding: utf-8
import argparse
import logging
import logging.config

from masterchess import chess

logger = logging.getLogger(__name__)

LOGGING = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'NOTSET',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        }
    },
    'loggers': {
        'masterchess': {
            'handlers': ['console'],
            'level': 'DEBUG'
        }
    }
}

logging.config.dictConfig(LOGGING)


def find_place(board, piece):

    for x in range(board.size):
        for y in range(board.size):
            try:
                piece.set_position((x, y))
                board.place_piece(piece)
                return True
            except chess.BoardExceptions:
                continue


def run(board_size, pieces):

    logger.info('Playing Chess')
    logger.info('Board size: %d' % board_size)
    logger.info('Pieces of bishops: %s' % len([piece for piece in pieces if str(piece) == 'bishop']))
    logger.info('Pieces of kinights: %s' % len([piece for piece in pieces if str(piece) == 'kinight']))
    logger.info('Pieces of kings: %s' % len([piece for piece in pieces if str(piece) == 'king']))
    logger.info('Pieces of pawns: %s' % len([piece for piece in pieces if str(piece) == 'pawn']))
    logger.info('Pieces of queens: %s' % len([piece for piece in pieces if str(piece) == 'queen']))
    logger.info('Pieces of rooks: %s' % len([piece for piece in pieces if str(piece) == 'rook']))

    total_pieces = len(pieces)
    placed_pieces = 0
    board = chess.Board(board_size)
    for piece in pieces:
        if find_place(board, piece):
            continue

    import pdb; pdb.set_trace()

def main():

    parser = argparse.ArgumentParser(
        description='Build a chess board with pieces which will not threatening one to another.'
    )

    parser.add_argument(
        '--board_size',
        '-s',
        default=3,
        type=int,
        help='Number of squares in the board'
    )

    parser.add_argument(
        '--bishops',
        '-b',
        default=0,
        type=int,
        help='Number of bishops'
    )

    parser.add_argument(
        '--kinights',
        '-i',
        default=0,
        type=int,
        help='Number of kinights'
    )

    parser.add_argument(
        '--kings',
        '-k',
        default=0,
        type=int,
        help='Number of kings'
    )

    parser.add_argument(
        '--pawns',
        '-p',
        default=0,
        type=int,
        help='Number of pawns'
    )

    parser.add_argument(
        '--queens',
        '-q',
        default=0,
        type=int,
        help='Number of Queens'
    )

    parser.add_argument(
        '--rooks',
        '-r',
        default=0,
        type=int,
        help='Number of rooks'
    )

    args = parser.parse_args()

    pieces = []
    pieces += [chess.Bishop() for x in range(args.bishops)]
    pieces += [chess.Kinight() for x in range(args.kinights)]
    pieces += [chess.King() for x in range(args.kings)]
    pieces += [chess.Pawn() for x in range(args.pawns)]
    pieces += [chess.Queen() for x in range(args.queens)]
    pieces += [chess.Rook() for x in range(args.rooks)]

    if len(pieces) <= 1:
        logger.error('You must select at least 2 pieces')
        exit()

    run(args.board_size, pieces)
