from utils.utils import load_text_file

move_scores = {'rock': 1, 'paper': 2, 'scissors': 3}
instruction_translation = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}


def calculate_score(moves):
    total = 0

    for set in moves:
        total = total + move_scores[set[1]]

        if set[0] == set[1]:
            total = total + 3

        if set[1] == 'rock' and set[0] == 'scissors':
            total = total + 6

        if set[1] == 'paper' and set[0] == 'rock':
            total = total + 6

        if set[1] == 'scissors' and set[0] == 'paper':
            total = total + 6

    return total


def process_file(line: str):
    instructions = line.replace('\n', '').split(' ')

    moves = []

    moves.append(instruction_translation[instructions[0]])

    if instructions[1] == 'X':
        if moves[0] == 'rock':
            moves.append('scissors')
        if moves[0] == 'paper':
            moves.append('rock')
        if moves[0] == 'scissors':
            moves.append('paper')

    if instructions[1] == 'Y':
        moves.append(moves[0])

    if instructions[1] == 'Z':
        if moves[0] == 'rock':
            moves.append('paper')
        if moves[0] == 'paper':
            moves.append('scissors')
        if moves[0] == 'scissors':
            moves.append('rock')

    return moves


if __name__ == '__main__':
    moves = load_text_file('input.txt', __file__, process_file)
    print(calculate_score(moves))
