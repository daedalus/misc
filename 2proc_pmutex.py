# Author Darío Clavijo
import random
import time
import sys
import threading
import time

interested = []
interested.append(False)
interested.append(False)


def enter_region(process):
	global interested
	k = 0
	print "enter_region: %d" % process

	other = 1 - process
	interested[process] = True
	turn = process
	while (turn  == process and interested[other] == True):
		k += 1
		#if (k % 10000 == 0):
		#	print "process wait",process
		continue
	print "entered_critical: %d ticks %d" % (process,k)
	
def leave_region(process):
	global interested
	print "leave_region: %d" % process

	interested[process] = False

def proc(n):
	t = int(random.randint(0,1))
	enter_region(n)
	time.sleep(t)
	leave_region(n)
ts = []
for n in range(0,2):
	t = threading.Timer(0.5, proc, args=(n,))
	t.start()
	ts.append(t)

	
