# coding: utf-8
# python version 3.6.0
import pandas as pd
import numpy as np

def file_read():
	r_filename = 'calculate.csv' #inportfilename
	data = pd.read_csv(r_filename,header=None)
	return data

def get_row(data):
	data = np.array(data)
	return data.shape[0]

def get_col(data):
	data = np.array(data)
	return data.shape[1]

def write_out(data):
	w_filename = 'text1.txt' #書き込みファイル名の指定(任意)
	row = get_row(data) #rowlength
	col = get_col(data) #collength
	str_bar = "|"
	str_n = " \n "
	bar = "---|"

	f = open(w_filename, 'w') 
	data = np.array(data,dtype = 'str')

	str_f = 0
	
	f = open('text1.txt', 'w',encoding="utf-8") #exportfilename
	for i in range(0,row):
		str_w = str_bar
		f.writelines(str_w)

		if i == 1:
			for i in range(0,col):
				f.write(bar)
			f.write("\n")

			str_w = str_bar
			f.writelines(str_w)

		for j in range(0,col):
			f.writelines(data[i][j])

			str_w = str_bar
			f.writelines(str_w)

			if j == (col-1):
				f.write("\n")

	f.close()

if __name__ == '__main__':
	data = file_read()
	write_out(data)

	