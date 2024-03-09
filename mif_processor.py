import mif
import os
from pathlib import Path
import glob
import fnmatch
import numpy as np
import csv

# mif_processor.py
# Produces a .csv file for each board containing the data from the DE1-SoC RAMs stored in .mif files.  

def write_RAMs_to_file(boardname):    
    data = []
    load_PLL(data, 'PLL_60', boardname)
    load_PLL(data, 'PLL_70', boardname)
    load_PLL(data, 'PLL_80', boardname)
    load_PLL(data, 'PLL_90', boardname)
    load_PLL(data, 'PLL_100', boardname)
    load_PLL(data, 'PLL_125', boardname)
    load_PLL(data, 'PLL_150', boardname)
    load_PLL(data, 'PLL_155', boardname)
    load_PLL(data, 'PLL_160', boardname)
    load_PLL(data, 'PLL_165', boardname)
    
    rows = []
    rowCursor = 0
    for inst in range (len(data)):
        row = []
        if inst % 8 == 0:
            if inst == 0:
                rows.append(['PLL 60'])
            elif inst == 8:
                rows.append(['PLL 70'])
            elif inst == 16:
                rows.append(['PLL 80'])
            elif inst == 24:
                rows.append(['PLL 90'])
            elif inst == 32:
                rows.append(['PLL 100'])
            elif inst == 40:
                rows.append(['PLL 125'])
            elif inst == 48:
                rows.append(['PLL 150'])
            elif inst == 56:
                rows.append(['PLL 155'])
            elif inst == 64:
                rows.append(['PLL 160'])
            elif inst == 72:
                rows.append(['PLL 165'])                                                  
        row.append('')
        row.append('RAM ' + str((inst % 8) + 1))
        row.append('Address')
        for byteNum in range(9, 0, -1):
            row.append('Byte ' + str(byteNum))
        rows.append(row)
        rowCursor += 1
        for addr in range(len(data[inst])):
            cols = []
            cols.append('')
            cols.append('')
            #cols.append('Address ' + str(addr) + ':')
            cols.append(str(addr))
            for byte in range(len(data[inst][addr])):
                cols.append(str(data[inst][addr][byte]))
            rows.append(cols)
            rowCursor += 1

    csvfname = boardname + '_Functional_Results.csv'	
    with open(csvfname, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    
def load_PLL(dataStorage, PLLname, boardname):
    p = Path('.')
    for fileNum in range(1, 9):
      filePath = p.joinpath('Shipped_Boards_Baselines').joinpath(boardname).joinpath('Baseline').joinpath('PLL_RAMs').joinpath(PLLname).joinpath('RAM' + str(fileNum) + '.mif')
      f = open(filePath, 'r')
      width, mem = mif.load(f, packed=True)
      dataStorage.append(mem)
      f.close()    

write_RAMs_to_file('Board_02612')
write_RAMs_to_file('Board_02689')
write_RAMs_to_file('Board_02748')
write_RAMs_to_file('Board_03104')
write_RAMs_to_file('Board_10970')