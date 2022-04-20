class Board(dict):  # Sparse matrix implementation for our purposes
    """Conway's Game of Life."""

    def __init__(self, *args, **kwargs):
        super(Board, self).__init__(*args, **kwargs)

    def __missing__(self, *args, **kwargs):
        return 0

    def get_current_cells(self):
        to_process = set()  # These are the neighbors (alive or dead) of current alive cells
        for r, c in self.keys():  # Get coordinates for each alive node
            neighbors = [(r, c),
                         (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1),
                         (r + 1, c - 1), (r + 1, c + 1),
                         (r - 1, c - 1), (r - 1, c + 1)]

            for neighbor in neighbors:
                to_process.add(neighbor)
        return to_process

    def get_neighbors(self, r, c):
        count = 0  # Start neighbor count at 0

        neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1),
                     (r + 1, c - 1), (r + 1, c + 1),
                     (r - 1, c - 1), (r - 1, c + 1)]

        for neighbor in neighbors:
            count += self[neighbor]  # self[x,y] = 1 if alive, thus sum of neighbor's values will give count

        alive, dead = set(), set()  # cells that are alive or dead w.r.t. the current state of the board
        curr = self[r, c]
        if curr == 1 and (count < 2 or count > 3):  # If alive with less than 2 neighbors or more than 3, it dies from
            dead.add((r, c))  # underpopulation/overpopulation
        elif (curr == 0 and count == 3) or (curr == 1 and (count == 2 or count == 3)):
            # If dead and has three neighbors, comes to life
            # If alive with 2/3 neighbors, remains in next generation
            alive.add((r, c))
        return alive, dead

    def swap_status(self, r, c):
        if self[r, c] == 1:
            del self[r, c]
        elif self[r, c] == 0:
            self[r, c] = 1
        return self

    def life_status(self):
        alive, dead = set(), set()  # Store current alive/dead cells
        for r, c in self.get_current_cells():  # Get alive/dead cells and get their alive/dead neighbors.
            curr_alive, curr_dead = self.get_neighbors(r, c)
            alive = alive | curr_alive
            dead = dead | curr_dead

        for x, y in dead:  # If dead and remaining in sparse matrix, we delete value.
            if self[x, y] == 1:
                del self[x, y]
        for x, y in alive:  # Otherwise we add it in.
            self[x, y] = 1
        return self
