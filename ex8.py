EMPTY = 0


def num_in_row(num, sud, orig_row):
    """
    A function that checks whether a number appears in a particular column.
    :param num: Integer, to check if it appears
    :param sud: List of lists, represents Sudoku
    :param orig_row: Integer, the column to check
    :return: Boolean, whether the number appears in the column
    """
    for col in range(len(sud)):
        if sud[col][orig_row] == num:
            return True
    return False


def num_in_square(num, sud, orig_col, orig_row):
    """
    A function that checks whether a number appears in an inner square
    :param num: Integer, to check if it appears
    :param sud: List of lists, represents Sudoku
    :param orig_col: Integer, column, whose internal square is to be checked
    :param orig_row: Integer, Row, whose internal square is to be checked
    :return: Boolean, whether the number appears in the inner square
    """
    big_squares = int(len(sud) ** 0.5)
    # Find the location of the inner square-
    big_col = orig_col // big_squares
    big_row = orig_row // big_squares

    # Scanning the entire inner square-
    for col in range(big_col*big_squares, (big_col+1)*big_squares):
        for row in range(big_row * big_squares, (big_row + 1) * big_squares):
            if sud[col][row] == num:
                return True
    return False


def get_possible_numbers(sud, col, row):
    """
    A function that calculates for a cell in Sudoku, set of all the
    numbers "rules" to assign to it
    :param sud: List of lists, represents Sudoku
    :param col: Integer, column coordinate
    :param row: Integer, line cordiality
    :return: set, collects all valid numbers for a particular location
    """
    set_of_possible = set()

    for i in range(1, len(sud)+1):
        if i not in sud[col] and not num_in_row(i, sud, row)\
                and not num_in_square(i, sud, col, row):
            set_of_possible.add(i)

    return set_of_possible


def solve_sudoku(sud):
    """
    A function that checks whether Sudoku can be solved,
    If so, updates Sudoku to be the solution,
    if not leaving the original Sudoku.
    Returns whether or not it succeeded.
    :param sud: List of lists, represents Sudoku
    :return: Boolean, Has Sudoku been solved
    """
    # Search all empty cells in Sudoku-
    for col in range(len(sud)):
        for row in range(len(sud[0])):
            if sud[col][row] == EMPTY:
                possible_numbers = get_possible_numbers(sud, col, row)

                # If there is an empty cell and no options,go back in recursion
                if len(possible_numbers) == 0:
                    return False

                # For each option, put it in place -
                # and try to continue solving the soduko
                for option in possible_numbers:
                    sud[col][row] = option
                    # If you succeed, True will return
                    if solve_sudoku(sud):
                        return True
                    else:
                        # If you can not solve it, return the cell to blank,
                        sud[col][row] = EMPTY
                return False  # All options are not good - go back in recursion

    return True  # All cells are full - we've finished solving


#############################################################################
#   part 2-                                                                 #
#############################################################################

def print_k_subsets(n, k, from_n=0, tap=tuple()):
    """
    A recursive function that prints sorted subsets in size k from (0,...,n-1)
    :param n: Integer, Primary group size
    :param k: Integer, subsets groups size
    :param from_n: Integer, minimum current main group.
        Default - 0
    :param tap: tuple, sub-current group.
        Default - Empty.
    """
    # Validation k
    if k < 0:
        print([])
        return

    if k == 0:
        # Case handling k = 0
        if len(tap) == 0:
            print([])
            return
        print(list(tap))
        return

    for i in range(from_n, n):
        print_k_subsets(n, k - 1, i + 1, tap + tuple([i]))


def fill_k_subsets(n, k, tot_list):
    """
    A function that fill in list all sorted subsets in
    size k from (0,...,n-1)
    :param n: Integer, Primary group size
    :param k: Integer, subsets groups size
    :param tot_list: list to fill
    """
    if k <= 0:
        tot_list.append([])
        return
    if n < k:
        return

    cur_set = [False]*n
    fill_k_subsets_helper(k, tot_list, cur_set, 0, 0)


def fill_set(tot_list, cur_set):
    """
    A function updates the collection list, according to the subgroup that
    the list of booleans represents
    :param tot_list: list to fill
    :param cur_set: A list of Boolean values, representing which organs to add
    """
    new_list = []
    for (index, cell) in enumerate(cur_set):
        if cell:
            new_list.append(index)
    tot_list.append(new_list)


def fill_k_subsets_helper(k, tot_list, cur_set, index, picked):
    """
    Recursive helper function, to fill_k_subsets function/
    fill in list all sorted subsets in size k
    :param k: Integer, subsets groups size
    :param tot_list: list to fill
    :param cur_set: A list of Boolean values, representing which organs to add
    :param index: integer, Current Index
    :param picked: Integer number, number of items already "taken"
    """
    if k == picked:
        fill_set(tot_list, cur_set)
        return
    if index == len(cur_set):
        return

    cur_set[index] = True
    fill_k_subsets_helper(k, tot_list, cur_set, index+1, picked+1)

    cur_set[index] = False
    fill_k_subsets_helper(k, tot_list, cur_set, index+1, picked)


def return_k_subsets(n, k, index=1):
    """
      A recursive function that return list with all sorted subsets in
      size k from (0,...,n-1)
      :param n: Integer, Primary group size
      :param k: Integer, subsets groups size
      :param index: Integer, Location of the recursion
      Default - 1
      """
    # Input test-
    if k <= 0:
        return [[]]
    if n < k:
        return []

    #  base case
    if index == k:
        return [[i] for i in range(n-k+1)]

    if index < n:
        work_list = return_k_subsets(n, k, index + 1)

        new_list = []
        for cell in work_list:
            for i in range(cell[-1]+1, n):
                new_list.append(cell + [i])
        return new_list
