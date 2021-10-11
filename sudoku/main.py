import helpers as hp


if __name__ == '__main__':

    while True:
        numel = input("How many elements do you want to remove from the matri 9x9?")
        try:
            Game = hp.SudokuGame(numel)

            Game.print()

            Game.sudoku_solve()

            Game.print()

            print("Sudoku solved! Play Again!")
        except Exception as e:
            print(e)




