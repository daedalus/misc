# !/usr/bin/env python
# author Dario Clavijo 2016
 
workdays import *
from datetime import date

# calculamos mi licencia sin contar sabados ni domingos ni el 12-10-2016
def lic():
        dstart = date(year=2016,month=9,day=20)
        d12 = date(year=2016,month=9,day=12)
        days = 28
        franqueo = 3

        r1 = workday(dstart,days,[d12])
        r2 = workday(dstart,days + franqueo,[d12])

        print "Empieza:",dstart,", Dias:",days,", Termina:",r1
        print "Empieza:",dstart,", Dias:",days+franqueo, ", Termina:",r2

lic()
