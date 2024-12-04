def print_sol(maze, start, goal, sol):
    res = maze[:]
    for i, j in sol:
        res[i][j] = 'x'

    res[start[0]][start[1]] = 'S'
    res[goal[0]][goal[1]] = 'G'

    for r in res:
        for c in r:
            print(c, end = ' ')
        print()
