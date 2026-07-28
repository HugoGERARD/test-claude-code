"""Core logic for Conway's Game of Life."""
from __future__ import annotations

import random
from typing import Iterable


class Grid:
    """A toroidal (wrap-around) Game of Life grid."""

    def __init__(self, width: int, height: int, cells: Iterable[tuple[int, int]] = ()):
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be positive")
        self.width = width
        self.height = height
        self.cells: set[tuple[int, int]] = set(cells)

    @classmethod
    def random(cls, width: int, height: int, density: float = 0.3, seed: int | None = None) -> "Grid":
        rng = random.Random(seed)
        cells = {
            (x, y)
            for x in range(width)
            for y in range(height)
            if rng.random() < density
        }
        return cls(width, height, cells)

    def is_alive(self, x: int, y: int) -> bool:
        return (x % self.width, y % self.height) in self.cells

    def live_neighbors(self, x: int, y: int) -> int:
        count = 0
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                if self.is_alive(x + dx, y + dy):
                    count += 1
        return count

    def step(self) -> "Grid":
        """Return a new Grid representing the next generation."""
        next_cells: set[tuple[int, int]] = set()
        for x in range(self.width):
            for y in range(self.height):
                neighbors = self.live_neighbors(x, y)
                alive = self.is_alive(x, y)
                if alive and neighbors in (2, 3):
                    next_cells.add((x, y))
                elif not alive and neighbors == 3:
                    next_cells.add((x, y))
        return Grid(self.width, self.height, next_cells)

    def render(self, alive_char: str = "#", dead_char: str = ".") -> str:
        rows = []
        for y in range(self.height):
            row = "".join(
                alive_char if (x, y) in self.cells else dead_char
                for x in range(self.width)
            )
            rows.append(row)
        return "\n".join(rows)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Grid):
            return NotImplemented
        return (
            self.width == other.width
            and self.height == other.height
            and self.cells == other.cells
        )
