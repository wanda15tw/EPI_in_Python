WHITE, BLACK = range(2)

import collections

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

def search_maze(maze, s, e):
    # perform DFS to find a feasible path
    def search_maze_helper(cur):
        # checks cur is within maze and is a white pixel
        if not (0 <= cur.x < len(maze) and 0 <= cur.y < len(maze[cur.x]) and maze[cur.x][cur.y] == WHITE):
            return False
        path.append(cur)
        maze[cur.x][cur.y] = BLACK
        if cur == e:
            return True

        if any(map(search_maze_helper, (Coordinate(cur.x - 1, cur.y), Coordinate(cur.x+1, cur.y), \
                                        Coordinate(cur.x, cur.y - 1), Coordinate(cur.x, cur.y+1)))):
            return True

        # cannot find a path, remove the entery added in path.append(cur).
        del path[-1]
        return False

    path = []
    if not search_maze_helper(s):
        return [] # no path between s and e
    return path