# coding:Shift_JIS

# importing an os module.
import os
# importing numpy as np
import numpy as np
# importing an excel file loader module.
import xlrd

data_path = './datafiles/'

# making a book list of periodic datas
# it return the book list
def make_periodic_book_list():
    book_list = os.listdir(data_path + '0/')
    print('loading periodic datas')
    print(book_list)
    print('done')
    return book_list

# making a book list of aperiodic datas
# returning the book list
def make_aperiodic_book_list():
    book_list = os.listdir(data_path + '1/')
    print('loading aperiodic datas')
    print(book_list)
    print('done')
    return book_list

# getting arrays from list and returing the arrays.
# these arrays should have sheets number for the 1d of the array, row number from each sheets for the 2d of the array.
# the 2d data should be fixed and it have to have 100( this number can be changed by result).
# returning data has 3 dimetions, such as data_3d_array[0(periodic) or 1(aperiodic)][number of sheets][datas of each sheets]
def make_data_arrays_from_list(periodic_list, aperiodic_list):
    data_3d_array = np.zeros((2, len(periodic_list) + len(aperiodic_list), 100))
    for i in range(0,2) : # I feel its a stupid way;;
        if i == 0:
            book_list = periodic_list
        else:
            book_list = aperiodic_list
        path = data_path + str(i) + '/' # making a path string because it will be used by loading fase.
        for enum, book_name in enumerate(book_list): # enum has number of loop; useful!!!!!!
            print(book_name) # printing the loading book name
            if book_name.startswith('.'): # ignoring the dot files that might be made by linux systems.
                print('ignored a system file')
            else:
                book = xlrd.open_workbook(path+book_name)
                sheet = book.sheet_by_index(0)
                for row in range(0, 100):
                    # am I crasy?
                    if i == 0:
                        arrayNum = enum
                    if i == 1:
                        arrayNum = enum + len(periodic_list)
                    data_3d_array[i][arrayNum][row] = sheet.cell(row, 0).value
                    print(data_3d_array[i][arrayNum][row]) # priting loaded data
    return data_3d_array

def main():
    periodic_list  = make_periodic_book_list()
    aperiodic_list = make_aperiodic_book_list()
    learning_data_3d_array = make_data_arrays_from_list(periodic_list, aperiodic_list)
    print()
    print(learning_data_3d_array)
if __name__ == "__main__":
    main()
