#!/usr/bin/env python
# codigo extraido de:
# https://github.com/dti-montevideo/servicios-abiertos/blob/master/transporte.md

import json
import urllib
import urllib2
import sys

codigo_parada=sys.argv[1]
tipo_dia=sys.argv[2]
hora=sys.argv[3]
url_base='http://www.montevideo.gub.uy/transporteRest/'

print url_base+'pasadas/'+str(codigo_parada)+'/'+tipo_dia
r=urllib2.urlopen(url_base+'pasadas/'+str(codigo_parada)+'/'+tipo_dia+'/'+hora)
j=json.loads(r.read())
for pasada in j:
    print "Linea:", pasada['linea'], "Hora:",str(pasada['horaDesc']), "Destino:",pasada['destino']
