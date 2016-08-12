Master Chess
============

Console Script that implements a Chess Challenge.

The problem is to find all unique configurations of a set of normal chess pieces on a chess board with dimensions M×N where none of the pieces is in a position to take any of the others. Assume the colour of the piece does not matter, and that there are no pawns among the pieces.

Write a program which takes as input:

The dimensions of the board: M, N

The number of pieces of each type (King, Queen, Bishop, Rook and Knight) to try and place on the board.

As output, the program should list all the unique configurations to the console for which all of the pieces can be placed on the board without threatening each other.

How to install
==============

PIPY
----

pip install fbcs_chess_challenge

Github
------

* Download the package from Github
* python setup.py install

Run tests
=========

python setup.py tests

or

python setup.py nosetests --with-coverage

Run Console Script
==================

For Help
--------

(chessmaster)MacBook-Pro:chess_master fabiobatalha$ playchess --help

    usage: playchess [-h] [--board_size BOARD_SIZE] [--bishops BISHOPS]
                     [--kinights KINIGHTS] [--kings KINGS] [--pawns PAWNS]
                     [--queens QUEENS] [--rooks ROOKS] [--show_threatening]

    Build a chess board with pieces which will not threatening one to another.

    optional arguments:
      -h, --help            show this help message and exit
      --board_size BOARD_SIZE, -s BOARD_SIZE
                            Number of squares in the board
      --bishops BISHOPS, -b BISHOPS
                            Number of bishops
      --kinights KINIGHTS, -i KINIGHTS
                            Number of kinights
      --kings KINGS, -k KINGS
                            Number of kings
      --pawns PAWNS, -p PAWNS
                            Number of pawns
      --queens QUEENS, -q QUEENS
                            Number of Queens
      --rooks ROOKS, -r ROOKS
                            Number of rooks
      --show_threatening, -t
                            Show threatening places display T in the board when
                            printing the results, otherwise None will be displayed

Running Sample
--------------

(chessmaster)MacBook-Pro:chess_master fabiobatalha$ playchess -s 4 -i 4 -r 2

    2016-08-12 01:22:11,660 - masterchess.playchess - INFO - Playing Chess
    2016-08-12 01:22:11,661 - masterchess.playchess - INFO - Board size: 4
    2016-08-12 01:22:11,661 - masterchess.playchess - INFO - Pieces of bishops: 0
    2016-08-12 01:22:11,661 - masterchess.playchess - INFO - Pieces of kinights: 4
    2016-08-12 01:22:11,661 - masterchess.playchess - INFO - Pieces of kings: 0
    2016-08-12 01:22:11,661 - masterchess.playchess - INFO - Pieces of pawns: 0
    2016-08-12 01:22:11,661 - masterchess.playchess - INFO - Pieces of queens: 0
    2016-08-12 01:22:11,662 - masterchess.playchess - INFO - Pieces of rooks: 2
    Number of possibilities: 8

    Game 1:
    rook    None    None    None
    None    kinight None    kinight
    None    None    rook    None
    None    kinight None    kinight

    Game 2:
    None    kinight None    kinight
    rook    None    None    None
    None    kinight None    kinight
    None    None    rook    None

    Game 3:
    None    rook    None    None
    kinight None    kinight None
    None    None    None    rook
    kinight None    kinight None

    Game 4:
    kinight None    kinight None
    None    rook    None    None
    kinight None    kinight None
    None    None    None    rook

    Game 5:
    None    None    None    rook
    kinight None    kinight None
    None    rook    None    None
    kinight None    kinight None

    Game 6:
    None    None    rook    None
    None    kinight None    kinight
    rook    None    None    None
    None    kinight None    kinight

    Game 7:
    kinight None    kinight None
    None    None    None    rook
    kinight None    kinight None
    None    rook    None    None

    Game 8:
    None    kinight None    kinight
    None    None    rook    None
    None    kinight None    kinight
    rook    None    None    None

Running Sample Displaying Threatening places
--------------------------------------------

(chessmaster)MacBook-Pro:chess_master fabiobatalha$ playchess -s 4 -i 4 -r 2

    2016-08-12 01:10:03,481 - masterchess.playchess - INFO - Playing Chess
    2016-08-12 01:10:03,481 - masterchess.playchess - INFO - Board size: 4
    2016-08-12 01:10:03,481 - masterchess.playchess - INFO - Pieces of bishops: 0
    2016-08-12 01:10:03,481 - masterchess.playchess - INFO - Pieces of kinights: 4
    2016-08-12 01:10:03,481 - masterchess.playchess - INFO - Pieces of kings: 0
    2016-08-12 01:10:03,481 - masterchess.playchess - INFO - Pieces of pawns: 0
    2016-08-12 01:10:03,482 - masterchess.playchess - INFO - Pieces of queens: 0
    2016-08-12 01:10:03,482 - masterchess.playchess - INFO - Pieces of rooks: 2
    Number of possibilities: 8

    Game 1:
    kinight T   kinight T
    T   T   T   rook
    kinight T   kinight T
    T   rook    T   T

    Game 2:
    T   kinight T   kinight
    T   T   rook    T
    T   kinight T   kinight
    rook    T   T   T

    Game 3:
    kinight T   kinight T
    T   rook    T   T
    kinight T   kinight T
    T   T   T   rook

    Game 4:
    rook    T   T   T
    T   kinight T   kinight
    T   T   rook    T
    T   kinight T   kinight

    Game 5:
    T   T   T   rook
    kinight T   kinight T
    T   rook    T   T
    kinight T   kinight T

    Game 6:
    T   kinight T   kinight
    rook    T   T   T
    T   kinight T   kinight
    T   T   rook    T

    Game 7:
    T   T   rook    T
    T   kinight T   kinight
    rook    T   T   T
    T   kinight T   kinight

    Game 8:
    T   rook    T   T
    kinight T   kinight T
    T   T   T   rook
    kinight T   kinight T

Build status
============

.. image:: https://travis-ci.org/fabiobatalha/chess_master.svg?branch=master
    :target: https://travis-ci.org/fabiobatalha/chess_master
