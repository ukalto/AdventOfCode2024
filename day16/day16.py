import heapq

def read_input():
    with open('day16', 'r') as file:
        maze = []
        start, end = None, None
        for row in file.readlines():
            temp = []
            for char in row.strip():
                temp.append(char)
                if char == 'S':
                    start = (len(maze), len(temp) - 1)
                elif char == 'E':
                    end = (len(maze), len(temp) - 1)
            maze.append(temp)
        return maze, start, end

DIRECTIONS = {
    'UP': (-1, 0),
    'DOWN': (1, 0),
    'LEFT': (0, -1),
    'RIGHT': (0, 1),
}

def turn_cost(current_direction, new_direction):
    if current_direction == new_direction:
        return 1
    return 1001

def solve_puzzle(maze, start, end):
    rows, cols = len(maze), len(maze[0])

    heap = []
    heapq.heappush(heap, (0, start[0], start[1], 'RIGHT'))
    visited = {}

    while heap:
        cost, x, y, direction = heapq.heappop(heap)
        if (x, y) == end:
            print(cost)
            return

        if (x, y, direction) in visited and visited[(x, y, direction)] <= cost:
            continue
        visited[(x, y, direction)] = cost

        for new_direction, (dx, dy) in DIRECTIONS.items():
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != '#':
                new_cost = cost + turn_cost(direction, new_direction)
                heapq.heappush(heap, (new_cost, nx, ny, new_direction))

if __name__ == '__main__':
    maze, start, end = read_input()
    solve_puzzle(maze, start, end)