#!/usr/bin/env python

memory = [1,2,3,4,5,6,7,8,9,1,1,1]

print "memory:",memory

program_counter = 0
while (program_counter >= 0):
  	a = memory[program_counter]
     	b = memory[program_counter+1]
     	c = memory[program_counter+2]


	print "PC:",program_counter,",a:",a,",b:",b,",c:",c

     	if (a < 0 or b < 0):
        	program_counter = -1
     	else:
         	memory[b] = memory[b] - memory[a]
         	if (memory[b] > 0):
             		program_counter += 3
         	else:
             		program_counter = c


	print "memory:",memory


