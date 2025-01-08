import constants as const
import numpy as np
import random as rn
import pandas as pd


class SudokuGame:

    def __init__(self, nremove=None):
        self.sudomat = const.DEF_VAL * np.ones((const.SUDO_DIM, const.SUDO_DIM))
        
        if nremove is not None:
            assert nremove.isnumeric(), "You have to insert an integer"
            nremove = int(nremove)
            assert nremove <= const.SUDO_DIM**2, f"You can remove maximum {const.SUDO_DIM**2} elements"

            # Prepare a valid sudoku matrix
            r_start = rn.randint(0, const.SUDO_DIM**2)
            c_start = rn.randint(0, const.SUDO_DIM**2)
            self.__fill(r_start, c_start)
            # self.__sudostartingmatrix = self.sudomat


            # Sample some elements to remove
            to_rem = rn.sample(range(const.SUDO_DIM**2), nremove)

            for elem in to_rem:
                r = elem//const.SUDO_DIM
                c = (elem - const.SUDO_DIM*r) - 1
                self.sudomat[r, c] = const.DEF_VAL

    def sudoku_read(self, filename):
        # Read a sudoku from a csv file
        self.sudomat = pd.read_csv(filename, header=None).values

    def sudoku_solve(self):
        [rn, cn] = self.__emptynext()
        self.__fill(rn, cn)


    def check_matrix(self):
        for r in range(0, const.SUDO_DIM):
            for c in range(0, const.SUDO_DIM):
                if not (self.__check_col(c) and self.__check_square(r, c) and self.__check_row(r)):
                    return False

        return True

    def __fill(self, r, c):
        # Fill the matrix starting from column c and row c

        # if the matrix is filled, return
        if self.__isfilled() and self.check_matrix():
            # print(self.sudomat)
            return

        # if the matrix is not valid remove the value you placed in position r,c by setting it equal to -1
        # and returns
        elif not self.check_matrix():
            self.sudomat[r, c] = const.DEF_VAL
            return


        else:
            i = 0
            v_perm = np.random.permutation(const.SUDO_DIM) + 1
            while i < const.SUDO_DIM:
                # Compute next empty entry
                [rn, cn] = self.__emptynext()
                if rn == -1 and cn == -1:
                    return
                self.sudomat[rn, cn] = v_perm[i]
                self.__fill(rn, cn)
                i = i + 1

            # If you reach this, something went wrong...
            if i == const.SUDO_DIM and not self.__isfilled():
                self.sudomat[rn, cn] = const.DEF_VAL
                self.sudomat[r, c] = const.DEF_VAL
                return


    def __isfilled(self):
        bolean = self.sudomat != const.DEF_VAL
        return np.all(bolean)

    def __emptynext(self):
        # Find the next empty value in the matrix and return the positions
        result = np.where(self.sudomat == const.DEF_VAL)
        if result[0].size == 0:
            # If everithing is full then return a not valid index, say -1 -1.
            return -1, -1
        return result[0][0], result[1][0]

    def __check_square(self, i, j):
        # Check if the square whose element ij belongs to is a valid square (i.e. no repetitions of numbers)
        row_id = i // const.SMALL_SQUARE_SIZE
        col_id = j // const.SMALL_SQUARE_SIZE

        row_id_s = row_id * const.SMALL_SQUARE_SIZE
        row_id_e = (row_id + 1) * const.SMALL_SQUARE_SIZE
        col_id_s = col_id * const.SMALL_SQUARE_SIZE
        col_id_e = (col_id + 1) * const.SMALL_SQUARE_SIZE

        # get the slice
        slice = self.sudomat[row_id_s:row_id_e, col_id_s:col_id_e]
        return self.check_different(slice)

    def __check_col(self, j):
        slice = self.sudomat[:, j]
        return self.check_different(slice)

    def __check_row(self, i):
        slice = self.sudomat[i, :]
        return self.check_different(slice)

    def print(self):
        print(self.sudomat)

    @staticmethod
    def check_different(np_matrix):
        # Check if all elements in the vector are different
        np_vector = np.reshape(np_matrix, (1, const.SUDO_DIM))
        bolean = np_vector[np_vector != const.DEF_VAL].size == np.unique(np_vector[np_vector != const.DEF_VAL]).size
        return bolean
