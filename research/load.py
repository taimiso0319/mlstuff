# coding:Shift_JIS

# importing an os module.
import os
# importing an excel file loader module.
import xlrd

data_path = './datafiles/'

def make_book_list():
    book_list = os.listdir(data_path)
    return book_list

# getting arrays from list and returing the arrays.
# these arrays should have sheets number for 1d, row number from each sheets for 2d.
# 2d data should be fixed and it have to have 100( this number can be changed by result).
def make_data_arrays_from_list(book_list):
    data_2d_array = np.zeros(len(book_list),100)
    for book_name in enumerate(book_list) :
        print(book_name)
        if book_name.startswith('.'):
            print('ignored a system file')
        else:
            book = xlrd.open_workbook(data_path+book_name)
            sheet = book.sheet_by_index(0)
            row_num = sheet.nrows;
            for row in range(0, row_num):
                print(sheet.cell(row,0)) # print laoded strings

def main():
    book_list = make_book_list()
    make_data_arrays_from_list(book_list)

if __name__ == "__main__":
    main()
