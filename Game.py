"""
This code uses alpha-beta-pruning to find the optimal solution.
"""


class Game:
    def __init__(self):
        self.turn = 'X'
        self.state = [['_', '_', '_'],
                      ['_', '_', '_'],
                      ['_', '_', '_']]
        self.result = None

    def print_state(self):

        for i in range(0, 3):
            for j in range(0, 3):
                if j < 2:
                    print('{} |'.format(self.state[i][j]), end=" ")
                else:
                    print('{} '.format(self.state[i][j]), end=" ")
            if i < 2:
                print("\n----------")
        print("\n")

    # Is the move valid?
    def is_valid(self, x, y):
        if x < 0 or x > 2 or y < 0 or y > 2:  # Out of bounds.
            return False
        elif self.state[x][y] != '_':  # Position is filled already.
            return False
        else:
            return True

    # is the game over? if so who won?
    def check_end(self):
        # horizontal win
        for i in range(0, 3):
            if self.state[i] == ['X', 'X', 'X']:
                return 'X'
            elif self.state[i] == ['O', 'O', 'O']:
                return 'O'
        # vertical win
        for i in range(0, 3):
            if (self.state[0][i] != '_' and
                    self.state[0][i] == self.state[1][i] and
                    self.state[1][i] == self.state[2][i]):
                return self.state[0][i]
        # diag1 win
        if (self.state[0][0] != '_' and
                self.state[0][0] == self.state[1][1] and
                self.state[0][0] == self.state[2][2]):
            return self.state[0][0]
        # diag2 win
        if (self.state[0][2] != '_' and
                self.state[0][2] == self.state[1][1] and
                self.state[0][2] == self.state[2][0]):
            return self.state[0][2]
        # is the board full, game over?
        for i in range(0, 3):
            for j in range(0, 3):
                if self.state[i][j] == '_':
                    return None  # there is an empty space.
        # nobody wins.
        return '_'

    # Generally same as the minimax algo.
    def max_alpha_beta(self, alpha, beta):
        maximum_value = -2
        proposed_x = None
        proposed_y = None

        result = self.check_end()
        if result == 'X':
            return -1, 0, 0
        elif result == 'O':
            return 1, 0, 0
        elif result == '_':
            return 0, 0, 0

        for i in range(0, 3):
            for j in range(0, 3):
                if self.state[i][j] == '_':
                    self.state[i][j] = 'O'
                    (m, min_i, in_j) = self.min_alpha_beta(alpha, beta)
                    if m > maximum_value:
                        maximum_value = m
                        proposed_x = i
                        proposed_y = j
                    self.state[i][j] = '_'

                    if maximum_value >= beta:
                        return maximum_value, proposed_x, proposed_y
                    if maximum_value > alpha:
                        alpha = maximum_value

        return maximum_value, proposed_x, proposed_y

    # Generally same as the minimax algo.
    def min_alpha_beta(self, alpha, beta):
        minimum_value = 2
        proposed_x = None
        proposed_y = None

        result = self.check_end()
        if result == 'X':
            return -1, 0, 0
        elif result == 'O':
            return 1, 0, 0
        elif result == '_':
            return 0, 0, 0

        for i in range(0, 3):
            for j in range(0, 3):
                if self.state[i][j] == '_':
                    self.state[i][j] = 'X'
                    (m, max_i, max_j) = self.max_alpha_beta(alpha, beta)
                    if m < minimum_value:
                        minimum_value = m
                        proposed_x = i
                        proposed_y = j
                    self.state[i][j] = '_'

                    if minimum_value <= alpha:
                        return minimum_value, proposed_x, proposed_y
                    if minimum_value < beta:
                        beta = minimum_value

        return minimum_value, proposed_x, proposed_y

    def play_alpha_beta(self):  # plays the game as alpha-beta
        while True:
            self.print_state()
            self.result = self.check_end()
            if self.result != None:
                if self.result == 'X':
                    print('X wins!')
                elif self.result == 'O':
                    print('O wins!')
                elif self.result == '_':
                    print("Draw!")
                return

            if self.turn == 'X':
                while True:
                    print("X's turn!")
                    (m, proposed_x, proposed_y) = self.min_alpha_beta(-2, 2)
                    print('Best move: X = {}, Y = {}'.format(
                        proposed_x, proposed_y))
                    print("Playing the best move...")

                    if self.is_valid(proposed_x, proposed_y):
                        self.state[proposed_x][proposed_y] = 'X'
                        self.turn = 'O'
                        break
                    else:
                        print('Invalid move.')
            else:
                print("O's turn!")
                (m, proposed_x, proposed_y) = self.max_alpha_beta(-2, 2)
                print('Playing move: X = {}, Y = {}'.format(
                    proposed_x, proposed_y))
                self.state[proposed_x][proposed_y] = 'O'
                self.turn = 'X'


def main():
    g = Game()
    g.play_alpha_beta()


if __name__ == "__main__":
    main()
