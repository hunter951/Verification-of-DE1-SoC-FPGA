import mif
import os
from pathlib import Path
import glob
import fnmatch
import numpy as np
import csv

# mif_processor.py
# Produces a .csv file containing the data from the DE1-SoC RAMs stored in .mif files.  
# Note only handles PLL_60 of first board need to expand for all
fCount = 0
p = Path('.')
#boardPath = Path(".\\Shipped_Boards_Baselines\\Board_02612\\Baseline\\PLL_RAMs\\PLL_60")
#for file in os.listdir(Path('.').joinpath('Shipped_Boards_Baselines').joinpath('Board_02612').joinpath('Baselines').joinpath('PLL_RAMs').joinpath('PLL_60')):
#for file in os.listdir(p.joinpath('Shipped_Boards_Baselines').joinpath('Board_02612').joinpath('Baseline').joinpath('PLL_RAMs').joinpath('PLL_60')):
#    if fnmatch.fnmatch(file, '*.mif'):
#        fCount += 1

data = []
#for fileNum in range(1, fCount + 1):
	#with open('RAM' + str(fileNum) + '.mif') as f:
		#width, mem = mif.load(f, packed=True)
		#data.append(mem)
for fileNum in range(1, 9):
      filePath = p.joinpath('Shipped_Boards_Baselines').joinpath('Board_02612').joinpath('Baseline').joinpath('PLL_RAMs').joinpath('PLL_60').joinpath('RAM' + str(fileNum) + '.mif')
      f = open(filePath, 'r')
      width, mem = mif.load(f, packed=True)
      data.append(mem)
      f.close()

print(data[0])

rows = []
rowCursor = 0
for inst in range (len(data)):
    col = []
    col.append('RAM ' + str(inst + 1))
    col.append('')
    for byteNum in range(9, 0, -1):
        col.append('Byte ' + str(byteNum))
    rows.append(col)
    rowCursor += 1
    for addr in range(len(data[inst])):
        cols = []
        cols.append(' ')
        cols.append('Address ' + str(addr) + ':')
        for byte in range(len(data[inst][addr])):
            cols.append(str(data[inst][addr][byte]))
        rows.append(cols)
        rowCursor += 1
		
with open('test.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
    