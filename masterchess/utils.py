# coding: utf-8


def pretty_print(matrix):
    """
    Print a matrix in a pretty print format:

    Atributes:

    matrix -- convensional x, y 2D list
    input ex:
        [
            ['pawn', None, None],
            [None, None, 'king'],
            [None, None, None]
        ]
    output ex:
        None    king    None
        None    None    None
        pawn    None    None
    """

    return '\r\n'.join(
        ['\t'.join([str(x) for x in i]) for i in zip(*matrix)][::-1]
    )
