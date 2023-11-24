import collections


class LifeGrid:
    def __init__(self, pattern):
        self.pattern = pattern

    def evolve(self):
        neighbours = {
            (-1, -1),  # Above left
            (-1, 0),  # Above
            (-1, 1),  # Above right
            (0, -1),  # Left
            (0, 1),  # Right
            (1, -1),  # Below left
            (1, 0),  # Below
            (1, 1),  # Below right
        }

        num_neightbours = collections.defaultdict(int)
        for row, col in self.pattern.alive_cells:
            for drow, dcol in neighbours:
                num_neightbours[(row + drow, col + dcol)] += 1

        stay_alive = {
            cell for cell, num  in num_neightbours.items() if num in {2, 3}
        } & self.pattern.alive_cells
        come_alive = {
            cell for cell, num in num_neightbours.items() if num == 3
        } - self.pattern.alive_cells

        self.pattern.alive_cells = stay_alive | come_alive

    def as_string(self, bbox):
        pass

    def __str__(self):
        return (
            f"{self.pattern.name}:\n"
            f"Alive cells -> {sorted(self.pattern.alive_cells)}"
        )
