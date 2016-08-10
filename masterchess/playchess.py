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

def run(board_size, bishops, kinights, kings, pawns, queens, rooks):

    logger.info('Playing Chess')
    logger.info('Board size: %d' % board_size)
    logger.info('Pieces of bishops: %d' % bishops)
    logger.info('Pieces of kinights: %d' % kinights)
    logger.info('Pieces of kings: %d' % kings)
    logger.info('Pieces of pawns: %d' % pawns)
    logger.info('Pieces of queens: %d' % queens)
    logger.info('Pieces of rooks: %d' % rooks)

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

    pieces = sum([args.bishops,
        args.kinights,
        args.kings,
        args.pawns,
        args.queens,
        args.rooks]
    )

    if pieces <= 1:
        logger.error('You must select at least 2 pieces')
        exit()

    run(
        args.board_size,
        args.bishops,
        args.kinights,
        args.kings,
        args.pawns,
        args.queens,
        args.rooks
    )