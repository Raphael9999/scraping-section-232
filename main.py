import mine232 as mn
import pandas as pd
import datetime
from os import path

# input parameters
gfrom = 10000
gto   = 15000
inc   = 100

# variable initiation
fromto = str(gfrom)+'-'+str(gto)
res_file = r'result\extract232_'+fromto+'.csv'
lfrom = gfrom
lto = min(lfrom+inc, gto)
hbool = True #~path.exists(res_file) # write header on first to_csv
startt = datetime.datetime.now() #Performance management, start of run time

while lfrom < lto:
    # extracting inc number of exclusion requests
    # if df get to big, program slows
    my_erl = mn.ERList(from_id=lfrom, to_id=lto)
    # append those at the end of the target file
    my_erl.df.to_csv(res_file, index = False, mode='a', header=hbool)
    # update variable for next loop
    lfrom = lfrom + inc
    lto = min(lto + inc, gto)
    if hbool:
        # we only write the header on the first to_csv
        hbool = False
    # progress bar
    endt = datetime.datetime.now() # current time
    prog_per = round( 100 * ( lfrom - gfrom) / ( gto - gfrom ),2)
    if prog_per > 100:
        # we are done, and are going out of the loop
        prog_per = 100
    print('\r', end='') # clear progress bar
    print(str(prog_per) + r'% extracted in', endt-startt, end='')