import random
from collections import deque

# Constants
WALL = "▓"
OPEN_SPACE = "◌"
START = "S"
END = "E"
PATH = "◍"

def generate_maze(size):
    maze = [[WALL for _ in range(size)] for _ in range(size)]
    start = (1, 1)
    end = (size - 2, size - 2)
    maze[start[0]][start[1]] = START
    maze[end[0]][end[1]] = END

    walls = [(i, j) for i in range(1, size-1, 2) for j in range(1, size-1, 2)]
    random.shuffle(walls)

    for wall in walls:
        x, y = wall
        maze[x][y] = OPEN_SPACE

    return maze

# Maze Printing Function
def print_maze(maze):
    for row in maze:
        print(" ".join(row))

# Breadth-First Search (BFS) for Pathfinding
def bfs(maze):
    start = (1, 1)
    end = (len(maze) - 2, len(maze[0]) - 2)

    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            return path

        if (x, y) not in visited:
            visited.add((x, y))

            neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            neighbors = [(nx, ny) for nx, ny in neighbors if 0 < nx < len(maze) and 0 < ny < len(maze[0])]

            for nx, ny in neighbors:
                if maze[nx][ny] == OPEN_SPACE and (nx, ny) not in visited:
                    queue.append(( (nx, ny), path + [(nx, ny)] ))

    return None

# Path Marking Function
def mark_path(maze, path):
    if path:
        for x, y in path:
            maze[x][y] = PATH
        return maze
    return None

# Path Printing Function
def print_path(maze):
    if maze is None:
        print("No path found.")
    else:
        print_maze(maze)

# Main Function
def main():
    size = int(input("Enter the size of the maze (n): "))
    
    maze = generate_maze(size)
    
    print("\nGenerated Maze:")
    print_maze(maze)

    while True:
        print("\nOptions:")
        print("1. Print Path")
        print("2. Generate Another Puzzle")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            path = bfs([row[:] for row in maze])
            marked_path = mark_path([row[:] for row in maze], path)
            print("\nPath:")
            print_path(marked_path)
        elif choice == '2':
            maze = generate_maze(size)
            print("\nGenerated Maze:")
            print_maze(maze)
        elif choice == '3':
            print("Exiting. Thank you for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()