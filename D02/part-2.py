input_file = open('input.txt')

result_scores = {
    'A X': 3 + 0, # scissors score + lose score
    'B X': 1 + 0, # rock score     + lose score
    'C X': 2 + 0, # paper score    + lose score
    'A Y': 1 + 3, # rock score     + draw score
    'B Y': 2 + 3, # paper score    + draw score
    'C Y': 3 + 3, # scissors score + draw score
    'A Z': 2 + 6, # paper score    + win score
    'B Z': 3 + 6, # scissors score + win score
    'C Z': 1 + 6  # rock score     + win score
}

from functools import reduce

def sum_score(acc: int, round: str):
    return acc + result_scores.get(round.strip())

total_score = reduce(sum_score, input_file, 0)

# Solution: 10560
print(total_score)
