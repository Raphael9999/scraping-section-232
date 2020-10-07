import mine232 as mn
import pandas as pd
import datetime # duration calculation
from os import path
import time # for the sleep at the end of the loop

# input parameters
glist = [13383, 16811, 17215, 18056, 18633, 18766, 18830, 19708] 

# variable initiation
glist.sort()
fromto = str(glist[0])+'-'+str(glist[-1])
res_file = r'result\extract232_'+fromto+'.csv'
startt = datetime.datetime.now() #Performance management, start of run time

my_erl = mn.ERList(ids=glist, wait=0.5)
# append those at the end of the target file
my_erl.df.to_csv(res_file, index = False, mode='a', header=True)

endt = datetime.datetime.now() # current time
print(my_erl.extracted, end='')
print(' were extracted in', endt-startt)
