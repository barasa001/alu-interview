#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Given a single-character text editor with only the character 'H',
    calculate the minimum number of operations
    needed to transform the editor into one that has `n` 'H' characters.
    
    Args:
    n: an integer representing the desired number of 'H' characters in the editor.
    
    Returns:
    An integer representing the minimum number of
    operations required to achieve `n` 'H' characters.
    """
    
    if n <= 1:
        return 0
    Argmnt, evn, Operations = n, 2, 0

    while Argmnt > 1:
        if Argmnt % evn == 0:
            Argmnt = Argmnt / evn
            Operations = Operations + evn
        else:
            evn += 1
    return Operations
