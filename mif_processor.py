import mif
import os
from pathlib import Path
import glob
import fnmatch
import numpy as np
import csv

# mif_processor.py
# Author: Hunter Frederick
# Locates .mif files in file system then extracts each .mif for writing to a .csv file organized according to .mif source

fCount = 0
for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.mif'):
        fCount += 1

data = []
for fileNum in range(0, fCount):
	with open('mem' + str(fileNum) + '.mif') as f:
		width, mem = mif.load(f, packed=True)
		data.append(mem)
		
rows = []
rowCursor = 0		
for inst in range (len(data)):
	col = []
	col.append('memory instance ' + str(inst))
	rows.append(col)
	rowCursor += 1
	for addr in range(len(data[inst])):		
		cols = []
		cols.append(' ')
		cols.append('Address ' + str(addr) + ':')
		cols.append(str(data[inst][addr][0]))
		rows.append(cols)
		rowCursor += 1
		
with open('test.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)  