import hashlib, binascii, hmac
from pbkdf2 import PBKDF2


def PMKID(apmac, clmac, PSK, SSID):
    pmk = PBKDF2(PSK, SSID, 4096).read(32)
    apmac = binascii.unhexlify(apmac.replace(":", ""))
    clmac = binascii.unhexlify(clmac.replace(":", ""))
    pmkid = hmac.new(pmk, "PMK Name" + apmac + clmac, hashlib.sha1).digest()
    return pmkid, pmk


REQ = "2a416a999af0a6bf454684269afb06ef"
print "Required hash: %s" % REQ
apmac = "34:bf:90:4a:bb:57"
clmac = "98:de:d0:1a:97:c2"
PSK = "786 5555"
SSID = "unknown"

print "SSID: [%s]" % SSID
print "PSK: [%s]" % PSK
print "AP mac: %s" % apmac
print "Cl mac: %s" % clmac
print "HASH: %s*%s*%s*%s" % (
    REQ,
    apmac.replace(":", ""),
    clmac.replace(":", ""),
    binascii.hexlify(SSID),
)

pmkid, pmk = PMKID(apmac, clmac, PSK, SSID)
print "PMK: " + binascii.hexlify(pmk)
print "PMKID: " + binascii.hexlify(pmkid[0:32])
