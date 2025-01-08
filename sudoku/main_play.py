import helpers as hp
import time

if __name__ == '__main__':


    file_sudodu = r"C:\Users\eid0110204\OneDrive - Eni\Documenti\all_my_files\university\012_codes\opencodes\sudoku\input_sudoku\sudoku_001.csv"


    print("Read a sudoku from a file!")

    Game = hp.SudokuGame()
    Game.sudoku_read(file_sudodu)
    Game.print()

    # Solve the sudoku
    start_time = time.time()
    Game.sudoku_solve()
    end_time = time.time() 
    execution_time = end_time - start_time

    Game.print()

    print("Sudoku solved in ", execution_time, " seconds") 
