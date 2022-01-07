# Sudoku Solver by Atharva Nangare

import tkinter as tk

board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]

MARGIN = 20
SIDE = 50
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9

class SolveSudoku():
    def __init__(self, board):
        self.board = board
        self.visited_sub = [[0 for i in range(10)] for j in range(9)]
        self.visited_row = [[0 for i in range(10)] for j in range(9)]
        self.visited_col = [[0 for i in range(10)] for j in range(9)]

    def solve(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    curr = self.board[i][j]
                    self.visited_sub[self.fun(i, j)][curr] = 1
                    self.visited_row[i][curr] = 1
                    self.visited_col[j][curr] = 1
        self.rec(0, 0)

    def fun(self, i, j):
        if i < 3 and j < 3:
            return 0
        elif i < 3 and j < 6:
            return 1
        elif i < 3 and j < 9:
            return 2
        elif i < 6 and j < 3:
            return 3
        elif i < 6 and j < 6:
            return 4
        elif i < 6 and j < 9:
            return 5
        elif i < 9 and j < 3:
            return 6
        elif i < 9 and j < 6:
            return 7
        return 8

    def check(self, arr):
        for i in range(9):
            for j in range(9):
                if arr[i][j] == 0:
                    return False
        return True

    def rec(self, i, j):
        if (self.check(self.board)):
            return True

        if (j >= 9):
            j = 0
            i = i + 1
        if (i >= 9):
            return False

        if self.board[i][j] != 0:
            return self.rec(i, j + 1)

        for k in range(1, 10):
            if self.visited_sub[self.fun(i, j)][k] != 1 and self.visited_row[i][k] != 1 and self.visited_col[j][k] != 1:
                self.visited_sub[self.fun(i, j)][k] = 1
                self.visited_row[i][k] = 1
                self.visited_col[j][k] = 1
                self.board[i][j] = k
                if self.rec(i, j):
                    return True
                self.visited_sub[self.fun(i, j)][k] = 0
                self.visited_row[i][k] = 0
                self.visited_col[j][k] = 0
                self.board[i][j] = 0

    def get_board(self):
        return self.board



class Application(tk.Frame):
    def __init__(self, board, master=None):
        super().__init__(master)
        self.board = board
        self.master = master
        self.grid()
        self.entries = []
        self.copy = []
        self.get_copy()
        self.create_grid()
        self.solve_sudoku()
        self.create_buttons()


    def get_copy(self):
        for i in range(9):
            temp = []
            for j in range(9):
                if self.board[i][j] == 0:
                    temp.append(0)
                else:
                    temp.append(1)
            self.copy.append(temp)


    def create_grid(self):
        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGHT + HEIGHT/10)
        self.canvas.grid(row=0, column=0)

        for i in range(10):
            color = "black" if i % 3 == 0 else "gray"

            x0 = MARGIN + i * SIDE
            y0 = MARGIN
            x1 = MARGIN + i * SIDE
            y1 = HEIGHT - MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

            x0 = MARGIN
            y0 = MARGIN + i * SIDE
            x1 = WIDTH - MARGIN
            y1 = MARGIN + i * SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

        for i in range(9):
            temp = []
            for j in range(9):
                x0 = MARGIN + i * SIDE
                y0 = MARGIN + j * SIDE
                e = tk.Entry(self)
                e["width"] = 2
                e["justify"] = "center"
                e["font"] = "Helvetica 30"
                if self.board[i][j] != 0:
                    e.insert(0, str(self.board[i][j]))
                    e.config({"background": "light gray"})
                    e.configure(state="readonly")
                temp.append(e)
                self.canvas.create_window(x0 + 1, y0 + 1, anchor="nw", window=e)
            self.entries.append(temp)


    def solve_sudoku(self):
        b = SolveSudoku(self.board)
        b.solve()
        self.board = b.get_board()


    def create_buttons(self):
        btn_check = tk.Button(self)
        btn_check["text"] = "CHECK"
        btn_check["font"] = "Helvetica 13 bold"
        btn_check["command"] = self.on_click_check
        self.canvas.create_window(2*MARGIN + SIDE, HEIGHT + 15, window = btn_check)

        btn_solve = tk.Button(self)
        btn_solve["text"] = "SOLVE"
        btn_solve["font"] = "Helvetica 13 bold"
        btn_solve["command"] = self.on_click_solve
        self.canvas.create_window(2*MARGIN + 4*SIDE, HEIGHT + 15, window = btn_solve)

        btn_reset = tk.Button(self)
        btn_reset["text"] = "RESET"
        btn_reset["font"] = "Helvetica 13 bold"
        btn_reset["command"] = self.on_click_reset
        self.canvas.create_window(2*MARGIN + 7*SIDE, HEIGHT + 15, window = btn_reset)


    def on_click_check(self):
        for i in range(9):
            for j in range(9):
                if self.copy[i][j] == 0:
                    t = str(self.entries[i][j].get())
                    self.entries[i][j].config({"background": "white"})
                    if t != "":
                        if t != str(self.board[i][j]):
                            self.entries[i][j].config({"background": "firebrick1"})
                        else:
                            self.entries[i][j].config({"background": "lawn green"})


    def on_click_solve(self):
        for i in range(9):
            for j in range(9):
                if self.copy[i][j] == 0:
                    self.entries[i][j].config({"background": "white"})
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, self.board[i][j])


    def on_click_reset(self):
        for i in range(9):
            for j in range(9):
                if self.copy[i][j] == 0:
                    self.entries[i][j].config({"background": "white"})
                    self.entries[i][j].delete(0, tk.END)



root = tk.Tk()
app = Application(board, master = root)
app.mainloop()