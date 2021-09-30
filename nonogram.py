import copy

from board_parser import get_board
from gui import keep_pygame, init_gui, update_cells, update_screen
from line_solver import grandmother, subtract_req, get_line_with_hint, sum_req, fix_boundaries

EDGES_COLOR = (0, 0, 0)
CHOSEN_COLOR = (204, 204, 204)
CELL_COLOR = (255, 255, 255)
NUMBERS_COLOR = (0, 0, 0)
RED_COLOR = (255, 0, 0)
MULTIPLIER = 0.85


def draw_rect(surface, fill_color, outline_color, rect, border=1):
    surface.fill(outline_color, rect)
    surface.fill(fill_color, rect.inflate(-border * 2, -border * 2))


class Board:
    def __init__(self, num_rows, num_cols):
        self.pixels = num_rows * num_cols
        self.width = num_cols
        self.height = num_rows
        self.req_rows = []
        self.req_cols = []
        self.board = []
        self.dynamic_dict = {}
        self.visualisation = None
        self.cells = None
        self.screen = None
        for _ in range(num_rows):
            row = []
            for _ in range(num_cols):
                row.append('u')
            self.board.append(row)

    @classmethod
    def constructor(cls, rows, cols):
        board = cls(len(rows), len(cols))
        for row in rows:
            board.add_req_row(row)
        for col in cols:
            board.add_req_col(col)
        return board

    def add_req_row(self, data):
        if isinstance(data, list):
            self.req_rows.append(data)
        else:
            self.req_rows.append([data])

    def add_req_col(self, data):
        if isinstance(data, list):
            self.req_cols.append(data)
        else:
            self.req_cols.append([data])

    @property
    def transpose(self):
        return [list(i) for i in zip(*self.board)]

    def __str__(self):
        result = ''
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if not j % 5:
                    result += ' | '
                if self.board[i][j] is None:
                    result += '   '
                else:
                    result += f' {self.board[i][j]} '
            result += "\n"
            if not (i + 1) % 5:
                result += ' _ ' * len(self.board[0])
                result += '\n'
        return result

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, item):
        return self.board[item]

    def print_rows(self):
        for row in self.req_rows:
            if isinstance(row, list):
                print(' '.join([str(num) for num in row]))
            else:
                print(row)

    def print_cols(self):
        for col in self.req_cols:
            if isinstance(col, list):
                print(' '.join([str(num) for num in col]))
            else:
                print(col)

    def guess_row(self, i):
        old_line = self.board[i]
        old_count = old_line.count('u')
        line = get_line_with_hint(self.width, self.req_rows[i], self.dynamic_dict, old_line)
        count = line.count('u')
        self.pixels -= (old_line.count('u') - line.count('u'))
        if self.visualisation and old_line.count('u') - line.count('u'):
            update_cells(self.cells, self.board)
            update_screen(self.cells, self.screen)
        for index, el in enumerate(line):
            if el != 'u':
                self.board[i][index] = el
        return old_count - count


    def guess_col(self, i):
        self.board = self.transpose
        old_col = self.board[i]
        col = get_line_with_hint(self.height, self.req_cols[i], self.dynamic_dict, old_col)
        self.pixels -= (old_col.count('u') - col.count('u'))
        for index, el in enumerate(col):
            if el != 'u':
                self.board[i][index] = el
        self.board = self.transpose
        if self.visualisation and old_col.count('u') - col.count('u'):
            print('line')
            update_cells(self.cells, self.board)
            update_screen(self.cells, self.screen)
        return old_col.count('u') - col.count('u')

    def fix_all_boundaries(self):
        for i in range(self.height):
            line = self.board[i]
            old_count = line.count('u')
            if line.count('u'):
                fix_boundaries(line, self.req_rows[i])
                self.board[i] = fix_boundaries(line, self.req_rows[i])
            self.pixels += (self.board[i].count('u') - old_count)

    def get_unknown_num(self, i, row=True):
        if row:
            return self.board[i].count('u')
        return self.transpose[i].count('u')

    def get_req_unused(self, i, row=True):
        if row:
            return self.board[i].count('0') + self.board[i].count('1') - sum(self.req_rows[i])
        return self.transpose[i].count('0') + self.transpose[i].count('1') - sum(self.req_cols[i])

    def fix_all_boundaries_new(self):
        for i in range(self.height):
            line = copy.copy(self.board[i])

            old_count = line.count('u')
            if line.count('u'):
                res = grandmother(line[:], self.req_rows[i])
                self.board[i] = res
                if (self.board[i].count('u') - old_count):
                    self.board_of_board.append(copy.deepcopy(self.board))

            self.pixels += (self.board[i].count('u') - old_count)
        self.board = self.transpose
        for i in range(self.width):
            line = copy.copy(self.board[i])

            old_count = line.count('u')
            if line.count('u'):
                res = grandmother(line, self.req_cols[i])
                self.board[i] = res

            self.pixels += (self.board[i].count('u') - old_count)
        self.board = self.transpose

    def fix_until_end(self):
        pixels = 0
        while pixels != self.pixels:
            pixels = self.pixels
            self.fix_all_boundaries_new()

    def better_solve(self, visualisation=False):
        self.visualisation = visualisation
        if self.visualisation:
            self.cells, self.screen = init_gui(self.board)
        import time
        t0 = time.time()
        prev = []
        my_index = 3
        while self.pixels:
            t1 = time.time()
            transposed = self.transpose
            print(f'cells remaining =  {self.pixels}, t = {t1 - t0}')
            total_keys, total = self.get_queue(prev, transposed)
            for index, key in enumerate(total_keys):
                if index > my_index:
                    break
                if key[1]:
                    element = copy.deepcopy(transposed[key[0]])
                    self.guess_col(key[0])
                else:
                    element = copy.deepcopy(self.board[key[0]])
                    self.guess_row(key[0])
                prev.append((key[0], key[1], element))
            my_index += .1

        print('DONE')
        if self.visualisation is False:
            t1 = time.time()
            print(t1 - t0)
            init_gui(self.board)
        keep_pygame()

    def get_queue(self, prev, transposed):
        rows = {(i, 0): (self.board[i].count('u') - sum_req(subtract_req(self.board[i], self.req_rows[i])) - 1.1 *
                         self.board[i].count('0')) /
                        self.board[i].count('u') for i in range(self.height) if self.board[i].count('u') > 0}
        for k in rows:
            num = k[0]
            row = self.board[num]
            if row.count('u') == sum(self.req_rows[num]) - row.count('u'):
                rows[k] = float('-inf')
        cols = {(i, 1): (transposed[i].count('u') - sum_req(subtract_req(transposed[i], self.req_cols[i])) + 0.9 *
                         transposed[i].count('1') - 1.1 * transposed[i].count('0')) /
                        transposed[i].count('u') for i in range(self.width) if transposed[i].count('u') > 0}
        for k in cols:
            num = k[0]
            row = transposed[num]
            if row.count('u') == sum(self.req_cols[num]) - row.count('u'):
                cols[k] = float('-inf')
        total = rows
        total.update(cols)
        total_keys = sorted(total.keys(), key=lambda val: total[val])

        if prev:
            for key in prev[:]:
                if not key[1]:
                    element = self.board[key[0]]
                if key[1]:
                    element = transposed[key[0]]
                if key[2] == element:
                    if key[:2] in total_keys:
                        total_keys.remove(key[:2])
                else:
                    prev.remove(key)
        return total_keys, total


if __name__ == '__main__':
    import time

    # url = 'https://www.nonograms.org/nonograms/i/46967'
    # url = 'https://www.nonograms.org/nonograms/i/47033'
    # url = 'https://www.nonograms.org/nonograms/i/48495'
    # url = 'https://www.nonograms.org/nonograms/i/48481'
    # url = 'https://www.nonograms.org/nonograms/i/48480'
    # url = 'https://www.nonograms.org/nonograms/i/48475'
    # url = 'https://www.nonograms.org/nonograms/i/48463'
    # url = 'https://www.nonograms.org/nonograms/i/48446'
    # url = 'https://www.nonograms.org/nonograms/i/48445'
    # url = 'https://www.nonograms.org/nonograms/i/48443'
    # url = 'https://www.nonograms.org/nonograms/i/48440'
    # url = 'https://www.nonograms.org/nonograms/i/48432'
    url = 'https://www.nonograms.org/nonograms/i/48418'
    rows, cols = get_board(url)
    board = Board.constructor(rows, cols)
    print(f'{len(rows)=}, {len(cols)=}')
    # board.better_solve(True)
    board.better_solve()
