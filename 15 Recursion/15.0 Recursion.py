def gcd(x, y):
    """
    GCD: greatest common divisor of x, y
    """
    return x if y == 0 else gcd(y, x % y)

"""
Tiling Problem using Divide and Conquer algorithm

// n is size of given square, p is location of missing cell
Tile(int n, Point p)

1) Base case: n = 2, A 2 x 2 square with one cell missing is nothing 
   but a tile and can be filled with a single tile.

2) Place a L shaped tile at the center such that it does not cover
   the n/2 * n/2 subsquare that has a missing square. Now all four 
   subsquares of size n/2 x n/2 have a missing cell (a cell that doesn't
   need to be filled).  See figure 2 below.

3) Solve the problem recursively for following four. Let p1, p2, p3 and
   p4 be positions of the 4 missing cells in 4 squares.
   a) Tile(n/2, p1)
   b) Tile(n/2, p2)
   c) Tile(n/2, p3)
   d) Tile(n/2, p3) 

visual: https://www.geeksforgeeks.org/tiling-problem-using-divide-and-conquer-algorithm/
"""


def tile_filling(size, missing_point):
    """

    :param size:
    :param missing_point:
    :return:
    """

