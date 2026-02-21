#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
import sys

def sendmail(S, OACI_AR):
    msg = EmailMessage()
    msg.set_content(S)
    msg['Subject'] = f'ATENCION: Nuevo vuelo del %s!!!' % OACI_AR
    msg['From'] = 'dclavijo@whiskey.antel.net.uy'
    msg['To'] = 'dclavijo@protonmail.com'
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()


def proc(OACI_AR):
  OACI_AR = OACI_AR.upper()
  fp = open("/tmp/%s.txt","r+" % OACI_AR)
  linesR = [line.rstrip() for line in fp.readlines()]
  linesW = []
  URL = "https://dinacia.gub.uy/search/contenido?keys=%s+" % OACI_AR
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
  results = soup.find('ol',class_="list-group node_search-results")
  newc = str(results.prettify())
  for n,e in enumerate(results.find_all("p")):
    sOACI_AR = OACI_AR.replace("-","")
    s = str(e)[3:].split("\n")[0].replace("<strong>","").replace("</strong>","").replace(OACI_AR,sOACI_AR).replace(OACI_AR.lower(),sOACI_AR).split("-")
    if s != ["<em></em></p>"]:
      if s[1] == 'Internacional Ángel S. Adami': s[1]='SUAA'
      s = s[:3] +  [s[3].replace(" ","")] + [s[4].replace(" ","")]
      s2=";".join(s)
      linesW.append(s2)
  if linesW != linesR:
    S = "\n".join(linesW)
    print("="*60)
    print(S)
    fp.seek(0)
    for line in linesW:
      fp.writelines(line+"\n")
    sendmail(S, OACI_AR)
    print("-"*60)
  fp.close() 

if __name__ == "__main__":
  proc(sys.argv[1])
