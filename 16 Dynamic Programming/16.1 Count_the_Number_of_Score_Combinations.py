def num_combinations_for_final_score(final_score, individual_play_scores):

    # tabulation / data structure for bottom up DP cache
    num_combinations_for_score = [[1] + [0] * final_score for _ in individual_play_scores]

    for i in range(len(individual_play_scores)):
        for j in range(1, final_score + 1):
            # solution for sub problem
            without_this_play = num_combinations_for_score[i - 1][j] if i >=1 else 0
            with_this_play = num_combinations_for_score[i][j - individual_play_scores[i]]\
                if j >= individual_play_scores[i] else 0
            num_combinations_for_score[i][j] = (without_this_play + with_this_play)
    return num_combinations_for_score[-1][-1]


input = (12, [2, 3, 7])
print(num_combinations_for_final_score(input[0], input[1]))


final_score, individual_play_scores = 12, [2, 3, 7]
import collections

def num_sequences_for_final_score(final_score, individual_play_scores):
    # too difficult to solve this
    pass

def climbing_stairs(n, k):
    """

    :param n: destination is exactly n steps up
    :param k: you can advance 1 to k steps ata time
    :return: number of ways in which you can get to the destination
    """
    climbing_stairs(n-1, k-1)+ ... +climbing_stairs(n-k+1, 1)


