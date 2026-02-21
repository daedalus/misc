from hashlib import sha256
import datetime
import sys

def obfuscate(s):
    dt = datetime.datetime(2026, 2, 2)
    offset = int(dt.timestamp())+ (5*3600)
    tmp = "Fecha\tDe\tA\tDuracion\n"

    for i in range(0,len(s),4):
        x = s[i:i+4]
        z = int(x[:-2],16)
        y = int(x,16) + offset + (86400 * (i >> 2))
        s_datetime = datetime.datetime.fromtimestamp(y)
        dur = str(datetime.timedelta(seconds=z))[2:]
        tmp += "%s\tSUAA\tSUAA\t%s\n" % (s_datetime,dur)

    return tmp

s = sys.argv[1].encode()
print(obfuscate(s))
