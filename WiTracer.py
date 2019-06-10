#!/usr/bin/python
import subprocess
from time import sleep
import sys
import re
import os
from terminaltables import SingleTable
import math
from decimal import Decimal

reset="\033[0;0m"
red="\033[38;5;9m"
byellow="\033[38;5;3m"
yellowb="\033[38;5;11m"
blue="\033[38;5;27m"
purple="\033[1;33;35m"
cyan="\033[38;5;6m"
white="\033[38;5;7m"
orange="\033[38;5;202m"
lblue="\033[38;5;117m"
green="\033[38;5;2m"



def walk(spaces, dist):
    x = ("""
                        O
                       \|/
                        | %s\ /
                       / \\%s[O]
    """) % (" "*spaces, "_"*dist)
    return x




num = 0
ESSID = []
BSSID = []
SIG = []
CH = []
TwoG = 2412
FiveG = 5170
mylist = ['TKIP', 'AES', 'WPA', 'PSK']


def organize(Data, ESSID, MAC, CH, ENC, SIG, bssid=None, opt=None):
    total = Data
    mac = total[MAC]
    essid = '-'.join(total[0:ESSID]) 
    ch = total[CH]
    enc = total[ENC]
    sig = int(total[SIG])
    if "5G" in essid or "5" in essid:
        db = 10**((27.55-(20*(math.log10(FiveG)))-(sig))/20)
        rounded = int(round(db,1)*2)
        dist = rounded
        spaces = dist
        db = ('%.2f'%db)
        dist_to_ap = walk(spaces, dist)
    else:
        db = 10**((27.55-(20*(math.log10(TwoG)))-(sig))/20)
        rounded = int(round(db,1)*2)
        dist = rounded
        spaces = dist
        db = ('%.2f'%db)
        dist_to_ap = walk(spaces, dist)
    if bssid != None:
        print '{:<45} {} {:>23} {:>30} {:>39} m'.format(white+essid, green+mac+reset, cyan+ch+reset, enc, orange+db+reset)
        print '{}'.format(dist_to_ap)
    elif bssid == None and opt == "-x":
        print '{:<45} {} {:>23} {:>30} {:>39} m'.format(white+essid, green+mac+reset, cyan+ch+reset, enc, orange+db+reset)
    elif bssid == None and opt == "-d":
        print '{:<45} {} {:>23} {:>30} {:>39} dBm'.format(white+essid, green+mac+reset, cyan+ch+reset, enc, orange+str(sig)+reset)

def Main(mon=None, arg=None):
        
    try:
        while 1:
            bssid = arg
            cmd = 'airport -s >out.txt'
            subprocess.call('airport -s >out.txt', shell=True)
            os.system('clear && printf "\e[3J"')

            print '+----------+--------------------------+----------+------+--------+----------+-----------+--------------------+---------+'
            print ' {} {:>55}     {:>27}     {:>19} {:>47}'.format(white+"ESSID", green+"BSSID"+reset, cyan+"CHANNEL"+reset, "Encryption", orange+"Distance"+reset)
            print '+----------+--------------------------+----------+------+--------+----------+-----------+--------------------+---------+' +"\n"
            with open("out.txt") as f:
                next(f)
                for line in f:
                    data = line.lstrip()
                    total = '***'.join(data.split())
                    total = total.split("***")
                    if any(x in total[-2] for x in mylist):
                        if arg != None:
                            if total[-7] == bssid:
                                organize(total, -7, -7, -5, -2, -6, "trace")
                        elif mon != None:
                            opt = mon
                            organize(total, -7, -7, -5, -2, -6, None, opt)

                    else:
                        if arg != None:
                            if total[-6] == bssid:
                                organize(total, -6, -6, -4, -1, -5, "trace")
                            
                        elif mon != None:
                            opt = mon
                            organize(total, -6, -6, -4, -1, -5, None, opt)
    except KeyboardInterrupt:
        print "User Interrupt"





def Help():

    print green + """
+-----------------------------------------------------------+
|      _    \/    _                                         |
|      \\\\   ||   //   Author : [ Tarek Talaat ]             |
|       \\\\__||__//                                          |
|        [______]                                           |
|                                                           |
|                                                           |
|                   Help Menu:                              |
|                                                           |
|                                                           |
|    -d -all      [ Scan all wifi networks in dBi Unit ]    |
|    -x -all      [ Scan all wifi networks in Meters   ]    |
|    -b           [ Scan and trace specific AP         ]    |
|                                                           |
|    Example: ./WiTracer -b ec:bb:59:aa:bc:50               |
|             ./WiTracer -d -all                            |
|             ./WiTracer -x -all                            |
+-----------------------------------------------------------+
    """ + reset




if len(sys.argv) == 3:
    if sys.argv[1] == "-b":
        bssid = sys.argv[2]
        Main(None, bssid)
    elif (sys.argv[1] == "-x" or sys.argv[1] == "-d") and sys.argv[2] == "-all": 
        mon = sys.argv[1]
        Main(mon)
    else:
        Help()
else:
    Help()












