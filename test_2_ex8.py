from ex8 import *
import io
import contextlib
import itertools
import copy


def capture_print(fun):
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        fun()
    retval = f.getvalue().strip().split("\n")
    # because splitting an empty string(e.g, nothing was printed) gives
    # an empty string in the list for some reason
    if retval == [""]:
        return []
    return retval


def test_3b3_sudoku():
    board = [
        [2, 1, 4, 3],
        [4, 3, 0, 1],
        [3, 4, 1, 2],
        [0, 0, 0, 4]
    ]
    assert solve_sudoku(board)
    assert board == [
        [2, 1, 4, 3],
        [4, 3, 2, 1],
        [3, 4, 1, 2],
        [1, 2, 3, 4]
    ]


def test_4b4_sudoku():
    board = [
        [2, 4, 3, 1],
        [1, 0, 2, 4],
        [4, 0, 1, 0],
        [3, 1, 0, 0]
    ]
    assert solve_sudoku(board)
    assert board == [
        [2, 4, 3, 1],
        [1, 3, 2, 4],
        [4, 2, 1, 3],
        [3, 1, 4, 2]
    ]


def test_6b6_sudoku():
    board = [
        [2, 1, 5, 3, 4, 6],
        [3, 0, 0, 2, 0, 0],
        [5, 0, 0, 0, 0, 4],
        [0, 2, 4, 5, 0, 0],
        [4, 0, 0, 0, 0, 5],
        [1, 5, 3, 4, 6, 2]
    ]
    assert solve_sudoku(board)


def assert_subset_works(n, k, expected):
    via_print = capture_print(lambda: print_k_subsets(n, k))
    assert len(via_print) == len(expected)
    assert set(str(ex) for ex in expected) == set(via_print)

    via_fill = []
    fill_k_subsets(n, k, via_fill)
    assert sorted(expected) == sorted(via_fill)

    via_return = return_k_subsets(n, k)
    assert sorted(expected) == sorted(via_return)


def test_n3k2_subsets():
    assert_subset_works(3, 2, [[0, 1], [0, 2], [1, 2]])


def test_subsets_general():
    for n in range(16):
        for k in range(0, n + 1):
            correct_subsets = [list(t) for t in
                               itertools.combinations(range(n), k)]
            assert_subset_works(n, k, correct_subsets)


def test_edgecase_subsets():
    for n in range(16):
        # the empty set is a subset of length 0 for every set
        assert_subset_works(n, 0, [[]])


def test_unsolveable_sudoku():
    unsolveable = [
        [1, 4, 2, 0, 3, 0, 0, 0, 0],
        [0, 7, 0, 4, 6, 0, 0, 5, 0],
        [0, 3, 0, 7, 8, 1, 0, 9, 0],
        [4, 0, 0, 0, 0, 7, 2, 6, 5],
        [0, 6, 7, 0, 0, 0, 0, 8, 0],
        [2, 9, 8, 6, 0, 3, 0, 0, 4],
        [0, 8, 0, 5, 0, 4, 9, 0, 0],
        [0, 2, 6, 3, 0, 0, 0, 0, 0],
        [7, 0, 4, 9, 2, 6, 0, 3, 1],
    ]
    unsolveable_dup = copy.deepcopy(unsolveable)
    assert not solve_sudoku(unsolveable_dup)
    assert unsolveable_dup == unsolveable


# everything above finished almost instantly for me
# this took about 5~ minutes to run on an i5-7300hq
def test_another_hard_sudoku():
    board = [[0, 0, 0, 7, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 4, 3, 0, 2, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 6],
             [0, 0, 0, 5, 0, 9, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 4, 1, 8],
             [0, 0, 0, 0, 8, 1, 0, 0, 0],
             [0, 0, 2, 0, 0, 0, 0, 5, 0],
             [0, 4, 0, 0, 0, 0, 3, 0, 0]]
    assert solve_sudoku(board)


# this test took about 16~ minutes to run on an i5-7300hq
def test_difficult_bruteforce_sudoku_9b9():
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 8, 5],
        [0, 0, 1, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 7, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 1, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 7, 3],
        [0, 0, 2, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 9]
    ]
    assert solve_sudoku(board)
