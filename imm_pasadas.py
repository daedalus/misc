#!/usr/bin/env python
# codigo extraido de:
# https://github.com/dti-montevideo/servicios-abiertos/blob/master/transporte.md

import json
import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
import sys

l = len(sys.argv)
# print l

codigo_parada = sys.argv[1]
tipo_dia = sys.argv[2]
hora = sys.argv[3]
if l > 4:
    linea = sys.argv[4]

url_base = "http://www.montevideo.gub.uy/transporteRest/"

url = (
    f"{url_base}pasadas/{str(codigo_parada)}/{tipo_dia}/{str(linea)}/{hora}"
    if l > 4
    else f"{url_base}pasadas/{str(codigo_parada)}/{tipo_dia}/{hora}"
)
j = json.loads(urllib.request.urlopen(url).read())
for pasada in j:
    print(
        "Linea:",
        pasada["linea"],
        "Hora:",
        pasada["horaDesc"],
        "Destino:",
        pasada["destino"],
    )
