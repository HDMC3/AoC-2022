input_file = open('input.txt')

result_scores = {
    'A Z': 3 + 0, # scissors score + draw score
    'C Y': 2 + 0, # paper score    + draw score
    'B X': 1 + 0, # rock score     + draw score
    'A X': 1 + 3, # rock score     + lose score
    'B Y': 2 + 3, # paper score    + lose score
    'C Z': 3 + 3, # scissors score + lose score
    'C X': 1 + 6, # rock score     + win score
    'B Z': 3 + 6, # scissors score + win score
    'A Y': 2 + 6  # paper score    + win score
}

from functools import reduce

def sum_score(acc: int, round: str):
    return acc + result_scores.get(round.strip())

total_score = reduce(sum_score, input_file, 0)

# Solution: 9651
print(total_score)
