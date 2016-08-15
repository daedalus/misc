#!/usr/bin/env python
# Author Dario Clavijo 2016
# Licence: GPLv3

from holidays import *
from workdays import *
from datetime import date
import sys

# calculamos licencia sin contar sabados ni domingos ni feriados
def lic(dstart,days,franqueo,holydays):

	r = [0,0,0,0]

        r[0] = workday(dstart,days)
        r[1] = workday(dstart,days + franqueo)
        r[2] = workday(dstart,days,holydays)
        r[3] = workday(dstart,days + franqueo,holydays)
	
	d = [0,0,0,0]
	
	d[0] = (r[0] - dstart).days
	d[1] = (r[1] - dstart).days
	d[2] = (r[2] - dstart).days
	d[3] = (r[3] - dstart).days

	return (r,d)

def display_res(dstart,days,franqueo,holydays,r,d):
	print "+---------------------------------------------------------------------------------------------------+"
        print "|Sin contar feriados										   |"
        print "|Empieza:",dstart,", Dias laborales:",days,", Termina:",r[0], " Dias Totales: ", (d[0])	   
        print "|Empieza:",dstart,", Dias laborales:",days+franqueo, ", Termina:",r[1], ", Dias totales:", (d[1])
	print "|												   |"

        print "|Contando feriados										   |"
        print "|Empieza:",dstart,", Dias laborales:",days,", Termina:",r[2]," Dias Totales: ", (d[2])
        print "|Empieza:",dstart,", Dias laborales:",days+franqueo, ", Termina:",r[3]," Dias Totales: ", (d[3])
	

#dstart = date(year=2016,month=9,day=20) # fecha de inicio
#holydays = [date(year=2016,month=9,day=12)] # feriado laborable en uruguay
days = 28 # dias acumulados
franqueo = 3 # horas de franqueo/8

curyear = date.today().year

def init_holidays(year):
	pascua = easter(curyear) # pascuas

	semana_santa = [0,0,0,0,0]

	semana_santa[0] = pascua - timedelta(days=6) # lunes santo
	semana_santa[1] = pascua - timedelta(days=5) # martes santo
	semana_santa[2] = pascua - timedelta(days=4) # miercoles santo
	semana_santa[3] = pascua - timedelta(days=3) # jueves santo
	semana_santa[4] = pascua - timedelta(days=2) # viernes santo

	carnaval = [0,0]
	carnaval[0] = pascua - timedelta(days=7) - timedelta(days=40)
	carnaval[1] = carnaval[0] + timedelta(days=1)

	# Feriados en Uruguay
	holidays = [ # feriados no laborables
		date(year=curyear, month=1, day=1),
		date(year=curyear, month=5, day=1),
		date(year=curyear, month=7, day=18),
		date(year=curyear, month=8, day=25),
		date(year=curyear, month=12, day=25),

		# semana santa
		semana_santa[0],
		semana_santa[1],
		semana_santa[2],
		semana_santa[3],
		semana_santa[4],

		carnaval[0],
		carnaval[1],
	
		# feriados laborables

	date(year=curyear, month=6, day=19),
	date(year=curyear, month=5, day=18),
	date(year=curyear, month=4, day=19),
	date(year=curyear, month=11, day=2),
	date(year=curyear, month=10, day=12),
	date(year=curyear, month=1, day=6)
	]
	return holidays

def print_holidays():
	for h in holidays:
		print h

def calculate_best_candidate(start_date,days,franqueo):

	start_date = datetime.strptime(start_date,"%d-%m-%Y").date()
	print "parametros:",start_date,days,franqueo
	dstart = start_date


	last_best = 0
	hs = init_holidays(dstart.year)
	best = []
	for i in range(0, 365):
		#dstart += timedelta(days=1)

		r,d = lic(dstart,days,franqueo,hs)
		best_d = max(d)
		if best_d > last_best:
			#if dstart >= start_date:
			last_best = best_d
			best.append((dstart,r,d))


	 	#best.append((dstart,r,d))
		#sorted(best)
		dstart += timedelta(days=1)

		
	
	for dstart,r,d in best:
		#print dstart,r[3],d[3]
		display_res(dstart,days,franqueo,hs,r,d)

calculate_best_candidate(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))
