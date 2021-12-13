class Board:

    def __init__(self, numbers):
        self.board = list(numbers)
        self.board_as_line = sum(self.board, [])
        self.winner_number = None
        print('New Board', len(self.board_as_line), self.board_as_line)
        self.numbers = {}
        for index, number in enumerate(self.board_as_line):
            self.numbers[number] = {'pos': index, 'marked': False}

    def did_won(self):
        return not self.winner_number == None

    def mark(self, number):
        if number in self.numbers:
            #print(number, 'marked on', self.numbers[number])
            self.numbers[number]['marked'] = True
            pos = self.numbers[number]['pos']
            if self.is_row_complete(pos) or self.is_col_complete(pos):
                self.winner_number = number
                return True
            else:
                return False

    def is_row_complete(self, pos):
        start_row = int(pos / 5) * 5
        end_row = start_row + 5
        row = self.board_as_line[start_row:end_row]
        #print('row', row)
        if len(list(filter(lambda number: self.numbers[number]['marked'],
                           row))) == 5:
            # print('winner matrix', self.board)
            # print('winner vector', self.board_as_line)
            # print('marked on winner', [
            #       number for number, value in self.numbers.items() if value['marked']])
            # print('winner row', row)
            return True

    def is_col_complete(self, pos):
        start_col = pos % 5
        column = self.board_as_line[start_col::5]
        #print('column', column)
        if len(list(filter(lambda number: self.numbers[number]['marked'],
                           column))) == 5:
            # print('winner matrix', self.board)
            # print('winner vector', self.board_as_line)
            # print('marked on winner', [
            #       number for number, value in self.numbers.items() if value['marked']])
            # print('winner column', column)
            return True

    def score(self):
        score = sum([number for number, value in self.numbers.items()
                     if not value['marked']])
        return score * self.winner_number
