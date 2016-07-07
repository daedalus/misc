import random

p = """<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>301 Moved Permanently</title>
</head><body>
<h1>Moved Permanently</h1>
<p>The document has moved <a href="https://www.random.org/cgi-bin/randbyte?nbytes=32&amp;format=f">here</a>.</p>
<hr>
<address>Apache/2.2.22 (Debian) Server at www.random.org Port 80</address>
</body></html>"""




def hexify(i):
        return hex(i).replace('0x','').replace('L','').zfill(64)

t = p[:32]
random.seed(t)


def iter():
	while True:
		b = random.getrandbits(256)
		print hexify(b)

iter()
