from gameoflife import Grid


def test_grid_rejects_invalid_size():
    try:
        Grid(0, 5)
        assert False, "expected ValueError"
    except ValueError:
        pass


def test_is_alive_and_wraparound():
    grid = Grid(3, 3, cells=[(0, 0)])
    assert grid.is_alive(0, 0)
    assert grid.is_alive(3, 0)  # wraps around width
    assert grid.is_alive(0, -3)  # wraps around height
    assert not grid.is_alive(1, 1)


def test_live_neighbors_counts_correctly():
    grid = Grid(3, 3, cells=[(0, 0), (1, 0), (0, 1)])
    assert grid.live_neighbors(1, 1) == 3


def test_still_life_block_is_stable():
    block = [(1, 1), (2, 1), (1, 2), (2, 2)]
    grid = Grid(4, 4, block)
    next_grid = grid.step()
    assert next_grid == grid


def test_blinker_oscillates():
    # Grid large enough that the pattern doesn't interact with its own
    # wrapped copies across the torus boundary.
    blinker = [(2, 1), (2, 2), (2, 3)]
    grid = Grid(5, 5, blinker)
    gen1 = grid.step()
    gen2 = gen1.step()
    assert gen1.cells == {(1, 2), (2, 2), (3, 2)}
    assert gen2 == grid


def test_underpopulation_kills_lone_cell():
    grid = Grid(3, 3, cells=[(1, 1)])
    assert grid.step().cells == set()


def test_overpopulation_kills_cell():
    grid = Grid(3, 3, cells=[(1, 1), (0, 0), (0, 1), (0, 2), (2, 2)])
    assert (1, 1) not in grid.step().cells


def test_reproduction_creates_cell():
    grid = Grid(3, 3, cells=[(0, 0), (1, 0), (0, 1)])
    assert (1, 1) in grid.step().cells


def test_render_shape():
    grid = Grid(3, 2, cells=[(0, 0)])
    rendered = grid.render()
    lines = rendered.split("\n")
    assert len(lines) == 2
    assert len(lines[0]) == 3
    assert lines[0][0] == "#"


def test_random_grid_is_deterministic_with_seed():
    a = Grid.random(5, 5, density=0.5, seed=42)
    b = Grid.random(5, 5, density=0.5, seed=42)
    assert a == b
