import pygame

EDGES_COLOR = (0, 0, 0)
CHOSEN_COLOR = (204, 204, 204)
CELL_COLOR = (255, 255, 255)
NUMBERS_COLOR = (0, 0, 0)
MULTIPLIER = 0.9


def draw_rect(surface, fill_color, outline_color, rect, border=1):
    surface.fill(outline_color, rect)
    surface.fill(fill_color, rect.inflate(-border * 2, -border * 2))


def init_cells(WINDOW_HEIGHT, WINDOW_WIDTH, BLOCK_SIZE, board=None):
    all_rects = []
    for index_y, y in enumerate(range(0, WINDOW_HEIGHT, BLOCK_SIZE)):
        if board and index_y >= len(board):
            continue
        row = []
        for index_x, x in enumerate(range(0, WINDOW_WIDTH, BLOCK_SIZE)):
            if board and index_x >= len(board[0]):
                continue

            rect = pygame.Rect(x, y, BLOCK_SIZE - 1, BLOCK_SIZE - 1)
            if board and board[index_y][index_x]:
                row.append([[rect, CELL_COLOR], str(board[index_y][index_x])])
            else:
                row.append([[rect, CELL_COLOR], ''])
        all_rects.append(row)
    print(f'init {len(all_rects)=} {len(all_rects[0])=}')
    return all_rects


def update_cells(cells, board):
    for index_y, row in enumerate(cells):
        for index_x, cell in enumerate(row):
            board_cell = board[index_y][index_x]
            # board_cell = board[index_x][index_y]
            if board_cell != 'u':
                cell[-1] = board_cell
            else:
                cell[-1] = 'u'


def update_screen(all_rects, screen):
    screen.fill(CELL_COLOR)
    for index_row, row in enumerate(all_rects):
        for index_col, item in enumerate(row):
            rect, color = item[0]
            if item[1] == '1':
                draw_rect(screen, NUMBERS_COLOR, EDGES_COLOR, rect)
            else:
                draw_rect(screen, CELL_COLOR, EDGES_COLOR, rect)
    pygame.display.flip()
    pygame.event.pump()

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return True


def init_gui(board):
    pygame.init()
    try:
        import tkinter as tk
        root = tk.Tk()
        window_width = int(MULTIPLIER * root.winfo_screenwidth())
        window_height = int(MULTIPLIER * root.winfo_screenheight())
    except ModuleNotFoundError:
        print('MODULE NOT FOUND')
        window_height = 900
        window_width = 1500
    block_size = int(min(window_height / len(board), window_width / len(board[0])))
    window_width = len(board[0]) * block_size
    window_height = len(board) * block_size
    cells = init_cells(window_height, window_width, block_size, board)
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    screen.fill(CELL_COLOR)
    update_screen(cells, screen)
    return cells, screen


def keep_pygame():
    while True:
        quit_pressed = event_handler()
        if quit_pressed:
            return
