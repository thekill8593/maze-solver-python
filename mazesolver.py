class MazeSolver:
    def __init__(self):
        with open('maze.txt', 'r') as f:
            self.maze = [[int(num) for num in line.split(' ')] for line in f]
        self.visited = [[False for _ in range(len(self.maze))] for _ in range(len(self.maze))]
        self.end_of_map = len(self.maze)
        self.path = {}
        try:
            self.solve_maze(0, 0)
        except:
            print('FOUND')
        self.print_path()

    def solve_maze(self, row, col):

        if row < 0 or row >= self.end_of_map:
            return
        if col < 0 or col >= self.end_of_map:
            return

        if self.maze[row][col] == 3:
            raise Exception('FOUND')

        if self.maze[row][col] == 0:
            self.visited[row][col] = True
            return

        if self.visited[row][col]:
            return

        self.path[f'{row}{col}'] = '*'
        print(f"Recursion on row:{row} col:{col}")

        self.visited[row][col] = True
        self.solve_maze(row + 1, col)
        self.solve_maze(row, col + 1)
        self.solve_maze(row, col - 1)
        self.solve_maze(row - 1, col)

    def print_path(self):
        for row in range(len(self.maze)):
            print('')
            for col in range(len(self.maze)):
                if self.path.get(f'{row}{col}') is not None:
                    print('*', end=" ", flush=True),
                else:
                    print(self.maze[row][col], end=" ", flush=True),

maze = MazeSolver()