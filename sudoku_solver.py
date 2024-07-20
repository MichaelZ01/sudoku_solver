# from tkinter import *
# from tkinter import ttk

# import sv_ttk

from lib.brute_force import solve

sample_sudoku :list[list[int]] = [
    [9, 0, 2, 7, 3, 0, 4, 0, 0],
    [0, 8, 0, 0, 4, 9, 0, 0, 0],
    [3, 7, 0, 0, 5, 1, 9, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 5, 7],
    [2, 1, 0, 0, 0, 0, 3, 9, 6],
    [0, 0, 0, 9, 1, 0, 0, 8 ,0],
    [5, 3, 1, 0, 0, 0, 0, 7, 2],
    [6, 4, 0, 5, 0, 0, 8, 3, 0],
    [0, 0, 7, 0, 0, 3, 5, 4, 0]
]


def main():
    # root = Tk()
    # root.title("Sudoku Solver")
    # root.geometry('900x900')
    # root.resizable(False, False)

    # mainframe = ttk.Frame(root, padding="3 3 12 12")
    # mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    # root.columnconfigure(0, weight=1)
    # root.rowconfigure(0, weight=1)

    # sv_ttk.use_dark_theme()
    # root.mainloop()

    print(sample_sudoku)
    starting_grid = sample_sudoku






if __name__ == "__main__":
    main()