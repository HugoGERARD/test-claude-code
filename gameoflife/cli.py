"""Command-line entry point for running a Game of Life simulation."""
from __future__ import annotations

import argparse
import time

from .grid import Grid

GLIDER = [(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)]


def build_grid(args: argparse.Namespace) -> Grid:
    if args.pattern == "glider":
        return Grid(args.width, args.height, GLIDER)
    return Grid.random(args.width, args.height, density=args.density, seed=args.seed)


def run(args: argparse.Namespace) -> None:
    grid = build_grid(args)
    for gen in range(args.generations):
        print(f"\033[H\033[JGeneration {gen}")
        print(grid.render())
        time.sleep(args.delay)
        grid = grid.step()


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Conway's Game of Life")
    parser.add_argument("--width", type=int, default=20)
    parser.add_argument("--height", type=int, default=10)
    parser.add_argument("--generations", type=int, default=50)
    parser.add_argument("--delay", type=float, default=0.2, help="seconds between generations")
    parser.add_argument("--density", type=float, default=0.3, help="initial live-cell density (random pattern)")
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--pattern", choices=["random", "glider"], default="random")
    args = parser.parse_args(argv)
    run(args)


if __name__ == "__main__":
    main()
