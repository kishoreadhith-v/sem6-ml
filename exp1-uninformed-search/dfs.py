from maze_sol_print import  *

maze = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

def bfs(maze, start, goal):
    r = len(maze)
    c = len(maze[0])
    frontier = [(start, [])]
    visited = set()

    while frontier:
        cur, path = frontier.pop()
        if cur in visited:
            continue

        visited.add(cur)

        if cur == goal:
            path.append(cur)
            return path

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = cur[0] + dx, cur[1] + dy
            if 0 <= x < c and 0 <= y < r and maze[x][y] == 0:
                p = path + [(cur[0], cur[1])]
                frontier.append(((x, y), p))

start = (0, 0)
goal = (4, 4)
sol = bfs(maze, start, goal)

print_sol(maze, start, goal, sol)