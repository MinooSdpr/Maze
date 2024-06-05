import heapq
from collections import deque

def bfs(maze):
    start_x, start_y = -1, -1
    end_x, end_y = -1, -1
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start_x, start_y = i, j
            elif maze[i][j] == 'G':
                end_x, end_y = i, j

    queue = deque([(start_x, start_y)])
    visited = set()
    parent = {}

    while queue:
        current_x, current_y = queue.popleft()
        if (current_x, current_y) == (end_x, end_y):
            path = []
            while (current_x, current_y) != (start_x, start_y):
                path.append((current_x, current_y))
                current_x, current_y = parent[(current_x, current_y)]
            return path[::-1]

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = current_x + dx, current_y + dy
            if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] != '#' and (new_x, new_y) not in visited:
                queue.append((new_x, new_y))
                visited.add((new_x, new_y))
                parent[(new_x, new_y)] = (current_x, current_y)

    return None

def print_BFS_maze(maze, path):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (i, j) in path:
                print('.', end='')
            else:
                print(maze[i][j], end='')
        print()
def print_a_star_maze(maze, path, start_x, start_y, end_x, end_y):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (i, j) == (start_x, start_y):
                print('S', end='')
            elif (i, j) == (end_x, end_y):
                print('G', end='')
            elif (i, j) in path:
                print('.', end='')
            else:
                print(maze[i][j], end='')
        print()

class Node:
    def __init__(self, x, y, g, h):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f

def is_valid(x, y, maze):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '%' and maze[x][y] != 'S'

def euclidean_distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def a_star(maze):
    start_x, start_y = -1, -1
    end_x, end_y = -1, -1
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start_x, start_y = i, j
            elif maze[i][j] == 'G':
                end_x, end_y = i, j

    open_list = [Node(start_x, start_y, 0, euclidean_distance(start_x, start_y, end_x, end_y))]
    closed_set = set()
    came_from = {}
    g_score = { (i, j): float('inf') for i in range(len(maze)) for j in range(len(maze[0])) }
    g_score[(start_x, start_y)] = 0

    while open_list:
        current = heapq.heappop(open_list)
        if current.x == end_x and current.y == end_y:
            path = []
            while (current.x, current.y) in came_from:
                path.append((current.x, current.y))
                current = came_from[(current.x, current.y)]
            path.append((start_x, start_y))
            path.reverse()
            return path

        closed_set.add((current.x, current.y))

        for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_x, new_y = current.x + i, current.y + j
            if is_valid(new_x, new_y, maze) and (new_x, new_y) not in closed_set:
                tentative_g_score = current.g + 1
                if tentative_g_score < g_score[(new_x, new_y)]:
                    came_from[(new_x, new_y)] = current
                    g_score[(new_x, new_y)] = tentative_g_score
                    f_score = tentative_g_score + euclidean_distance(new_x, new_y, end_x, end_y)
                    heapq.heappush(open_list, Node(new_x, new_y, tentative_g_score, f_score))

    return None


def main(filepath, method):
    if method == 'a':
        with open(filepath, 'r') as file:
            maze = [list(line.strip()) for line in file]

        start_x, start_y = -1, -1
        end_x, end_y = -1, -1
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j] == 'S':
                    start_x, start_y = i, j
                elif maze[i][j] == 'G':
                    end_x, end_y = i, j

        path = a_star(maze)
        if path:
            print_a_star_maze(maze, path, start_x, start_y, end_x, end_y)
        else:
            print("No path found")
    elif method == 'b':
        with open(filepath, 'r') as file:
            maze = [list(line.strip()) for line in file]

            path = bfs(maze)
            if path:
                print_BFS_maze(maze, path)
            else:
                print("No path found")

if __name__ == "__main__":
    path = input('Enter maze file path to find way: ')
    method = input('Enter the algorithm b for BFS and a for A*: ').lower()
    main(path,method)