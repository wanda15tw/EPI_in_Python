NUM_PEGS = 3

def compute_tower_hanoi(num_rings):
    def compute_tower_hanoi_steps(num_rings_to_move, from_peg, to_peg, use_peg):
        if num_rings_to_move > 0:
            compute_tower_hanoi_steps(num_rings_to_move - 1, from_peg, use_peg, to_peg)
            pegs[to_peg].append(pegs[from_peg].pop())
            result.append([from_peg, to_peg])
            compute_tower_hanoi_steps(num_rings_to_move - 1, use_peg, to_peg, from_peg)

    result = []
    pegs = [list(reversed(range(1, num_rings + 1)))] + [[] for _ in range(1, NUM_PEGS)]
    compute_tower_hanoi_steps(num_rings, 0, 1, 2)
    return result


print(compute_tower_hanoi(1))
print(compute_tower_hanoi(2))
print(compute_tower_hanoi(3))



def hanoi(num_rings):
    """

    :param num_rings:
    :return: result: a list of moves [[from_peg, to_peg], ...]
    """
    def hanoi_moves(num_rings, from_peg, to_peg, use_peg):
        """
        internal function to recursively compute the move of the moment
        :param num_rings:
        :param from_peg:
        :param to_peg:
        :param use_peg:
        :return: move = [from_peg, to_peg]
        """
        # base case
        if num_rings == 1:
            result.append([from_peg, to_peg])
            return

        # when n > 1, first move n - 1 rings from 0 to 2
        hanoi_moves(num_rings-1, from_peg, use_peg, to_peg)
        hanoi_moves(1, from_peg, to_peg, use_peg)
        hanoi_moves(num_rings-1, use_peg, to_peg, from_peg)

    result = []
    hanoi_moves(num_rings, 0, 1, 2)
    return result


for i in range(1, 4):
    print(hanoi(i))