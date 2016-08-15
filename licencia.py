from workdays import *
from datetime import date

# calculamos mi licencia sin contar sabados ni domingos ni el 12-10-2016
def lic():
        dstart = date(year=2016,month=9,day=20) # fecha de inicio
        d12 = date(year=2016,month=9,day=12) # feriado laborable en uruguay
        days = 28 # dias acumulados
        franqueo = 3 # horas de franqueo/8

        r1 = workday(dstart,days)
        r2 = workday(dstart,days + franqueo)
        r3 = workday(dstart,days,[d12])
        r4 = workday(dstart,days + franqueo,[d12])

        print "Sin contar:",d12
        print "Empieza:",dstart,", Dias:",days,", Termina:",r1
        print "Empieza:",dstart,", Dias:",days+franqueo, ", Termina:",r1
        print

        print "Contando:", d12
        print "Empieza:",dstart,", Dias:",days,", Termina:",r3
        print "Empieza:",dstart,", Dias:",days+franqueo, ", Termina:",r4


lic()

